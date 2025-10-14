import re
import os
import glob
import json
import pandas as pd
from pathlib import Path

def iterate_togenerate_folders():
    # 匹配所有 ToGenerate 目录路径
    pattern_cursor_1 = r"D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/1_prompts_cursor/*/*/*/ToGenerate"
    pattern_copilot_2 = r"D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/2_prompts_copilot/*/*/*/ToGenerate"
    pattern_codeGeex_3 = r"D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/3_prompts_CodeGeeX4/*/*/*/ToGenerate"
    pattern_deepseekcoder_4 = r"D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/4_prompts_deepseekcoder/*/*/*/ToGenerate"
    # glob 返回的是字符串路径，转换为 Path 对象再统一为 posix 风格
    all_dirs = [Path(p).as_posix() for p in glob.glob(pattern_deepseekcoder_4) if Path(p).is_dir()]
    return all_dirs



def process_each_folder():
    togenerate_folders = iterate_togenerate_folders()

    # Collect rows for each sheet
    sheet_original = []
    sheet_rename = []
    sheet_restructure = []
    sheet_full = []

    python=[]
    ruby=[]
    java=[]
    cpp=[]
    for folder in togenerate_folders:
        print(f"\n--- Processing folder: {folder} ---")
        folder_path = Path(folder)
        CWE = folder.split("/")[-4]
        language = folder.split("/")[-3]
        dataset = folder.split("/")[-1]


        # if 'ruby' in folder and '29' not in folder:
        #     ruby.append(folder)
        # elif 'java' in folder:
        #     java.append(folder)
        # elif 'python' in folder:
        #     python.append(folder)
        # elif 'c' in folder:
        #     cpp.append(folder)



    # print(len(java))
    # print(len(cpp))
    # print(len(ruby))
    # print(len(python))
# process_each_folder()

def get_CWE_distribution1():
    import matplotlib
    matplotlib.use('Agg')  # 使用非交互式后端

    import matplotlib.pyplot as plt

    # 数据：CWE 类型和对应的漏洞数量
    cwe_types_num = {
        "CWE-79": 3,
        "CWE-89": 2,
        "CWE-352": 1,
        "CWE-22": 1,
        "CWE-78": 1,
        "CWE-416": 1,
        "CWE-94": 2,
        "CWE-20": 3,
        "CWE-287": 2,
        "CWE-269": 1,
        "CWE-502": 1,
        "CWE-200": 1,
        "CWE-918": 1,
        "CWE-798": 1,
        "CWE-190": 1,
        "CWE-400": 1,
        "CWE-835": 1,
        "CWE-611": 1,
        "CWE-310": 1,
        "CWE-1333": 1,
        "CWE-313": 1,
        "CWE-468": 1,
        "CWE-332": 1,
        "CWE-284": 1,
        "CWE-73": 1,
    }
    cwe_types = cwe_types_num.keys()
    num_vulnerabilities = cwe_types_num.values()

    # 绘图
    plt.figure(figsize=(12, 6))
    bars = plt.bar(cwe_types, num_vulnerabilities, color='steelblue')

    # 设置横轴标签旋转角度，标签和标题
    plt.xticks(rotation=60, ha='right')
    plt.xlabel("CWE Types")
    plt.ylabel("#Vulnerabilities")
    plt.title("CWE Type Distribution of Vulnerabilities")

    # 调整布局避免遮挡
    plt.tight_layout()

    # 显示图形
    plt.show()
    plt.savefig("cwe_distribution.pdf", dpi=300)
    return


def get_CWE_distribution():
    import matplotlib
    matplotlib.use('Agg')  # 非交互式后端
    import matplotlib.pyplot as plt

    # 数据
    cwe_types_num = {
        "CWE-79": 3,
        "CWE-89": 2,
        "CWE-352": 1,
        "CWE-22": 1,
        "CWE-78": 1,
        "CWE-416": 1,
        "CWE-94": 2,
        "CWE-20": 3,
        "CWE-287": 2,
        "CWE-269": 1,
        "CWE-502": 1,
        "CWE-200": 1,
        "CWE-918": 1,
        "CWE-798": 1,
        "CWE-190": 1,
        "CWE-400": 1,
        "CWE-835": 1,
        "CWE-611": 1,
        "CWE-310": 1,
        "CWE-1333": 1,
        "CWE-313": 1,
        "CWE-468": 1,
        "CWE-332": 1,
        "CWE-284": 1,
        "CWE-73": 1,
    }

    cwe_types = list(cwe_types_num.keys())
    num_vulnerabilities = list(cwe_types_num.values())

    # 绘图
    plt.figure(figsize=(12, 6))
    plt.bar(cwe_types, num_vulnerabilities, color='steelblue')

    # 设置横纵坐标字体大小和粗细
    plt.xticks(rotation=60, ha='right', fontsize=16, color='black')  # CWE 标签
    plt.yticks(fontsize=16)

    # 加粗横纵坐标 label
    # plt.xlabel("CWE Types", fontsize=20, fontweight='bold', color='black')
    plt.xlabel("CWE Types", fontsize=20, color='black')
    plt.ylabel("Vulnerability Count", fontsize=20,  color='black')

    # 加粗图标题
    # plt.title("Distribution of Vulnerabilities by CWE Types", fontsize=16, weight='bold', color='black')

    # 紧凑布局 & 保存
    plt.tight_layout()
    plt.savefig("cwe_distribution.pdf", format='pdf', dpi=300)
    plt.close()


get_CWE_distribution()