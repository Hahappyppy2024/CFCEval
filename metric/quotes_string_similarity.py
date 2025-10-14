import re
import string
import token
import tokenize
from io import StringIO
from CFCEval4AIWARE.metric.utils import get_keywords_ops_com_ter
from CFCEval4AIWARE.metric.utils.tokenizer import get_ops_keywords
from CFCEval4AIWARE.metric.utils.utils import ngrams
from difflib import SequenceMatcher
import Levenshtein

def jaccard_similarity(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    intersection = set1 & set2
    union = set1 | set2
    return len(intersection) / len(union)

def quotes_str_similarity(reference_list,hypothesis_list, language,weights=(0.25, 0.25, 0.25, 0.25),):
    '''
    To solve the diversity in generated code (Hypothesis) .
    '''

    ref_lines = reference_list[0].split("\n")

    hypo_lines = hypothesis_list[0].split("\n")
    examed_hypo = hypo_lines[0:len(ref_lines)]

    ref_str=" ".join(ref_lines)
    # print("refstr")
    #     # print(ref_str)
    hypo_str=" ".join(examed_hypo)

    def extract_strings_from_code(code_str):
        """
        Extract all string literals from the code (including those enclosed in double or single quotes).
        """
        pattern = r'(?<!\\)(["\'])(.*?)(?<!\\)\1'  # 匹配 "xxx" 或 'xxx'，排除转义引号
        matches = re.findall(pattern, code_str)
        return [match[1] for match in matches]

    extracts_ref=" ".join(extract_strings_from_code(ref_str))
    extracts_hypo = " ".join(extract_strings_from_code(hypo_str))
    # print("extracts_ref")
    # print(extracts_ref)
    # print("examed_hypo")
    # print(examed_hypo)

    similarity=0
    if "%" in extracts_hypo:
        similarity=0
    if len(extracts_ref)==0 or len(extracts_hypo)==0:
        similarity=0
    else:
        s_similari=SequenceMatcher(None, extracts_ref, extracts_hypo).ratio()
        j_similarity=jaccard_similarity(extracts_ref, extracts_hypo)
        L_similarity = 1 - Levenshtein.distance(extracts_ref, extracts_hypo) / max(len(extracts_ref), len(extracts_hypo))

        similarity=(s_similari+j_similarity+L_similarity)/3
        # print(SequenceMatcher(None, extracts_ref, extracts_hypo).ratio())
        # print(f"Jaccard Similarity: {jaccard_similarity(extracts_ref, extracts_hypo):.3f}")
        # print(f"Similarity: {similarity:.3f}")
    return similarity

# ref_str='LOGGER.error("MediaFileManager: Missing file %s" % "absolute_path")'
# hypo_str='LOGGER.error("Missing file" % absolute_path "path")'
# quotes_str_blue_score(ref_str, hypo_str, 'python', weights=(0.25, 0.25, 0.25, 0.25), )

    # total_count = 0
    # match_count = 0
    # match_count_candidate_to_reference = 0
    # for r_token in extracts_ref:
    #     if r_token in extracts_hypo:
    #         match_count += 1
    #
    # for h_token in extracts_hypo:
    #     if h_token in extracts_ref:
    #         match_count_candidate_to_reference += 1
    #
    # total_count += len(extracts_ref)
    # score = match_count / total_count

    # all_char_list=[]
    # for item in extracts:
    #     char_list=[]
    #     for c in item:
    #         if c not in string.punctuation:
    #             char_list.append(c)
    #     all_char_list.append(char_list)
    #
        # for line in code:
    #     if "%" in line:
    #         weight=1.0
    #     else:
    #         weight=0.5

    # return all_char_list