# Copyright (c) Microsoft Corporation.
# Copyright (c) 2023 Konstantin Chernyshev.
# Licensed under the MIT license.
from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple, Union
from CFCEval4AIWARE.metric import bleu,weighted_ngram_match
# from . import  dataflow_match, syntax_match
from CFCEval4AIWARE.metric.utils.utils import AVAILABLE_LANGS, get_tree_sitter_language
from CFCEval4AIWARE.metric.utils.tokenizer import get_ref_hyper_tokens_key_ops
from CFCEval4AIWARE.metric.utils.keywords import c44,csharpe107,cpp92,Dart33,Elixir15,Erlang23,Fortran103,Go25,Java67
from CFCEval4AIWARE.metric.utils.keywords import JS59,Kotlin79,Lua22, MATLAB20,ObjectiveC85,PHP69,Python38,R21,Ruby41
from CFCEval4AIWARE.metric.utils.keywords import Rust53, Scala40, Swift97
from CFCEval4AIWARE.metric.utils.get_keywords_ops_com_ter import get_keywords_ops_comment
from CFCEval4AIWARE.metric.quotes_string_similarity import quotes_str_similarity
from CFCEval4AIWARE.metric.key_ops_ngram_match import key_ops_match,weighted_key_ops_match,key_ops_blue_score,weighted_key_ops_blue_score
from CFCEval4AIWARE.metric.utils.utils import AVAILABLE_LANGUAGES
PACKAGE_DIR = Path(__file__).parent


def calculate_ELRM(
    reference: Union[List[str], List[List[str]]],
    hypothesis:List[str],
    language: str,
    weights: Tuple[float, float, float, float] = (0.25, 0.25, 0.25, 0.25),
    # tokenizer: Optional[Callable] = None,
    # keywords_dir: Path = PACKAGE_DIR / "keywords",
) -> Dict[str, float]:
    """Calculate CodeBLEU score
    Args:
        predictions: list of predictions
        references: list of lists with references
        lang: input language, one of AVAILABLE_LANGS
        weights: weights of the ngram_match, weighted_ngram_match, syntax_match, and dataflow_match respectively
        tokenizer: tokenizer function, Defaults to lambda s: s.split()
        keywords_dir: path to the directory with keywords files
        lang_so_file: path to the .so file with the parser for the language

    Return:
        Scores dict
    """
    assert len(reference) == len(hypothesis), "Number of references and predictions should be the same"
    assert language in AVAILABLE_LANGS, f"Language {language} is not supported (yet). Available languages: {AVAILABLE_LANGUAGES}"
    assert len(weights) == 4, "weights should be a tuple of 4 floats (alpha, beta, gamma, theta)"
    # assert keywords_dir.exists(), f"keywords_dir {keywords_dir} does not exist"

    # get the tree-sitter language for a given language
    # tree_sitter_language = get_tree_sitter_language(language)
    # preprocess inputs
    # references = [[x.strip() for x in ref] if isinstance(ref, list) else [ref.strip()] for ref in references]
    # hypothesis = [x.strip() for x in predictions]
    #  This tokenizer cannot correctly tokenize the code whose components have no space in between.
    # calculate ngram match (BLEU)
    # if tokenizer is None:
    #     def tokenizer(s):
    #         return s.split()
    # tokenized_hyps = [tokenizer(x) for x in hypothesis]
    # tokenized_refs = [[tokenizer(x) for x in reference] for reference in references]

    ref_all_tokens,ref_key_ops,examed_hypo_all_tokens,examed_hypo_key_ops=get_ref_hyper_tokens_key_ops(reference,hypothesis,language,weights)

    # print("ELRM FILE ref_all_tokens")
    # print(ref_all_tokens)
    # print("ELRM FILE examed_hypo_all_tokens")
    # print(examed_hypo_all_tokens)
    ngram_blue_score = bleu.corpus_bleu([ref_all_tokens], [examed_hypo_all_tokens])
    keywords,ops,comment,terminator= get_keywords_ops_comment(language)
    # calculate weighted ngram match
    # with open(keywords_dir / (language + ".txt"), "r", encoding="utf-8") as f:
    #     keywords = [x.strip() for x in f.readlines()]


    def make_weights(reference_tokens, key_word_list):
        return {token: 1 if token in key_word_list else 0.2 for token in reference_tokens}

    tokenized_refs_with_weights = [[ref_all_tokens, make_weights(ref_all_tokens, keywords)]]

    #
    # print("print(tokenized_refs_with_weights)")
    # print(len(tokenized_refs_with_weights))
    # print(tokenized_refs_with_weights)
    weighted_ngram_match_score = weighted_ngram_match.corpus_bleu([tokenized_refs_with_weights], [examed_hypo_all_tokens])

    # # Calcualte keywards ops ngram match
    keywords_ops_match_score=key_ops_match([ref_key_ops],[examed_hypo_key_ops],language,weights=(0.25, 0.25, 0.25, 0.25))
    # weighted_keywords_ops_match_score =weighted_key_ops_match(ref_key_ops,examed_hypo_key_ops,language,weights=(0.25, 0.25, 0.25, 0.25))
    keywords_ops_blue_score =key_ops_blue_score([ref_key_ops],[examed_hypo_key_ops],language,weights=(0.25, 0.25, 0.25, 0.25))
    # weighted_keywords_ops_blue_score =weighted_key_ops_blue_score([ref_key_ops],[examed_hypo_key_ops],language,weights=(0.25, 0.25, 0.25, 0.25))
    print("keywords_ops_blue_score")
    print(keywords_ops_blue_score)

    # calculate quotes_str_similarity
    quotes_string_similarity=quotes_str_similarity(reference,hypothesis,language)
    print("quotes_string_similarity")
    print(quotes_string_similarity)
    # # calculate syntax_match_score match
    # syntax_match_score = syntax_match.corpus_syntax_match(
    #     references, hypothesis, lang, tree_sitter_language=tree_sitter_language
    # )
    #
    # # calculate dataflow_match_score
    # dataflow_match_score = dataflow_match.corpus_dataflow_match(
    #     references, hypothesis, lang, tree_sitter_language=tree_sitter_language
    # )


    alpha, beta, gamma, theta = weights
    ELRM_score = (
        alpha * ngram_blue_score
        + beta * weighted_ngram_match_score
        + gamma * keywords_ops_blue_score
        + theta * quotes_string_similarity

    )

    return {
        "ELRM": ELRM_score,
        "ngram_blue_score": ngram_blue_score,
        "weighted_ngram_match_score": weighted_ngram_match_score,
        "Keywords_Ops_match_score": keywords_ops_blue_score,
        "String_Literal_Similarity_" : quotes_string_similarity,
    }
