import re
import os
import glob
import json
import pandas as pd
from pathlib import Path


def extract_content_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    match = re.search(r'#\s*(.*?)\s*#', text, re.DOTALL)  # 支持跨多行
    if match:
        result = match.group(1)
        # print(f"[{file_path}] Extracted:\n{result}\n")
        return result
    else:
        # print(f"[{file_path}] No match found.\n")
        return None

def extract_content_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    blocks = []
    current_block = []
    inside_block = False

    for line in lines:
        stripped = line.strip()

        if stripped == "#":  # Only lines that are exactly '#'
            if inside_block:
                # End of a block
                if current_block:
                    blocks.append("".join(current_block).strip())
                    current_block = []
                inside_block = False
            else:
                # Start of a block
                inside_block = True
        elif inside_block:
            current_block.append(line)

    # If ends inside a block
    if inside_block and current_block:
        blocks.append("".join(current_block).strip())

    # Return the first match if exists, or None
    return blocks[0] if blocks else None


def iterate_togenerate_folders():
    # 匹配所有 ToGenerate 目录路径
    pattern_cursor_1 = r"D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/1_prompts_cursor/*/*/*/ToGenerate"
    pattern_copilot_2 = r"D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/2_prompts_copilot/*/*/*/ToGenerate"
    pattern_codeGeex_3 = r"D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/3_prompts_CodeGeeX4/*/*/*/ToGenerate"
    pattern_deepseekcoder_4 = r"D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/4_prompts_deepseekcoder/*/*/*/ToGenerate"
    # glob 返回的是字符串路径，转换为 Path 对象再统一为 posix 风格
    all_dirs = [Path(p).as_posix() for p in glob.glob(pattern_cursor_1) if Path(p).is_dir()]
    return all_dirs


def load_json_as_dict(file_path):
    """
    Load a JSON file and return its contents as a Python dictionary.
    Parameters:
        file_path (str): Path to the JSON file.
    Returns:
        dict: Parsed contents of the JSON file.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data




def process_each_folder():
    togenerate_folders = iterate_togenerate_folders()

    # Collect rows for each sheet
    sheet_original = []
    sheet_rename = []
    sheet_restructure = []
    sheet_full = []

    for folder in togenerate_folders:
        print(f"\n--- Processing folder: {folder} ---")
        folder_path = Path(folder)
        CWE = folder.split("/")[-4]
        language = folder.split("/")[-3]
        dataset = folder.split("/")[-1]

        # Initialize placeholders
        original_patch = rename_patch = restructure_patch = full_trans_patch = ""
        original_generated_code = rename_generated_code = restructured_generated_code = full_trans_generated_code = ""

        for file in folder_path.iterdir():
            if file.is_file():
                fname = file.name.lower()
                file_location_raw = str(file.resolve())
                # file_location = f'=HYPERLINK("{file_location_raw}", "Open File")'
                file_location=str(file_location_raw)
                # print("file_location:"+ file_location)
                if file.suffix.lower() == ".json":
                    data = load_json_as_dict(file)
                    original_patch = data.get("original_patch_code", "")
                    rename_patch = data.get("renamed_patch_code", "")
                    restructure_patch = data.get("restructured_patch_code", "")
                    full_trans_patch = data.get("renamed_and_restructured_patch_code", "")
                elif "original" in fname:
                    original_generated_code = extract_content_from_file(file)

                elif "rename" in fname:
                    rename_generated_code = extract_content_from_file(file)

                elif "restructure" in fname:
                    restructured_generated_code = extract_content_from_file(file)

                elif "full_trans" in fname:
                    full_trans_generated_code = extract_content_from_file(file)

        # Append to each sheet's data list
        sheet_original.append([CWE, language,file_location, original_patch, original_generated_code, "", "", "", ""])
        sheet_rename.append([CWE, language, file_location, rename_patch, rename_generated_code, "", "", "", ""])
        sheet_restructure.append([CWE, language, file_location, restructure_patch, restructured_generated_code, "", "", "", ""])
        sheet_full.append([CWE, language, file_location, full_trans_patch, full_trans_generated_code, "", "", "", ""])

    # Convert to DataFrames
    df_original = pd.DataFrame(sheet_original, columns=["CWE", "Language", "FileLocation", "Original_Patch", "Original_Generated", "ELRM", "CodeBLEU", "BLEU", "HumanScore"])
    df_rename = pd.DataFrame(sheet_rename, columns=["CWE", "Language", "FileLocation", "Rename_Patch", "Rename_Generated", "ELRM", "CodeBLEU", "BLEU", "HumanScore"])
    df_restructure = pd.DataFrame(sheet_restructure, columns=["CWE", "Language", "FileLocation", "Restructure_Patch", "Restructure_Generated", "ELRM", "CodeBLEU", "BLEU", "HumanScore"])
    df_full = pd.DataFrame(sheet_full, columns=["CWE", "Language", "FileLocation", "Full_Patch", "Full_Generated", "ELRM", "CodeBLEU", "BLEU", "HumanScore"])

    # Write to Excel
    output_path = "experiments/data/1_cursor_patch_evaluation_summary.xlsx"
    with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
        df_original.to_excel(writer, sheet_name="ORIGINAL", index=False)
        df_rename.to_excel(writer, sheet_name="RENAME", index=False)
        df_restructure.to_excel(writer, sheet_name="RESTRUCTURE", index=False)
        df_full.to_excel(writer, sheet_name="FULL_GENERATION", index=False)

    return output_path


process_each_folder()
# 我最后需要什么表格额？EXCEL
# SHEET1: ORIGIANL :cwe, language, filelocation,original patch, original_generated, align_codeblue,codeblue,blue,human score
# SHEET2:RENAME: cwe, language, filelocation,rename patch,rename generated,align_codeblue,codeblue,blue,human score
# SHEET3:RESTRUCTURE cwe, language, filelocation,restructure patch, restructure generated, align_codeblue,codeblue,blue,human score
# SHEET4:full_generation:cwe, language, filelocation,full patch, full generated,align_codeblue,codeblue,blue,human score



def dump_dict(dic,filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(dic, f, ensure_ascii=False, indent=4)


def CodeBLEU_dump_dict(dic):
    filename = "output_CodeBLEU.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(dic, f, ensure_ascii=False, indent=4)


def iterate_ref_hypo():
    cursor="D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/1_cursor_patch_evaluation_summary.xlsx"
    copilot="D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/2_copilot_patch_evaluation_summary.xlsx"
    codeGeeX="D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/3_CodeGeeX_patch_evaluation_summary.xlsx"
    DeepSeekCoder="D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/4_DeepSeekCoder_patch_evaluation_summary.xlsx"

    cursor_score={}
    copilot_score={}
    codeGeeX_score={}
    DeepSeekCoder_score={}

    excel_file = pd.ExcelFile(codeGeeX)
    sheet_names = excel_file.sheet_names
    dataframes = {}
    for sheet_name in sheet_names:
        df = excel_file.parse(sheet_name)
        dataframes[sheet_name] = df
        for index, row in df.iterrows():
            cwe = row["CWE"]
            lang = row["Language"]
            file_path = row["FileLocation"]
            print("print(sheet_name)")
            print(sheet_name)
            print("index:"+str(index))
            print("cwe:"+cwe)
            print("language:"+lang)
            patch=""
            gen=""
            ELRM=""
            codebleu=""
            name=sheet_name+"_"+cwe+"_"+lang
            if 'remove' not in cwe:
                if 'original' in str(sheet_name).lower():
                    patch = row["Original_Patch"]
                    gen = row["Original_Generated"]
                elif 'rename'  in str(sheet_name).lower():
                    patch = row["Rename_Patch"]
                    gen = row["Rename_Generated"]
                elif 'restructure' in str(sheet_name).lower():
                    patch = row["Restructure_Patch"]
                    gen = row["Restructure_Generated"]
                elif 'full' in str(sheet_name).lower():
                    patch = row["Full_Patch"]
                    gen = row["Full_Generated"]
                print("patch:"+str(len(str(patch))))
                print("gen:"+ str(len(str(gen))))
                if len(str(patch))>5 and len(str(gen))>5:
                    if "java" in lang:
                        lang="java"
                    ELRM = calculate_ELRM([patch], [gen], lang)
                    try:
                        CodeBleu=calc_codebleu([patch],[gen],lang)
                        # cwe_lang_codebleu[str(cwe)+"_"+str(lang)]=codebleu
                    except TypeError as e:
                        print(f"[ERROR] Failed to load language: {e}")
                        codebleu=0
                else:
                    codebleu=0
                    ELRM=0
                codeGeeX_score[name]=codebleu
                # print("ELRM:" + str(ELRM))
                # DeepSeekCoder_score.append(ELRM)
                # DeepSeekCoder_score.append(codebleu)
            # df.loc[index, "ELRM"] = str(ELRM)
            # df.loc[index, "CodeBLEU"] = str(CodeBleu)
            # df.to_excel(cursor,sheet_name=sheet_name )
    # ELRM={
    #     # "curosr":cursor_ELRM,
    #     # "copilot":copilot_ELRM,
    #     # "codeGeeX": codeGeeX_ELRM,
    #     # "DeepSeekCoder": DeepSeekCoder_ELRM,
    # }
    # codeBLEU={
    #     # "curosr":cursor_score,
    #     # "copilot":copilot_score,
    #     # "codeGeeX": codeGeeX_score,
    #     # "DeepSeekCoder": DeepSeekCoder_score,
    # }

    dump_dict(codeGeeX_score, "data/codeGeeX_CodeBLEU.json")
    # CodeBLEU_dump_dict(codeBLEU)
        # Perform operations on df for each sheet
    return

iterate_ref_hypo()

def iterate_ref_hypo():
    cursor="D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/experiments/data/1_cursor_patch_evaluation_summary.xlsx"
    copilot="D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/experiments/data/2_copilot_patch_evaluation_summary.xlsx"
    codeGeeX="D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/experiments/data/3_CodeGeeX_patch_evaluation_summary.xlsx"
    DeepSeekCoder="D:/000_PHD_project/000AIWARE/CFCEval4AIWARE/generated_prompt/experiments/data/4_DeepSeekCoder_patch_evaluation_summary.xlsx"


    score={}
    excel_file = pd.ExcelFile(DeepSeekCoder)
    sheet_names = excel_file.sheet_names
    dataframes = {}
    for sheet_name in sheet_names:
        df = excel_file.parse(sheet_name)
        dataframes[sheet_name] = df
        for index, row in df.iterrows():
            cwe = row["CWE"]
            lang = row["Language"]
            file_path = row["FileLocation"]
            print("print(sheet_name)")
            print(sheet_name)
            print("index:"+str(index))
            print("cwe:"+cwe)
            print("language:"+lang)
            patch=""
            gen=""
            ELRM=""
            codebleu=""
            name=sheet_name+"_"+cwe+"_"+lang
            if 'remove' not in cwe:
                if 'original' in str(sheet_name).lower():
                    patch = row["Original_Patch"]
                    gen = row["Original_Generated"]
                elif 'rename'  in str(sheet_name).lower():
                    patch = row["Rename_Patch"]
                    gen = row["Rename_Generated"]
                elif 'restructure' in str(sheet_name).lower():
                    patch = row["Restructure_Patch"]
                    gen = row["Restructure_Generated"]
                elif 'full' in str(sheet_name).lower():
                    patch = row["Full_Patch"]
                    gen = row["Full_Generated"]
                print("patch:"+str(len(str(patch))))
                print("gen:"+ str(len(str(gen))))
                if len(str(patch))>5 and len(str(gen))>5:
                    if "java" in lang:
                        lang="java"
                    # ELRM = calculate_ELRM([patch], [gen], lang)
                    try:
                        codebleu=calc_codebleu([patch],[gen],lang)
                        print(codebleu)
                        # cwe_lang_codebleu[str(cwe)+"_"+str(lang)]=codebleu
                    except TypeError as e:
                        # print(f"[ERROR] Failed to load language: {e}")
                        # print(file_path)
                        codebleu=0
                else:
                    codebleu=0
                    # ELRM=0
                print("codebleu:"+str(codebleu))
                score[name]=codebleu
                # print("ELRM:" + str(ELRM))
                # DeepSeekCoder_score.append(ELRM)
                # DeepSeekCoder_score.append(codebleu)
            # df.loc[index, "ELRM"] = str(ELRM)
            # df.loc[index, "CodeBLEU"] = str(CodeBleu)
            # df.to_excel(cursor,sheet_name=sheet_name )
    # ELRM={
    #     # "curosr":cursor_ELRM,
    #     # "copilot":copilot_ELRM,
    #     # "codeGeeX": codeGeeX_ELRM,
    #     # "DeepSeekCoder": DeepSeekCoder_ELRM,
    # }
    # codeBLEU={
    #     # "curosr":cursor_score,
    #     # "copilot":copilot_score,
    #     # "codeGeeX": codeGeeX_score,
    #     # "DeepSeekCoder": DeepSeekCoder_score,
    # }

    dump_dict(score, "data/score/DeepSeekCoder_CodeBLEU.json")
    # CodeBLEU_dump_dict(codeBLEU)
        # Perform operations on df for each sheet
    return

iterate_ref_hypo()