import string
import pandas as pd
import math
import time
from codebleu import calc_codebleu

py_operators=['+','-','*','/','//','%','>','<','=']


def get_diff_lists(list1,list2):
    difference_result = []
    for item in list1:
        if item not in list2:
            difference_result.append(item)
    return difference_result

#####################################For punctuation category #########################################################

def get_sum_weights_pun(ans_list, gen_list,lambda_p,n_gram):
    avg_len_ans = get_avg_length_ngram(ans_list,n_gram)
    avg_len_gen = get_avg_length_ngram(gen_list,n_gram)
    TP_weights = []
    FP_weights = []
    FN_weights = []


    for v1 in gen_list:
        if v1 in ans_list:  # TP
            weight=1
            TP_weights.append(weight)
            # print("TP")

        else:  # FP
            # print("FP")
            weight=1
            FP_weights.append(weight)

    for v2 in ans_list:
        if v2 not in gen_list:  # FN
            weight=1
            FN_weights.append(weight)

    sum_TP_weights = 0.4 * sum(TP_weights)
    sum_FP_weights = 0.77 * sum(FP_weights)
    sum_FN_weights = 0.7 * sum(FN_weights)
    # print("sum_FN_weights")
    # print(sum_FN_weights)
    return sum_TP_weights, sum_FP_weights, sum_FN_weights

def get_precision_pun(ans_list, gen_list,lambda_p,n_gram):
    sum_TP_weights, sum_FP_weights, sum_FN_weights = get_sum_weights_pun(ans_list, gen_list,lambda_p,n_gram)
    # print("print(sum_TP_weights)")
    # print(sum_TP_weights)
    # print(sum_FP_weights)
    precision = sum_TP_weights / (sum_TP_weights + sum_FP_weights + 1e-10)  # avoid division by zero
    return precision

def get_recall_pun(ans_list, gen_list,lambda_p,n_gram):
    sum_TP_weights, sum_FP_weights, sum_FN_weights = get_sum_weights_pun(ans_list, gen_list,lambda_p,n_gram)
    recall = sum_TP_weights / (sum_TP_weights + sum_FN_weights + 1e-10)  # avoid division by zero
    return recall

###########################################For Lexicon category ####################################################
def get_weight(alpha, avg_ans_len, gen_word_len):
    numerator = alpha
    length = abs(avg_ans_len - gen_word_len)
    # length = avg_ans_len - gen_word_len
    denominator = 1 + abs(alpha - 1) * (math.exp(length))
    weight = numerator / denominator
    # print("weights")
    # print(weight)
    return weight

def get_weight_FP(alpha, avg_ans_len, gen_word_len):
    numerator = alpha
    length = gen_word_len-avg_ans_len
    denominator = 1 + abs(alpha - 1) * (math.exp(length))
    weight = numerator / denominator
    # print("weights")
    # print(weight)
    return weight


def get_avg_length_ngram(list,n_gram):
    # print("---get_avg_length---list---")
    # print(list)
    avg_length=0
    if n_gram==1:
        num = len(list)
        total_length = 0
        for l in list:
            total_length += len(l)
        avg_length = total_length / (num++1e-10)
    else:
        print("---->1")
        length = []
        for l in list:
            one_str = ''.join(l)
            length.append(len(one_str))
        avg_length = sum(length) / (len(list)++1e-10)

    print(avg_length)
    return avg_length

# get_avg_length_ngram([["a","abc"],["def","aaaaaaa"],["cccccccccccc","111111"]],1)
# get_avg_length_ngram([["a","abc"],["def","aaaaaaa"],["cccccccccccc","111111"]],2)
# get_avg_length_ngram([["a","abc","def"],["aaaaaaa","cccccccccccc","111111"]],3)

def get_len_list(g):
    length=0
    if isinstance(g,list):
        print("get_len_list",g)
        for l in g:
            length=length+len(l)
    else:
        length=len(g)

    return length

def get_sum_weights(ans_list, gen_list,alpha,n_gram):
    # ans_list = ans_dict.values()
    # gen_list = gen_dict.values()
    print("get_sum_weights_gen_list",gen_list)
    print("get_sum_weights_ans_list",ans_list)
    avg_len_ans = get_avg_length_ngram(ans_list,n_gram)
    avg_len_gen = get_avg_length_ngram(gen_list,n_gram)

    # we ignore the influence of index because the form can be access chain
    TP_weights = []
    FP_weights = []
    FN_weights = []
    for g in gen_list:
        len_g = get_len_list(g)
        print("len_G",len_g)
        if g in ans_list:  # TP
            # print("TP")
            weight = get_weight(7, avg_len_gen, len_g)
            TP_weights.append(weight)
        else:  # FP
            # print("FP")
            weight = get_weight(2, avg_len_gen, len_g)
            FP_weights.append(weight)

    for a in ans_list:
        len_a = len(a)
        if a not in gen_list:  # FN
            # print("FN")
            weight = get_weight(2, avg_len_gen, len_a)
            FN_weights.append(weight)

    sum_TP_weights = sum(TP_weights)
    sum_FP_weights = sum(FP_weights)
    sum_FN_weights = sum(FN_weights)
    # print("sum_FN_weights")
    # print(sum_FN_weights)

    return sum_TP_weights, sum_FP_weights, sum_FN_weights

def get_precision(ans_list, gen_list,alpha,n_gram):
    sum_TP_weights, sum_FP_weights, sum_FN_weights = get_sum_weights(ans_list, gen_list,alpha,n_gram)
    # print("print(sum_TP_weights)")
    # print(sum_TP_weights)
    # print(sum_FP_weights)
    precision = sum_TP_weights / (sum_TP_weights + sum_FP_weights + 1e-10)  # avoid division by zero
    return precision


def get_recall(ans_list, gen_list,alpha,n_gram):
    sum_TP_weights, sum_FP_weights, sum_FN_weights = get_sum_weights(ans_list, gen_list,alpha,n_gram)
    recall = sum_TP_weights / (sum_TP_weights + sum_FN_weights + 1e-10)  # avoid division by zero
    return recall


def get_f_beta(beta,precision,recall):
    f_beta = ((1 + beta ** 2) * precision * recall) / (
                (beta ** 2) * precision + recall + 1e-10)  # avoid division by zero
    return f_beta


def accuracy():
    return
###################################################Iterators##################################################
def find_same_n_gram(list):
    list1=list[0:3]
    same_num=0
    for l in list:
        if l in list1:
            same_num=same_num+1
    return same_num

def get_n_gram_lists(n,elems):
    pairs=None
    if n>=len(elems):
        pairs=[elems]
    else:
        pairs = [elems[i:i+n] for i in range(len(elems) - n)]
    print("get_n_gram_list",pairs)
    return pairs


def to_ordered_list(statement):
    statement=str(statement)
    statement=statement.replace('\n', '').split(" ")
    statement_list=[]
    # print(statement)
    for i in statement:
        i=str(i)
        for j in i:
            if j in string.punctuation:
                i=i.replace(j, "*" + j + "*")
        ele = i.split("*")
        ele = [i for i in ele if i != '']
        statement_list.extend(ele)

    punc=[]
    lexicon=[]
    operators=[]
    number=[]
    for p in statement_list:
        if p in py_operators and p in string.punctuation:
            operators.extend(p)
        elif p in string.punctuation:
            punc.extend(p)
        elif p.isnumeric():
            number.extend(p)
        else:
            lexicon.append(p)

    return statement_list,lexicon,punc,number,operators

def to_dict(statement):
    statement = str(statement)
    statement = statement.replace('\n', '').split(" ")
    statement_list = []
    # print(statement)
    for i in statement:
        i = str(i)
        for j in i:
            if j in string.punctuation:
                i = i.replace(j, "*" + j + "*")
        ele = i.split("*")
        ele = [i for i in ele if i != '']
        statement_list.extend(ele)

    punc = {}
    lexicon = {}
    operators = {}
    number = {}
    statement_dict={}
    index=0
    for p in statement_list:
        statement_dict[index]=p
        if p in py_operators and p in string.punctuation:
            operators[index]=p
        elif p in string.punctuation:
            punc[index]=p
        elif p.isnumeric():
            number[index]=p
        else:
            lexicon[index]=p
        index=index+1

    # print(statement_list)
    # print(statement_dict)

    return statement_dict, lexicon, punc, number, operators


def convert_to_for_compare(patch, gene):
    patch=str(patch)
    gene=str(gene)
    patch_List=patch.split('\n')
    gene_list=gene.split('\n')
    if str(patch)[0]=="#":
        patch_List=patch_List[1:]

    len_p=len(patch_List)
    len_g=len(gene_list)


    if len_p-len_g>0:
        patch_List=patch_List[:len_g]

    if len_p-len_g<0:
        gene_list=gene_list[:len_p]

    patch_str= ' '.join([str(elem) for elem in patch_List])

    gen_str=' '.join([str(elem) for elem in gene_list])
    print(patch_List)
    print(gene_list)
    print(patch_str)
    print(gen_str)
    return patch_str,gen_str


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
    from groue import Rouge
    ans_str=" ".join(ans_list)
    pred_str=" ".join(pred_list)
    rouge = Rouge()
    scores = rouge.get_scores(pred_str,ans_str,avg=True)
    return scores


def get_CodeBLEU(ans_list,pred_list):
    # pip install codebleu==0.1.2
    # pip install codebleu
    result = calc_codebleu(ans_list, pred_list, lang="python", weights=(0.25, 0.25, 0.25, 0.25), tokenizer=None)
    print(result)
    return result
# get_CodeBLEU(["a","b","c","d"],["a","bb","c","dd"])
# def get_ELEM(a_punc,g_punc,a_lexicon,g_lexicon):

def get_lex_punc_num_op_list(statement_list):
    punc = []
    lexicon = []
    operators = []
    number = []
    for p in statement_list:
        if p in py_operators and p in string.punctuation:
            operators.extend(p)
        elif p in string.punctuation:
            punc.extend(p)
        elif p.isnumeric():
            number.extend(p)
        else:
            lexicon.append(p)
    return lexicon,punc,number,operators

# def get_ELEM_n_gram(a_statement_list,g_statement_list,n_gram):
def get_ELEM(a_punc,g_punc,a_lexicon,g_lexicon,n_gram):
    g_n_gram_lexicon = get_n_gram_lists(n_gram, g_lexicon)
    g_n_gram_punc = get_n_gram_lists(n_gram, g_punc)

    a_n_gram_lexicon = get_n_gram_lists(n_gram, a_lexicon)
    a_n_gram_punc = get_n_gram_lists(n_gram, a_punc)
    # a_lexicon, a_punc, a_number, a_operators=get_lex_punc_num_op_list(a_statement_list)
    # g_lexicon, g_punc, g_number, g_operators=get_lex_punc_num_op_list(g_statement_list)


    alpha=3
    beta=1
    # beta=0.5
    lambda_p=0.1
    print(a_punc)
    print(g_punc)
    # for lexical category
    # gen_precision=get_precision(a_lexicon, g_lexicon,alpha,n_gram)
    # gen_recall=get_recall(a_lexicon, g_lexicon,alpha,n_gram)
    gen_precision = get_precision(a_n_gram_lexicon, g_n_gram_lexicon, alpha, n_gram)
    gen_recall=get_recall(a_n_gram_lexicon, g_n_gram_lexicon,alpha,n_gram)
    f_beta=get_f_beta(beta,gen_precision,gen_recall)
    print("precision,recall,f_0.5")
    print(gen_precision)
    print(gen_recall)
    print(f_beta)

    if len(g_punc)!=0 and len(a_punc)!=0:
        # for punctuation category
        p_gen_precision = get_precision_pun(a_punc, g_punc,lambda_p,n_gram)
        p_gen_recall = get_recall_pun(a_punc, g_punc, lambda_p,n_gram)
        p_f_beta = get_f_beta(beta, p_gen_precision, p_gen_recall)
        average_precision = (p_gen_precision + gen_precision) / 2
        average_recall = (p_gen_recall + gen_recall) / 2
        average_f_beta = get_f_beta(beta, average_precision, average_recall)
        print("average")
        print(average_f_beta)
    else:
        average_f_beta=f_beta
    # print("p_gen_precision")
    # print(p_gen_precision)
    # print(p_gen_recall)
    # print(p_f_beta)
    return average_f_beta

no_trans_note_work=[57,91,100,101,102,103,104,105,112,113,125,142,145,146,
147,148,155,161,182,187,192,193,199,201,204,205,207,209,
211,212,215,218,219,224,225,232,247,267,268]

trans_work=['266', '269', '271', '272', '273', '274', '275', '278', '279', '283',
            '284', '293', '10', '11', '16', '17', '21', '22', '23', '24', '25', '29',
            '2', '30', '32', '33', '35', '39', '3', '42', '43', '44', '46', '47', '48',
            '4', '50', '56', '58', '59', '60', '61', '62', '63', '7', '8', '9', '64', '65',
            '66', '68', '69', '76', '80', '81', '82', '83', '84', '85', '86', '87', '88', '92',
            '93', '94', '95', '101', '106', '107', '108', '109', '110', '113', '96', '97', '98',
            '116', '118', '119', '121', '122', '127', '129', '130', '131', '133', '134', '137', '138',
            '139', '153', '154', '168', '169', '175', '208', '210', '213', '223', '227', '234', '235', '236',
            '237', '238', '242', '244', '245', '246', '250', '251', '252', '253', '259']


def save_dict(d,name):
    print(name)
    with open('{}.json'.format(name), 'w') as fp:
        json.dump(d, fp)
    return


def collect_fixed_unfixed():
    generated_code = pd.ExcelFile("D:/000_PHD_project/analyzer/Dataset/code_no_trans.xlsx")
    # generated_code_after_trans=pd.ExcelFile("D:/000_PHD_project/analyzer/Dataset/code_trans.xlsx")
    gen_code_sheetnames =  generated_code.sheet_names
    # after_trans_sheetnames=generated_code_after_trans.sheet_names
    # print(gen_code_sheetnames)
    # print(after_trans_sheetnames)
    models=["Copilot","CodeGeex","codeLLAMA_7b","Starcoder2_7b"]
    n_gram=2

    c2_fixed_BLEU={}
    c2_fixed_GLEU={}
    c2_fixed_ROUGE={}
    c2_fixed_CODEBLUE = {}
    c2_fixed_ELEM={}

    c2_unfixed_BLEU={}
    c2_unfixed_GLEU={}
    c2_unfixed_ROUGE={}
    c2_unfixed_CODEBLUE = {}
    c2_unfixed_ELEM={}
    # sheetname_pyname:value

    for sheet in gen_code_sheetnames:
    # for sheet in after_trans_sheetnames:
        print(sheet)
        df = pd.read_excel(generated_code, sheet_name=sheet)
        # df = pd.read_excel(generated_code_after_trans, sheet_name=sheet)

        for index in df.index:
            py_name=df['Prompt_Name'].loc[index]
            id=str(py_name).split("_")[1]
            print(id)
            if id not in no_trans_note_work:
                answer=df['answer'].loc[index]
                # c2_g = df['Copilot'].loc[index]
                # c2_g = df['CodeGeex'].loc[index]
                # c2_g = df['codeLLAMA_7b'].loc[index]
                c2_g = df['Starcoder2_7b'].loc[index]
                # c2 = df['C1'].loc[index]
                # c2= df['C2'].loc[index]
                # c2 = df['C3'].loc[index]
                c2= df['S2'].loc[index]
                # ans,gene=convert_to_for_compare(answer, c1_g)

                g_statement_list, g_lexicon, g_punc, g_number, g_operators = to_ordered_list(c2_g)
                a_statement_list, a_lexicon, a_punc, a_number, a_operators = to_ordered_list(answer)
                print("gggggggg_punc,g_punc,a_lexicon,g_lexicon,n_gram","".join(a_statement_list))
                print("aaaaaaaaa_punc,g_punc,a_lexicon,g_lexicon,n_gram", a_statement_list)

                key=sheet+'__'+py_name

                if len(str(c2_g))>2 and str(c2_g)!='nan' and len(g_lexicon)!=0:
                    if c2>0:
                        print(c2_g)
                        # print("ccccccc1111111"+str(len(a_lexicon)))
                        # print(id)
                        # print(len(g_lexicon))
                        BLEU= get_BLEU( a_statement_list,g_statement_list)
                        GLEU= get_GLEU( a_statement_list,g_statement_list)
                        ROUGE= get_ROUGE(a_statement_list,g_statement_list)
                        code_bleu = get_CodeBLEU(["".join(a_statement_list)],["".join(g_statement_list)])
                        ELEM= get_ELEM(a_punc,g_punc,a_lexicon,g_lexicon,n_gram)

                        # ELEM=get_ELEM(a_statement_list,g_statement_list)
                        # print("BLEU",BLEU)
                        # print("GLEU",GLEU)
                        # print("ROUGE",ROUGE)
                        # print("code_bleu",code_bleu['codebleu'])
                        # print("ELEM",ELEM)
                        c2_fixed_BLEU[key]=BLEU
                        c2_fixed_GLEU[key]=GLEU
                        c2_fixed_ROUGE[key]=ROUGE['rouge-2']['f']
                        c2_fixed_ELEM[key]=ELEM
                        c2_fixed_CODEBLUE[key]=code_bleu['codebleu']

                    if c2==0:
                        print(c2_g)
                        BLEU2 = get_BLEU( a_statement_list,g_statement_list)
                        GLEU2 =  get_GLEU( a_statement_list,g_statement_list)
                        # print(g_lexicon)
                        ROUGE2 = get_ROUGE( a_statement_list,g_statement_list)
                        code_bleu2 = get_CodeBLEU(["".join(a_statement_list)],["".join(g_statement_list)])
                        ELEM2 = get_ELEM(a_punc,g_punc,a_lexicon,g_lexicon,n_gram)
                        c2_unfixed_BLEU[key] = BLEU2
                        c2_unfixed_GLEU[key] = GLEU2
                        c2_unfixed_ROUGE[key] = ROUGE2['rouge-2']['f']
                        c2_unfixed_ELEM[key] = ELEM2
                        c2_unfixed_CODEBLUE[key] = code_bleu2['codebleu']
                        # print("BLEU2",BLEU2)
                        # print("GLEU2",GLEU2)
                        # print("ROUGE2",ROUGE2)
                        # print("code_bleu2['codebleu']",code_bleu2['codebleu'])
                        # print("ELEM2",ELEM2)


    # print(len((list(c1_fixed_BLEU.keys()))))#98     #52          #43     #69
    # print(sum(list(c1_fixed_BLEU.values())))#67.27  #32.01     #26.01  #46.97
    # print(sum(list(c1_fixed_GLEU.values())))#66.69  #32.17     #25.73  #46.49
    # print(sum(list(c1_fixed_ROUGE.values())))#73.07 #36.83   #29.44    #50.71
    # print(sum(list(c1_fixed_CodeBleu.values())))#41.17  #19.94   #16.8   #28.85
    # print(sum(list(c1_fixed_ELEM.values())))#81.875 #40.99     #34.60   #56.51
    # 2222222222print(sum(list(c1_fixed_ELEM.values())))#88.397 #44.30     #36.25   #57.79

    # print(len((list(c1_unfixed_BLEU.keys()))))#408  #457       #463     409
    # print(sum(list(c1_unfixed_BLEU.values())))#91.82 #104.85   #112.52  #87.33
    # print(sum(list(c1_unfixed_GLEU.values())))#86.78 #96.44   #97.118   #84.58
    # print(sum(list(c1_unfixed_ROUGE.values())))#105.81 #112.53   #123.05  #104.19
    # print(sum(list(c1_unfixed_CodeBLEU.values()))) #113.65  #120.41   # 126.70  #113.06
    # print(sum(list(c1_unfixed_ELEM.values())))#211.85 #202.59   #241.45   #180.50
    #222222222 print(sum(list(c1_unfixed_ELEM.values())))#219.91 #206.97   #223.19   #187.83



    # print(len((list(c2_fixed_BLEU.keys())))) #100   #62       #41          # 59
    # print(sum(list(c2_fixed_BLEU.values()))) #72.27   #39.19   #27.997     # 36.30
    # print(sum(list(c2_fixed_GLEU.values()))) #71.14   #38.48   #26.52     # 34.97
    # print(sum(list(c2_fixed_ROUGE.values()))) #77.07  #42.50   #29.00     # 39.28
    # print(sum(list(c2_fixed_CODEBLUE.values())))  #
    # print(sum(list(c2_fixed_ELEM.values()))) #85.07   #48.08   #32.72     #46.49
    # 22print(sum(list(c2_fixed_ELEM.values()))) #85.07   #48.08   #32.72     #46.49


    # print(len((list(c2_unfixed_BLEU.keys())))) #574    #545     #467    # 554
    # print(sum(list(c2_unfixed_BLEU.values()))) #174.24  #146.59  #113.22  # 128.00
    # print(sum(list(c2_unfixed_GLEU.values()))) #165.23  #132.21  #105.50  # 121.27
    # print(sum(list(c2_unfixed_ROUGE.values()))) #202.48  #154.39  #121.19  # 146.64
    # print(sum(list(c2_unfixed_CODEBLUE.values())))  #
    # print(sum(list(c2_unfixed_ELEM.values()))) #331.330  #273.53  213.73   # 257.16
    # 22print(sum(list(c2_unfixed_ELEM.values()))) #  #     #


    print(len((list(c2_fixed_BLEU.keys()))))#
    print(sum(list(c2_fixed_BLEU.values())))#
    print(sum(list(c2_fixed_GLEU.values())))#
    print(sum(list(c2_fixed_ROUGE.values())))#
    print(sum(list(c2_fixed_CODEBLUE.values())))  #
    print(sum(list(c2_fixed_ELEM.values())))#


    print(len((list(c2_unfixed_BLEU.keys()))))#
    print(sum(list(c2_unfixed_BLEU.values())))#
    print(sum(list(c2_unfixed_GLEU.values())))#
    print(sum(list(c2_unfixed_ROUGE.values())))#
    print(sum(list(c2_unfixed_CODEBLUE.values())))  #
    print(sum(list(c2_unfixed_ELEM.values())))#

    # save_dict()

    return
collect_fixed_unfixed()

