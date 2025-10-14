from collections import Counter
from CFCEval4AIWARE.metric.utils.utils import ngrams
import code

reference_counts=Counter(ngrams([1,2,3,4,5], 2)) if len([1,2,3,4,5]) >= 2 else Counter()
max_counts = {}
# for ngram in reference_counts:
#     print("ngram:"+ str(ngram))
#     max_counts[ngram] = max(max_counts.get(ngram, 0), reference_counts[ngram])
#     print(max_counts.get(ngram, 0))
#     print(reference_counts[ngram])
#     print(max_counts)

# print(max(1, sum(reference_counts.values())))

from codebleu import calc_codebleu
patch_1="auto combined_string>=s1++s2 <<=;\n if a==b: a=a++ elif a==c a=a-- :=work(combined_string.c_str()); \n return False  if else in not in"
generate_0="auto combined_string=s1+ s2;\n work(combined_string.c_str());"
generate1="auto combined = s1 + s2; work(combined.c_str());"
generate2="auto string = s1 + s2; work(string.c_str());"
pred = "def add ( a , b ) :\n return a + b"
ref = "def sum ( first , second ) :\n return second + first"

res = calc_codebleu([patch_1], [generate1], "python")
print(res)

import re
#
#
# def extract_strings_from_code(code_text):
#     """
#     Extract all string literals from the code (including those enclosed in double or single quotes).
#     """
#     pattern = r'(?<!\\)(["\'])(.*?)(?<!\\)\1'
#     matches = re.findall(pattern, code_text)
#     return [match[1] for match in matches]
#
# code = '''
# print("Hello, world!")
# name = "Alice"
# escaped = "He said: \\"Hi!\\""
# message = 'Goodbye'
# '''
#
# print(extract_strings_from_code(code))