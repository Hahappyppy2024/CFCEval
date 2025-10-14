from codebleu import calc_codebleu
from CFCEval4AIWARE.metric.ELRM import calculate_ELRM

prediction = "def add ( a , b ) :\n return a + b"
reference = "def sum ( first , second ) :\n return second + first"




ref1="paths = [ipython_dir]"
gen1="paths = [ipython_dir, get_ipython_package_dir()]"
codebleu_1 = calc_codebleu([ref1], [gen1], lang="python", weights=(0.25, 0.25, 0.25, 0.25), tokenizer=None)
ELRM_1 = calculate_ELRM([ref1], [gen1], language="python", weights=(0.10, 0.05, 0.80, 0.05))
ELRM_15 = calculate_ELRM([ref1], [gen1], language="python", weights=(0.25, 0.25, 0.25, 0.25))
print(codebleu_1)
print(ELRM_1)
print(ELRM_15)
print("-----------------")

# ref2="if action == \"add\" and form.is_submitted():"
# gen2="if action == 'add' and form.is_submitted():"
# codebleu_2 = calc_codebleu([ref2], [gen2], lang="python", weights=(0.25, 0.25, 0.25, 0.25), tokenizer=None)
# ELRM_2 = calculate_ELRM([ref2], [gen2], language="python", weights=(0.10, 0.05, 0.80, 0.05))
# ELRM_25 = calculate_ELRM([ref2], [gen2], language="python", weights=(0.25, 0.25, 0.25, 0.25))
# print(codebleu_2)
# print(ELRM_2)
# print(ELRM_25)
# print("-----------------")


# ref3=""
# gen3=""
# codebleu_3 = calc_codebleu([ref3], [gen3], lang="python", weights=(0.25, 0.25, 0.25, 0.25), tokenizer=None)
# ELRM_3 = calculate_ELRM([ref3], [gen3], language="python", weights=(0.25, 0.25, 0.25, 0.25))
# print(codebleu_3)
# print(ELRM_3)
# print("-----------------")
#
#
# ref4=""
# gen4=""
# codebleu_4 = calc_codebleu([ref4], [gen4], lang="python", weights=(0.25, 0.25, 0.25, 0.25), tokenizer=None)
# ELRM_4 = calculate_ELRM([ref4], [gen4], language="python", weights=(0.25, 0.25, 0.25, 0.25))
# print(codebleu_1)
# print(ELRM_1)
# print("-----------------")