import pandas
import json
import re
import os
from scipy.stats import pearsonr


def dump_dict_to_json(data_dict, filename):
    """
    将字典保存为json文件

    :param data_dict: 要保存的字典
    :param filename: 保存的文件名
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data_dict, f, ensure_ascii=False, indent=4)

def collect_LLM_score():
    A4 = "D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/experiments/LLMs_judgement/A_chatGPT-4o/"
    B4_1 = "D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/experiments/LLMs_judgement/B-chatGPT-4.1/"
    C_o3 = "D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/experiments/LLMs_judgement/C-chatGPT-o3/"

    target_folders = ['1_cursor', '2_copilot','3_codeGeeX', '4_deepseekCoder']
    cursor=[]
    copilot=[]
    codeGeeX=[]
    deepseekCoder=[]
    # all_chatgpt4o={}
    all_chatgpt41={}
    # all_chatgpto3={}

    score_pattern = re.compile(r'score[:：]\s*([\d\.]+)', re.IGNORECASE)
    for folder in target_folders:
        folder_path = os.path.join(B4_1, folder)
        folder_name = folder.split("_")[-1]
        if not os.path.isdir(folder_path):
            continue
        for dirpath, _, filenames in os.walk(folder_path):
            for filename in filenames:
                if filename.endswith('.txt'):
                    score=0
                    file_path = os.path.join(dirpath, filename)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        # 倒序查找带有score的最后一行
                        for line in reversed(lines):
                            if line.lower().startswith("score"):
                                score = int(line.split(":")[-1].strip())
                                print(f'{file_path} -> score: {str(score)}')
                                break
                            # if match:
                            #     print(f'{file_path} -> score: {match.group(1)}')
                            #     print(match.group(1))
                    if folder_name == 'cursor':
                        cursor.append(score)
                    elif folder_name == "copilot":
                        copilot.append(score)
                    elif folder_name == "codeGeeX":
                        codeGeeX.append(score)
                    elif folder_name == "deepseekCoder":
                        deepseekCoder.append(score)

        all_chatgpt41["cursor"]=cursor
        all_chatgpt41["copilot"] = copilot
        all_chatgpt41["codeGeeX"] = codeGeeX
        all_chatgpt41["deepseekCoder"] = deepseekCoder

    dump_dict_to_json(all_chatgpt41,"all_chatgpt41.json")
    # print(all_chatgpt41)
    return

# collect_LLM_score()


def load_json_to_dict(filename):
    """
    从JSON文件读取并返回为字典

    :param filename: JSON文件名
    :return: 读取到的字典
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data_dict = json.load(f)
    return data_dict

def collect_LLM_score():
    chatGPT4o=load_json_to_dict("D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/experiments/LLMs_judgement/all_chatgpt4o.json")
    chatGPT41=load_json_to_dict("D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/experiments/LLMs_judgement/all_chatgpt41.json")
    chatGPT3o=load_json_to_dict("D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/experiments/LLMs_judgement/all_chatgpto3.json")

    cursor=[]
    copilot=[]
    codeGeeX=[]
    deepseekCoder=[]
    for key1,value1 in chatGPT4o.items():

        if "cursor" in key1:
            cursor.extend(value1)
        elif "copilot" in key1:
            copilot.extend(value1)
        elif "codeGeeX" in key1:
            codeGeeX.extend(value1)
        elif "deepseekCoder" in key1:
            deepseekCoder.extend(value1)

    for key2, value2 in chatGPT41.items():
        if "cursor" in key2:
            cursor.extend(value2)
        elif "copilot" in key2:
            copilot.extend(value2)
        elif "codeGeeX" in key2:
            codeGeeX.extend(value2)
        elif "deepseekCoder" in key2:
            deepseekCoder.extend(value2)

    for key, value in chatGPT3o.items():
        if "cursor" in key:
            cursor.extend(value)
        elif "copilot" in key:
            copilot.extend(value)
        elif "codeGeeX" in key:
            codeGeeX.extend(value)
        elif "deepseekCoder" in key:
            deepseekCoder.extend(value)



    all_LLMS_score={
        "cursor":cursor,
        "copilot":copilot,
        "codeGeeX": codeGeeX,
        "deepseekCoder": deepseekCoder,
    }
    dump_dict_to_json(all_LLMS_score,"all_LLMs_score.json")
    average_scores = {}
    for name, scores in all_LLMS_score.items():
        if scores:  # 防止列表为空
            avg = sum(scores) / len(scores)
        else:
            avg = 0
        average_scores[name] = avg
    print(average_scores)
    return
# collect_LLM_score()

def comparsion():
    def dict_list_average(d):
        avg_dict = {}
        for key, values in d.items():
            # 转为 float（如果需要），并计算均值
            nums = [float(x) for x in values]
            avg = sum(nums) / len(nums) if nums else 0
            avg_dict[key] = avg
        return avg_dict
    BLEU=load_json_to_dict("D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/experiments/LLMs_judgement/BLEU.json")
    codeBLEU=load_json_to_dict("D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/experiments/LLMs_judgement/codeBLEU.json")
    ELRM=load_json_to_dict("D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/experiments/LLMs_judgement/ELRM.json")

    bleu_avg = dict_list_average(BLEU)
    codebleu_avg = dict_list_average(codeBLEU)
    elrm_avg = dict_list_average(ELRM)

    print("BLEU 平均值：", bleu_avg)
    print("codeBLEU 平均值：", codebleu_avg)
    print("ELRM 平均值：", elrm_avg)
    return
# comparsion()


def calcualte_Pearson_correlation_coefficients():

    keys = ['cursor', 'copilot', 'deepseekCoder', 'codeGeeX']

    LLMs=load_json_to_dict("D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/experiments/LLMs_judgement/all_LLMs_score.json")
    BLEU=load_json_to_dict("D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/experiments/LLMs_judgement/BLEU.json")
    codeBLEU=load_json_to_dict("D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/experiments/LLMs_judgement/codeBLEU.json")
    ELRM=load_json_to_dict("D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/experiments/LLMs_judgement/ELRM.json")

    for key in keys:
        # 如果每个 value 是列表，去平均值；如果直接是数字，可以注释掉下面这一行
        bleu_vals = BLEU[key] if isinstance(BLEU[key], list) else [BLEU[key]]
        elrm_vals = ELRM[key] if isinstance(ELRM[key], list) else [ELRM[key]]
        codebleu_vals = codeBLEU[key] if isinstance(codeBLEU[key], list) else [codeBLEU[key]]
        llms_vals = LLMs[key] if isinstance(LLMs[key], list) else [LLMs[key]]

        # 如果你的分数是列表，且BLEU和LLMs长度相同，可以直接相关性；如果只是单一数字，不用pearson相关性
        # 这里以平均分为例，若你想用原始list相关性可调整
        bleu_avg = sum(map(float, bleu_vals)) / len(bleu_vals)
        elrm_avg = sum(map(float, elrm_vals)) / len(elrm_vals)
        codebleu_avg = sum(map(float, codebleu_vals)) / len(codebleu_vals)
        llms_avg = sum(map(float, llms_vals)) / len(llms_vals)

        # 自动对齐长度到最短
        min_len = min(len(bleu_vals), len(llms_vals), len(elrm_vals), len(codebleu_vals))

        if min_len < 2:
            print(f"{key}: 样本数不足，无法计算Pearson相关性。")
            continue

        bleu_vals_aligned = bleu_vals[:min_len]
        elrm_vals_aligned = elrm_vals[:min_len]
        codebleu_vals_aligned = codebleu_vals[:min_len]
        llms_vals_aligned = llms_vals[:min_len]

        pearson_bleu = pearsonr(bleu_vals_aligned, llms_vals_aligned)[0]
        pearson_elrm = pearsonr(elrm_vals_aligned, llms_vals_aligned)[0]
        pearson_codebleu = pearsonr(codebleu_vals_aligned, llms_vals_aligned)[0]

        print(f"{key}:")
        print(f"  BLEU & LLMs Pearson: {pearson_bleu:.4f}")
        print(f"  ELRM & LLMs Pearson: {pearson_elrm:.4f}")
        print(f"  codeBLEU & LLMs Pearson: {pearson_codebleu:.4f}\n")


        # min_len = min(len(bleu_vals), len(llms_vals))
        # if min_len > 1:
        #     bleu_vals_aligned = bleu_vals[:min_len]
        #     llms_vals_aligned = llms_vals[:min_len]
        #     pearson = pearsonr(bleu_vals_aligned, llms_vals_aligned)[0]
        #     print(f"  BLEU & LLMs: {pearson}")
        # else:
        #     print("  BLEU & LLMs: NA")
        # print(f"{key}:")
        # 若你有分数list且长度大于1，建议用list算pearson；否则直接输出pair的均值
        # print(f"  BLEU & LLMs: {pearsonr(bleu_vals, llms_vals)[0] if len(bleu_vals) > 1 else 'NA'}")
        # print(f"  ELRM & LLMs: {pearsonr(elrm_vals, llms_vals)[0] if len(elrm_vals) > 1 else 'NA'}")
        # print(f"  codeBLEU & LLMs: {pearsonr(codebleu_vals, llms_vals)[0] if len(codebleu_vals) > 1 else 'NA'}")

    return



def calcualte_Pearson_correlation_coefficients2():
    from scipy.stats import pearsonr

    ELRM = [0.322941,
            0.504458,
            0.183283,
            0.559772,
            0.118703,
            0.02133,
            0.852662,
            0.224746,
            0.704683,
            0.144269]
    BLEU = [0.40896,
            0.557854,
            0.122095,
            0.616603,
            0.147722,
            0.02338,
            0.701688,
            0.38988,
            1, 0.22814]
    BLEU2=[0,
           0,
           0.000104,
           0,
           0,
           0.254066,
           0,
           0,
           0,
           0]

    codeBLEU = [0,
                0,
                0.029545,
                0,
                0,
                0,
                0.628775,
                0,
                0,
                0]
    LLMs = [3,
            5,
            1,
            2,
            1,
            2,
            5,
            2,
            5,
            2]

    print("ELRM & LLMs Pearson:", pearsonr(ELRM, LLMs)[0])
    print("BLEU & LLMs Pearson:", pearsonr(BLEU, LLMs)[0])
    print("BLEU2 & LLMs Pearson:", pearsonr(BLEU2, LLMs)[0])
    print("codeBLEU & LLMs Pearson:", pearsonr(codeBLEU, LLMs)[0])

    return


calcualte_Pearson_correlation_coefficients2()
