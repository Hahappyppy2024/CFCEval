import string
import token
import tokenize
from io import StringIO
from CFCEval4AIWARE.metric.utils.get_keywords_ops_com_ter import get_keywords_ops_comment
from CFCEval4AIWARE.metric.utils.utils import ngrams

def remove_comment(code_lines,language):
    # print("langage:"+ language)
    _, _, comment,_=get_keywords_ops_comment(language)
    cleaned_line=[]
    for line in code_lines:
        line=line.strip()
        # print("line :"+line)
        # print("coment:"+comment)
        # print("line[0:2]"+ line[0:2])
        if comment not in line[0:2]:
            cleaned_line.append(line)
    return cleaned_line

def get_ops_keywords(code_lines,language):
    cleaned_code=remove_comment(code_lines,language)
    code= " ".join(cleaned_code)
    # print("code:"+code)
    language=language.lower()
    keywords,ops,comment,_=get_keywords_ops_comment(language)
    OPERATOR_TYPES = {
        token.OP,  # Symbols like +, *, ==, etc.
        token.NAME  # Keywords like 'and', 'or', 'not', 'in', 'is'
    }
    # Tokenize and extract operators
    all_tokens,  keywords_ops=[],[]

    def extract_operators(code_str):
        # print("extract_operators code:"+code_str)
        all_tokens = []
        keywords_ops = []

        try:
            tokens = tokenize.generate_tokens(StringIO(code_str).readline)
            for tok_type, tok_str, *_ in tokens:
                if tok_str not in ['\n', ' ']:
                    all_tokens.append(tok_str)
                if tok_type == token.OP:
                    keywords_ops.append(tok_str)
                elif tok_type == token.NAME and tok_str in keywords:
                    keywords_ops.append(tok_str)
        except tokenize.TokenError as e:
            print(f"[Warning] Tokenization failed: {e}")

        return all_tokens, keywords_ops
    all_tokens, keywords_ops = extract_operators(code)
    # print("found_operators")
    # print(all_tokens)
    # print( keywords_ops )
    return all_tokens, keywords_ops


def get_ref_hyper_tokens_key_ops(
        reference_list,
        hypothesis_list,
        language,
        weights=(0.25, 0.25, 0.25, 0.25),):
    # print("reference_list")
    # print(reference_list)
    # print(hypothesis_list)
    ref_lines=reference_list[0].split("\n")
    hypo_lines=hypothesis_list[0].split("\n")
    examed_hypo=hypo_lines[0:len(ref_lines)]
    # print("all_tokens")
    # print(ref_lines)
    # print( examed_hypo)
    ref_all_tokens,ref_keywords_ops=get_ops_keywords(ref_lines,language)
    examed_hypo_all_tokens, examed_hypo_keywords_ops=get_ops_keywords(examed_hypo,language)
    ref_all_tokens= [item for item in ref_all_tokens if item and str(item).strip()]
    ref_keywords_ops= [item for item in ref_keywords_ops if item and str(item).strip()]
    examed_hypo_all_tokens= [item for item in examed_hypo_all_tokens if item and str(item).strip()]
    examed_hypo_keywords_ops= [item for item in examed_hypo_keywords_ops if item and str(item).strip()]
    # print("ref:")
    # print(ref_all_tokens)
    # print("examed hypo")
    # print(examed_hypo_all_tokens)
    return ref_all_tokens,ref_keywords_ops,examed_hypo_all_tokens, examed_hypo_keywords_ops

# generate_0="#abcabc \n return auto combined_string=s1+ s2; \n work(combined_string.c_str());"
# generate_1="#abcabc \n return auto combined_string=s1+ s2;"
# get_ref_hyper_tokens_key_ops(generate_0,generate_1,"python")
# 多行reference，
# 多行hypothesis
# 如何对比
# 1. 单行对比 代码设计多点，需要算均值，比较麻烦
# 2.多行去\n 对比--选择，


# def remove_comment(code_str,language):
#     lines=code_str.split("\n")
#     _, _, comment,_=get_keywords_ops_comment(language)
#     cleaned_line=[]
#     for line in lines:
#         if line[0:2]!=comment:
#             cleaned_line.append(line)
#     return cleaned_line
#
# def get_ops_keywords(code,language):
#     language=language.lower()
#     keywords,ops,comment,_=get_keywords_ops_comment(language)
#     OPERATOR_TYPES = {
#         token.OP,  # Symbols like +, *, ==, etc.
#         token.NAME  # Keywords like 'and', 'or', 'not', 'in', 'is'
#     }
#     # Tokenize and extract operators
#     operators = []
#     def extract_operators(code_str):
#         tokens = tokenize.generate_tokens(StringIO(code_str).readline)
#         for tok_type, tok_str, *_ in tokens:
#             # print(*_)
#             if tok_type == token.OP:
#                 operators.append(tok_str)
#             elif tok_type == token.NAME and tok_str in keywords:
#                 operators.append(tok_str)
#         return operators
#     found_operators = extract_operators(code)
#     # print("found_operators")
#     # print(found_operators)
#     return found_operators
#
#
# patch_1="auto combined_string>=s1++s2 <<=;\n if a==b: a=a++ elif a==c a=a-- :=work(combined_string.c_str()); \n return False  if else in not in"
# generate_0="auto combined_string=s1+ s2; \n work(combined_string.c_str());"
# generate1="auto combined = s1 + s2; work(combined.c_str());"
# generate2="auto string = s1 + s2; work(string.c_str());"
#
# def collect_all_lines_ops_keywords(code,language):
#     cleaned_code=remove_comment(code,language)
#     all_ops_keywords=[]
#     for line in cleaned_code:
#         ops_keywords=get_ops_keywords(line,language)
#         all_ops_keywords.append(ops_keywords)
#     return all_ops_keywords


