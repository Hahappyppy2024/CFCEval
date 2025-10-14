import string
import token
import tokenize
from pathlib import Path
from io import StringIO
from CFCEval4AIWARE.metric.utils.get_keywords_ops_com_ter import get_keywords_ops_comment
from CFCEval4AIWARE.metric.utils.tokenizer import get_ref_hyper_tokens_key_ops
from CFCEval4AIWARE.metric.utils.utils import ngrams
from CFCEval4AIWARE.metric import bleu
PACKAGE_DIR = Path(__file__).parent

def key_ops_match(reference_key_ops,hypothesis_key_ops,language,weights=(0.25, 0.25, 0.25, 0.25)):
    '''----solve no ast tree: semantic correctness,
    Example 1
    >>> prediction1_str=
    >>> patch1_str=
    >>> prediction2=[]
    >>> patch2=[]

    Example 2
    >>> prediction1_str=
    >>> patch1_str=
    >>> prediction2=[]
    >>> patch2=[]
    '''
    # reference_all_tokens,reference_key_ops, hypothesis_all_tokens, hypothesis_key_ops=get_ref_hyper_tokens_key_ops(
    #     reference_str,
    #     hypothesis_str,
    #     language,
    #     weights=(0.25, 0.25, 0.25, 0.25))
    # print("reference_key_ops")
    # print(reference_key_ops)
    # print("hypothesis_key_ops")
    # print(hypothesis_key_ops)
    total_count = 0
    match_count = 0
    match_count_candidate_to_reference = 0
    for r_token in reference_key_ops:
        if r_token in hypothesis_key_ops:
            match_count += 1

    for h_token in hypothesis_key_ops:
        if h_token in reference_key_ops:
            match_count_candidate_to_reference += 1

    total_count += len(reference_key_ops)
    # print(f'match_count       {match_count} / {total_count}')
    # print(f'match_count_fixed {match_count_candidate_to_reference} / {total_count}')
    match_score = match_count / total_count
    return match_score


def weighted_key_ops_match(reference_key_ops,hypothesis_key_ops,language,weights=(0.25, 0.25, 0.25, 0.25)):
    '''----solve no ast tree: semantic correctness,
    Example 1
    >>> prediction1_str=
    >>> patch1_str=
    >>> prediction2=[]
    >>> patch2=[]

    Example 2
    >>> prediction1_str=
    >>> patch1_str=
    >>> prediction2=[]
    >>> patch2=[]
    '''
    # reference_all_tokens,reference_key_ops, hypothesis_all_tokens, hypothesis_key_ops=get_ref_hyper_tokens_key_ops(
    #     reference_str,
    #     hypothesis_str,
    #     language,
    #     weights=(0.25, 0.25, 0.25, 0.25))

    total_count = 0
    match_count = 0
    match_count_candidate_to_reference = 0
    for r_token in reference_key_ops:
        if r_token in hypothesis_key_ops:
            match_count += 1

    for h_token in hypothesis_key_ops:
        if h_token in reference_key_ops:
            match_count_candidate_to_reference += 1

    total_count += len(reference_key_ops)
    # print(f'match_count       {match_count} / {total_count}')
    # print(f'match_count_fixed {match_count_candidate_to_reference} / {total_count}')
    match_score = match_count / total_count
    return match_score

def key_ops_blue_score(reference_key_ops,hypothesis_key_ops,language,weights=(0.25, 0.25, 0.25, 0.25)):
    '''----solve no ast tree: semantic correctness,
    Example 1
    >>> prediction1_str=
    >>> patch1_str=
    >>> prediction2=[]
    >>> patch2=[]

    Example 2
    >>> prediction1_str=
    >>> patch1_str=
    >>> prediction2=[]
    >>> patch2=[]
    '''
    # reference_all_tokens,reference_key_ops, hypothesis_all_tokens, hypothesis_key_ops=get_ref_hyper_tokens_key_ops(
    #     reference_str,
    #     hypothesis_str,
    #     language,
    #     weights=(0.25, 0.25, 0.25, 0.25))
    ref_hypo_blue_score=bleu.corpus_bleu(reference_key_ops, hypothesis_key_ops)
    return ref_hypo_blue_score


def weighted_key_ops_blue_score(reference_key_ops,hypothesis_key_ops,language,weights=(0.25, 0.25, 0.25, 0.25)):
    '''----solve no ast tree: semantic correctness,
    Example 1
    >>> prediction1_str=
    >>> patch1_str=
    >>> prediction2=[]
    >>> patch2=[]

    Example 2
    >>> prediction1_str=
    >>> patch1_str=
    >>> prediction2=[]
    >>> patch2=[]
    '''
    # reference_all_tokens,reference_key_ops, hypothesis_all_tokens, hypothesis_key_ops=get_ref_hyper_tokens_key_ops(
    #     reference_str,
    #     hypothesis_str,
    #     language,
    #     weights=(0.25, 0.25, 0.25, 0.25))
    ref_hypo_blue_score=bleu.corpus_bleu(reference_key_ops, hypothesis_key_ops)

    return ref_hypo_blue_score



# def all_tokens_match(reference_str,hypothesis_str,language,weights=(0.25, 0.25, 0.25, 0.25)):
#     '''----solve no ast tree: semantic correctness,
#     Example 1
#     >>> prediction1_str=
#     >>> patch1_str=
#     >>> prediction2=[]
#     >>> patch2=[]
#
#     Example 2
#     >>> prediction1_str=
#     >>> patch1_str=
#     >>> prediction2=[]
#     >>> patch2=[]
#     '''
#     reference_all_tokens,reference_key_ops, hyperthesis_all_tokens, hyperthesis_key_ops=get_ref_hyper_tokens_key_ops(
#         reference_str,
#         hypothesis_str,
#         language,
#         weights=(0.25, 0.25, 0.25, 0.25))
#     total_count=0
#     match_count=0
#     match_count_candidate_to_reference=0
#     for r_token in reference_all_tokens:
#         if r_token in hyperthesis_all_tokens:
#             match_count += 1
#
#     for h_token in hyperthesis_all_tokens:
#         if h_token in reference_all_tokens:
#             match_count_candidate_to_reference += 1
#
#     total_count += len(reference_all_tokens)
#     # print(f'match_count       {match_count} / {total_count}')
#     # print(f'match_count_fixed {match_count_candidate_to_reference} / {total_count}')
#     score = match_count / total_count
#     return score
#
# def weighted_all_tokens_match(reference_str,hypothesis_str,language,weights=(0.25, 0.25, 0.25, 0.25)):
#     '''----solve no ast tree: semantic correctness,
#     Example 1
#     >>> prediction1_str=
#     >>> patch1_str=
#     >>> prediction2=[]
#     >>> patch2=[]
#
#     Example 2
#     >>> prediction1_str=
#     >>> patch1_str=
#     >>> prediction2=[]
#     >>> patch2=[]
#     '''
#     reference_all_tokens,reference_key_ops, hypothesis_all_tokens, hypothesis_key_ops=get_ref_hyper_tokens_key_ops(
#         reference_str,
#         hypothesis_str,
#         language,
#         weights=(0.25, 0.25, 0.25, 0.25))
#     total_count = 0
#     match_count = 0
#     match_count_candidate_to_reference = 0
#     for r_token in reference_key_ops:
#         if r_token in hypothesis_key_ops:
#             match_count += 1
#
#     for h_token in hypothesis_key_ops:
#         if h_token in reference_key_ops:
#             match_count_candidate_to_reference += 1
#
#     total_count += len(reference_all_tokens)
#     # print(f'match_count       {match_count} / {total_count}')
#     # print(f'match_count_fixed {match_count_candidate_to_reference} / {total_count}')
#     score = match_count / total_count
#
#     return
#
#
# def all_tokens_blue_score(reference_str,hypothesis_str,language,weights=(0.25, 0.25, 0.25, 0.25)):
#     '''----solve no ast tree: semantic correctness,
#     Example 1
#     >>> prediction1_str=
#     >>> patch1_str=
#     >>> prediction2=[]
#     >>> patch2=[]
#
#     Example 2
#     >>> prediction1_str=
#     >>> patch1_str=
#     >>> prediction2=[]
#     >>> patch2=[]
#     '''
#     reference_all_tokens,reference_key_ops, hypothesis_all_tokens, hypothesis_key_ops=get_ref_hyper_tokens_key_ops(
#         reference_str,
#         hypothesis_str,
#         language,
#         weights=(0.25, 0.25, 0.25, 0.25))
#     ref_hypo_blue_score=bleu.corpus_bleu(reference_all_tokens, hypothesis_all_tokens)
#
#     return ref_hypo_blue_score
