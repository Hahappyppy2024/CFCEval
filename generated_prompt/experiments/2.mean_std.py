from CFCEval4AIWARE.metric.ELRM import calculate_ELRM
import pandas as pd
import pandas as pd
import numpy as np
from scipy import stats
from codebleu import calc_codebleu
import json
import os



def Collect_ELRM(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    elrm_scores = {}
    bleu_scores={}
    for key, value_dict in data.items():
        if isinstance(value_dict, dict):
            if "ELRM" in value_dict and value_dict["ELRM"]>0:
                elrm_scores[key] = value_dict["ELRM"]
            if "ngram_blue_score" in value_dict and value_dict["ngram_blue_score"]>0:
                bleu_scores[key] = value_dict["ngram_blue_score"]
    return elrm_scores,bleu_scores



def Collect_CodeBLEU(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    codebleu_scores = {}
    for key, value_dict in data.items():
        if isinstance(value_dict, dict):
            if "codebleu" in value_dict and value_dict["codebleu"]>0:
                codebleu_scores[key] = value_dict["codebleu"]
    return codebleu_scores

def dump_dict(dic,filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(dic, f, ensure_ascii=False, indent=4)

def iterate_ELRM():
    path="D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/experiments/data/score/"
    # 遍历所有文件
    matching_files = []
    elrm_files = []
    codebleu_files = []

    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)
        if not filename.endswith(".json"):
            continue  # 只处理 JSON 文件
        if "ELRM" in filename:
            elrm_files.append(os.path.abspath(full_path))
        if "CodeBLEU" in filename:
            codebleu_files.append(os.path.abspath(full_path))

    filename_ELRM={}
    filename_BLEU={}
    filename_CodeBLEU={}
    for file in elrm_files:
        filename=file.split("\\")[-1]
        elrm_scores, bleu_scores=Collect_ELRM(file)
        filename_ELRM[filename]=list(elrm_scores.values())
        filename_BLEU[filename]=list(bleu_scores.values())
    for file in codebleu_files:
        filename = file.split("\\")[-1]
        codebleu_scores=Collect_CodeBLEU(file)
        filename_CodeBLEU[filename] = list(codebleu_scores.values())


    print(filename_CodeBLEU)
    dump_dict(filename_ELRM,"ELRM.json")
    dump_dict(filename_BLEU, "BLEU.json")
    dump_dict(filename_CodeBLEU, "codeBLEU.json")


    return  filename_ELRM,filename_BLEU,filename_CodeBLEU



iterate_ELRM()






def calculate_mean_variance_t():
    # 示例数据
    with open("ELRM.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    cursor=data['cursor_ELRM.json']
    copilot=data['copilot_ELRM.json']
    codegeex=data['codeGeeX_ELRM.json']
    deepseekcoder=data['DeepSeekCoder_ELRM.json']
    # 计算均值和标准差
    mean_A = np.mean(cursor)
    std_A = np.std(cursor, ddof=1)  # 样本标准差，设置 ddof=1
    ###############
    mean_B = np.mean(copilot)
    std_B = np.std(copilot, ddof=1)
    #################
    mean_C = np.mean(codegeex)
    std_C = np.std(codegeex, ddof=1)
    #################
    mean_D = np.mean(deepseekcoder)
    std_D = np.std(deepseekcoder, ddof=1)
    #################
    print(f"Mean A: {mean_A:.4f}, Std A: {std_A:.4f}")
    print(f"Mean B: {mean_B:.4f}, Std B: {std_B:.4f}")
    print(f"Mean C: {mean_C:.4f}, Std A: {std_C:.4f}")
    print(f"Mean d: {mean_D:.4f}, Std B: {std_D:.4f}")

    # 进行独立样本 t 检验（假设 A 和 B 是独立样本）
    t_stat1, p_value1 = stats.ttest_ind(cursor, copilot, equal_var=False)  # Welch's t-test 更稳健
    t_stat2, p_value2 = stats.ttest_ind(codegeex, copilot, equal_var=False)  # Welch's t-test 更稳健
    t_stat3, p_value3 = stats.ttest_ind(codegeex, deepseekcoder, equal_var=False)  # Welch's t-test 更稳健
    t_stat4, p_value4 = stats.ttest_ind(cursor, deepseekcoder, equal_var=False)  # Welch's t-test 更稳健
    print(f"T-statistic: {t_stat1:.4f}, p-value: {p_value1:.4f}")
    print(f"T-statistic: {t_stat2:.4f}, p-value: {p_value2:.4f}")
    print(f"T-statistic: {t_stat3:.4f}, p-value: {p_value3:.4f}")
    print(f"T-statistic: {t_stat4:.4f}, p-value: {p_value4:.4f}")
    return



# calculate_mean_variance_t()