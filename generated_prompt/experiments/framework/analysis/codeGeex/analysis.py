import json
import os
from collections import Counter

scorer_path="D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/experiments/framework/analysis/codeGeex/scorer/"
tagger_path="D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/experiments/framework/analysis/codeGeex/tagger/"



def s_collect_quality():
    def get_last_label_value(txt_path):
        """
        读取txt_path文件，找到最后出现的label，并返回其值。
        label: 不区分大小写
        """
        label_value = None
        score_value = None
        label = "classification"
        score = "score"
        with open(txt_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # 匹配 'Score: xx' 这种格式，label可换
                if line.lower().startswith(label.lower() + ":"):
                    # 取冒号后面的内容并去除多余空格
                    label_value = line.split(":", 1)[1].strip()
                if line.lower().startswith(score.lower() + ":"):
                    # 取冒号后面的内容并去除多余空格
                    score_value = line.split(":", 1)[1].strip()
        return score_value, label_value

    folder=scorer_path
    print(f"Listing files in: {folder}")
    all_score=[]
    all_label=[]
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file).replace("\\", "/")
            quality=file_path.split('/')[-3]
            print(quality)
            if quality[0]=="1":
                score_value, label_value=get_last_label_value(file_path)
                print(file_path)
                print(score_value, label_value)
                all_score.append(score_value)
                all_label.append(label_value)

    count_dict_s = Counter(all_score)
    count_dict_l = Counter(all_label)
    # Counter({'3': 7, '5': 4, '4': 4, '2': 3, '1': 2})
    # Counter({'Poor': 12, 'Good': 8})

    print(count_dict_s)
    print(count_dict_l)
    return

# s_collect_quality()

def s_collect_fixed_unfixed():
    def get_last_label_value(txt_path):
        """
        读取txt_path文件，找到最后出现的label，并返回其值。
        label: 不区分大小写
        """
        label_value = None
        score_value = None
        label = "classification"
        score = "score"
        with open(txt_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # 匹配 'Score: xx' 这种格式，label可换
                if line.lower().startswith(label.lower() + ":"):
                    # 取冒号后面的内容并去除多余空格
                    label_value = line.split(":", 1)[1].strip()
                if line.lower().startswith(score.lower() + ":"):
                    # 取冒号后面的内容并去除多余空格
                    score_value = line.split(":", 1)[1].strip()
        return score_value, label_value

    folder=scorer_path
    print(f"Listing files in: {folder}")
    all_score=[]
    all_label=[]
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file).replace("\\", "/")
            quality=file_path.split('/')[-3]
            # print(quality)
            if quality[0]=="2":
                score_value, label_value=get_last_label_value(file_path)
                print(file_path)
                print(score_value, label_value)
                all_score.append(score_value)
                all_label.append(label_value)

    count_dict_s = Counter(all_score)
    count_dict_l = Counter(all_label)
    print(count_dict_s)
    print(count_dict_l)
    return
# s_collect_fixed_unfixed()

def s_collect_resolved_unresolved():
    def get_last_label_value(txt_path):
        """
        读取txt_path文件，找到最后出现的label，并返回其值。
        label: 不区分大小写
        """
        label_value = None
        score_value = None
        label = "classification"
        score = "score"
        with open(txt_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # 匹配 'Score: xx' 这种格式，label可换
                if line.lower().startswith(label.lower() + ":"):
                    # 取冒号后面的内容并去除多余空格
                    label_value = line.split(":", 1)[1].strip()
                if line.lower().startswith(score.lower() + ":"):
                    # 取冒号后面的内容并去除多余空格
                    score_value = line.split(":", 1)[1].strip()
        return score_value, label_value

    folder=scorer_path
    print(f"Listing files in: {folder}")
    all_score=[]
    all_label=[]
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file).replace("\\", "/")
            quality=file_path.split('/')[-3]
            # print(quality)
            if quality[0]=="3":
                score_value, label_value=get_last_label_value(file_path)
                print(file_path)
                print(score_value, label_value)
                all_score.append(score_value)
                all_label.append(label_value)

    count_dict_s = Counter(all_score)
    count_dict_l = Counter(all_label)
    print(count_dict_s)
    print(count_dict_l)
    return

# s_collect_resolved_unresolved()

def s_collect_relevant_irrelevant():
    def get_last_label_value(txt_path):
        """
        读取txt_path文件，找到最后出现的label，并返回其值。
        label: 不区分大小写
        """
        label_value = None
        score_value = None
        label = "classification"
        score = "score"
        with open(txt_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # 匹配 'Score: xx' 这种格式，label可换
                if line.lower().startswith(label.lower() + ":"):
                    # 取冒号后面的内容并去除多余空格
                    label_value = line.split(":", 1)[1].strip()
                if line.lower().startswith(score.lower() + ":"):
                    # 取冒号后面的内容并去除多余空格
                    score_value = line.split(":", 1)[1].strip()
        return score_value, label_value

    folder=scorer_path
    print(f"Listing files in: {folder}")
    all_score=[]
    all_label=[]
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file).replace("\\", "/")
            quality=file_path.split('/')[-3]
            # print(quality)
            if quality[0]=="4":
                score_value, label_value=get_last_label_value(file_path)
                print(file_path)
                print(score_value, label_value)
                all_score.append(score_value)
                all_label.append(label_value)

    count_dict_s = Counter(all_score)
    count_dict_l = Counter(all_label)
    print(count_dict_s)
    print(count_dict_l)
    return
# s_collect_relevant_irrelevant()
################################################################
def t_collect_quality():
    def get_last_label_value(txt_path):
        """
        读取txt_path文件，找到最后出现的label，并返回其值。
        label: 不区分大小写
        """
        label_value = None
        label = "label"
        with open(txt_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                print(line)
                # 匹配 'Score: xx' 这种格式，label可换
                if line.lower().startswith(label.lower() + ":"):
                    # 取冒号后面的内容并去除多余空格
                    label_value = line.split(":", 1)[1].strip()
                # if line.lower().startswith(score.lower() + ":"):
                #     # 取冒号后面的内容并去除多余空格
                #     score_value = line.split(":", 1)[1].strip()
        return label_value

    folder=tagger_path
    print(f"Listing files in: {folder}")
    all_label=[]
    print(folder)
    for root, dirs, files in os.walk(folder):
        print(root)
        for file in files:
            file_path = os.path.join(root, file).replace("\\", "/")
            quality=file_path.split('/')[-3]
            print(quality)
            if quality[0]=="1":
                label_value=get_last_label_value(file_path)
                print(file_path)
                print(label_value)
                # all_score.append(score_value)
                all_label.append(label_value)

    count_dict_l = Counter(all_label)
    print(count_dict_l)
    return

# t_collect_quality()


def t_collect_fixed_unfixed():
    def get_last_label_value(txt_path):
        """
        读取txt_path文件，找到最后出现的label，并返回其值。
        label: 不区分大小写
        """
        label_value = None
        label = "label"
        with open(txt_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                print(line)
                # 匹配 'Score: xx' 这种格式，label可换
                if line.lower().startswith(label.lower() + ":"):
                    # 取冒号后面的内容并去除多余空格
                    label_value = line.split(":", 1)[1].strip()
                # if line.lower().startswith(score.lower() + ":"):
                #     # 取冒号后面的内容并去除多余空格
                #     score_value = line.split(":", 1)[1].strip()
        return label_value

    folder=tagger_path
    print(f"Listing files in: {folder}")
    all_label=[]
    print(folder)
    for root, dirs, files in os.walk(folder):
        print(root)
        for file in files:
            file_path = os.path.join(root, file).replace("\\", "/")
            quality=file_path.split('/')[-3]
            print(quality)
            if quality[0]=="2":
                label_value=get_last_label_value(file_path)
                print(file_path)
                print(label_value)
                # all_score.append(score_value)
                all_label.append(label_value)

    count_dict_l = Counter(all_label)
    print(count_dict_l)
    return

# t_collect_fixed_unfixed()

def t_collect_resolved_unresolved():
    def get_last_label_value(txt_path):
        """
        读取txt_path文件，找到最后出现的label，并返回其值。
        label: 不区分大小写
        """
        label_value = None
        label = "label"
        with open(txt_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                print(line)
                # 匹配 'Score: xx' 这种格式，label可换
                if line.lower().startswith(label.lower() + ":"):
                    # 取冒号后面的内容并去除多余空格
                    label_value = line.split(":", 1)[1].strip()
                # if line.lower().startswith(score.lower() + ":"):
                #     # 取冒号后面的内容并去除多余空格
                #     score_value = line.split(":", 1)[1].strip()
        return label_value

    folder=tagger_path
    print(f"Listing files in: {folder}")
    all_label=[]
    print(folder)
    for root, dirs, files in os.walk(folder):
        print(root)
        for file in files:
            file_path = os.path.join(root, file).replace("\\", "/")
            quality=file_path.split('/')[-3]
            print(quality)
            if quality[0]=="3":
                label_value=get_last_label_value(file_path)
                print(file_path)
                print(label_value)
                # all_score.append(score_value)
                all_label.append(label_value)

    count_dict_l = Counter(all_label)
    print(count_dict_l)
    return
t_collect_resolved_unresolved()
def t_collect_relevant_irrelevant():
    def get_last_label_value(txt_path):
        """
        读取txt_path文件，找到最后出现的label，并返回其值。
        label: 不区分大小写
        """
        label_value = None
        label = "label"
        with open(txt_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # print(line)
                # 匹配 'Score: xx' 这种格式，label可换
                if line.lower().startswith(label.lower() + ":"):
                    # 取冒号后面的内容并去除多余空格
                    label_value = line.split(":", 1)[1].strip()
                # if line.lower().startswith(score.lower() + ":"):
                #     # 取冒号后面的内容并去除多余空格
                #     score_value = line.split(":", 1)[1].strip()
        return label_value

    folder=tagger_path
    print(f"Listing files in: {folder}")
    all_label=[]
    # print(folder)
    for root, dirs, files in os.walk(folder):
        # print(root)
        for file in files:
            file_path = os.path.join(root, file).replace("\\", "/")
            quality=file_path.split('/')[-3]
            # print(quality)
            if quality[0]=="4":
                label_value=get_last_label_value(file_path)
                print(file_path)
                print(label_value)
                # all_score.append(score_value)
                all_label.append(label_value)


    count_dict_l = Counter(all_label)
    print(count_dict_l)
    return

# t_collect_relevant_irrelevant()