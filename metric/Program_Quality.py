from .utils.get_keywords_ops_com_ter import get_keywords_ops_comment

def check_quality_type1(code_line,language):
    '''
    unbalanced bracket and quotes
    Example1: a=abc.import(
    '''
    s = str(code_line)
    pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",  # for C++, Java
        "'": "'",  # single quote
        '"': '"',  # double quote
        "`": "`",  # backtick for JS string
        "/*": "*/",  # for comments in C, Java, JavaScript etc.
        "--[[": "]]",  # for multiple lines of comments in Lua
        "=begin": "=end",  # for multiple lines of Ruby
        "#(": ")#",  # for multiple lines of  Lisp-like comment forms
        "#{": "}",  # for Ruby string
    }
    stack = []
    for c in s:
        if c in "{[(":
            stack.append(c)
        elif stack and c == pairs[stack[-1]]:
            stack.pop()
        else:
            return False
    return len(stack) == 0




def check_quality_type2(code_line,language):
    '''
    starting and ending with punctuations,operators and keywords
    Example1: abc=
    Example2: if a!=b or
    Example3: if a==
    Exampel4: = a+c
    '''
    quality=""
    keywords, ops, comment, terminator=get_keywords_ops_comment(language)
    if code_line.split(' ')[0] in keywords or code_line[0] in ops\
        or code_line[0] in comment:
        quality = "Bad"
    elif terminator!= None and code_line[0] == terminator:
        quality = "Bad"
    if code_line.split(' ')[-1] in keywords or code_line[-1] in ops\
        or code_line[-1] in comment:
        quality = "Bad"

    return quality


def check_quality_type3(code_line,language):
    '''
    no terminators
    Example1: JAVA--> A=
    Example2:
    Example3:
    '''
    quality = ""
    keywords, ops, comment, terminator = get_keywords_ops_comment(language)
    if terminator!= None and code_line!=terminator:
        quality="Bad"
    return quality



def check_quality_type4():
    return