import pandas as pd
import string

dir="D:/000_PHD_project/analyzer/Dataset/benchmark.csv"
py_operators=['+','-','*','/','//','%','>','<','=']

def ele_punc_categorie(patch):
    patch=str(patch)
    patch=patch.replace('\n', '').split(" ")
    patch_list=[]
    for i in patch:
        i=str(i)
        ele=[]
        ele = []
        for j in i:
            if j in string.punctuation:
                i = i.replace(j, "*" + j + "*")
        # print(i)
        ele = i.split("*")
        ele = [i for i in ele if i != '']
        # print(ele)
        patch_list.extend(ele)

    punc=[]
    lexicon=[]
    operators=[]
    number=[]
    for p in patch_list:
        if p in py_operators and p in string.punctuation:
            operators.extend(p)
        elif p in string.punctuation:
            punc.extend(p)
        elif p.isnumeric():
            number.extend(p)
        else:
            lexicon.append(p)

    # print(punc)
    # print(lexicon)
    # print(number)
    # print(operators)
    # print(patch_list)
    # print(len(patch_list))
    # print(len(punc))
    # print(len(lexicon))
    # print(len(operators))

    return patch_list,lexicon,punc,number,operators



def get_diff_lists(list1,list2):
    difference_result = []
    for item in list1:
        if item not in list2:
            difference_result.append(item)
    return difference_result

def CoF():
    import time
    df=pd.read_csv(dir)
    all_cof=[]
    all_cop=[]
    for index in df.index:
        cof=0
        cop=0
        patch_a=df['patch+'].loc[index]
        patch_d=df['patch-'].loc[index]

        patch_list_a,lexicon_a,punc_a,number_a,operators_a=ele_punc_categorie(patch_a)
        patch_list_d,lexicon_d,punc_d,number_d,operators_d = ele_punc_categorie(patch_d)
        all_diff=get_diff_lists(patch_list_a,patch_list_d)
        lex_diff=get_diff_lists(lexicon_a,lexicon_d)
        punc_diff=get_diff_lists(punc_a,punc_d)
        len_all=len(all_diff)
        len_lex=len(lex_diff)
        len_punc=len(punc_diff)

        # print(all_diff)
        # print(lex_diff)
        # print(punc_diff)
        # cof=len_lex/len_all
        # cop=len_punc/len_all
        # all_cof.append(cof)
        # all_cop.append(cop)
        if len(all_diff)==0 and len(lex_diff)==0:
            print(lex_diff)
        elif len(all_diff)==0 and len(punc_diff)==0:
            print(punc_diff)
        else:
            cof=len_lex/len_all
            cop=len_punc/len_all
            print("cof")
            print(cof)
            print("cop")
            print(cop)
            all_cof.append(cof)
            all_cop.append(cop)


    avg_cof=sum(all_cof)/len(all_cof)
    avg_cop=sum(all_cop)/len(all_cop)

    print("avg_cof")
    print(avg_cof)
    print("avg_cop")
    print(avg_cop)
    # avg_cof
    # 0.6734814055208364
    # avg_cop
    # 0.25978199340457137
    return cof,cop


CoF()

