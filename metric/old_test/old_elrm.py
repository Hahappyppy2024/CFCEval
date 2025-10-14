import string
import pandas as pd
import math
import time
import nltk
from codebleu import calc_codebleu
import keyword
from keywords import python35,python38,c44,cpp92,cshaper107,Java67,JS59,Ryby41
import re
from operators import py_all_operators
py_operators=['+','-','*','/','//','%','>','<','=']




def get_codeBLEU(ans_list,pre_list,language):
    '''
    To install: pip install tree-sitter-python==0.21
    Function to calculate CodeBLEU, BLEU, ROUGEand Accuracy score
    pred = "def add ( a , b ) :\n return a + b"
    ref = "def sum ( first , second ) :\n return second + first"
    res = calc_codebleu([ref], [pred], "python")
    '''
    from codebleu import calc_codebleu
    res = calc_codebleu(ans_list, pre_list,language)
    return res
#
# score1=get_codeBLEU([patch_1],[generate_0])
# score2=get_codeBLEU([patch_1],[generate1])

patch_1="auto combined_string>=s1++s2 <<=;\n if a==b: a=a++ elif a==c a=a-- :=work(combined_string.c_str()); \n return False  if else in not in"
generate_0="auto combined_string=s1+ s2; work(combined_string.c_str());"
generate1="auto combined = s1 + s2; work(combined.c_str());"
generate2="auto string = s1 + s2; work(string.c_str());"



def get_operators(code,language):
    language=language.lower()
    import tokenize
    import token
    from io import StringIO
    keywords = []
    important_punc = ["+", "=", ""]
    unimportant_punc = ["_", "(", ")", "."]
    if language == "python":
        keywords = (keyword.kwlist)
    elif language == "java":
        keywords = Java67
    elif language == "c":
        keywords = c44
    elif language == "cpp":
        keywords = cpp92
    elif language == "ruby":
        keywords = Ryby41
    print("code")
    print(code)
    OPERATOR_TYPES = {
        token.OP,  # Symbols like +, *, ==, etc.
        token.NAME  # Keywords like 'and', 'or', 'not', 'in', 'is'
    }
    # Tokenize and extract operators
    operators = []
    def extract_operators(code_str):
        tokens = tokenize.generate_tokens(StringIO(code_str).readline)
        for tok_type, tok_str, *_ in tokens:
            # print(*_)
            if tok_type == token.OP:
                operators.append(tok_str)
            elif tok_type == token.NAME and tok_str in keywords:
                operators.append(tok_str)
        return operators

    found_operators = extract_operators(code)
    print("found_operators")
    print(found_operators)
    return found_operators


def get_keyword_punch_order(ans_list,pre_list,language):

    return

# get_keyword_punch_order(patch_1,generate1,"python")


def get_AlignCodeBLEU(ans_list,pre_list,language):
    # 判断标点符号位置 order
    # 判断 keywords,
    codebleu=get_codeBLEU([ans_list],[pre_list],language)
    print("codebleu score1")
    print(codebleu)
    ans_list_op=get_operators(ans_list,language)
    pre_list_op=get_operators(pre_list,language)
    print("codebleu score2")
    print(get_codeBLEU(ans_list_op,pre_list_op,language))

    return
get_AlignCodeBLEU(patch_1,generate1,"python")



def get_GLEU(ans_list,pred_list):
    from nltk.translate.gleu_score import sentence_gleu
    gleu_score = sentence_gleu([ans_list], pred_list)
    return gleu_score



def get_BLEU(ans_list,pred_list):
    '''
        from nltk.translate.bleu_score import sentence_bleu
        reference = [['this', 'is', 'a', 'test'], ['this', 'is' 'test']]
        candidate = ['this', 'is', 'a', 'test']
        score = sentence_bleu(reference, candidate)
        print(score)
    '''
    # Define your desired weights (example: higher weight for bi-grams)
    weights=(0.5, 0.5, 0, 0) # Weights for uni-gram, bi-gram, tri-gram, and 4-gram
    from nltk.translate.bleu_score import sentence_bleu
    score = sentence_bleu([ans_list], pred_list, weights=weights)
    return score


def get_ROUGE(ans_list,pred_list):#3 DIFFEENT average?
    # from pyrouge import Rouge155
    from rouge import Rouge
    ans_str=" ".join(ans_list)
    pred_str=" ".join(pred_list)
    rouge = Rouge()
    scores = rouge.get_scores(pred_str,ans_str,avg=True)
    return scores



def ELRM(ans_list, pred_list):
    '''
    Calculate the ELRM score.
    :param ans_list: List of expected answers.
    :param pred_list: List of predicted answers.
    :return: ELRM score as a float.
    '''
    if len(ans_list) == 0 or len(pred_list) == 0:
        return 0.0
    
    ans_punctuated = [word for word in ans_list if word not in string.punctuation]
    pred_punctuated = [word for word in pred_list if word not in string.punctuation]

    weighted_word=[]
    codeBleu=calc_codebleu(ans_list, pred_list, lang='python', verbose=False)

    ELRM=codeBLEU+ get_BLEU(ans_list, pred_list)
    return float(ans_list == pred_list)
