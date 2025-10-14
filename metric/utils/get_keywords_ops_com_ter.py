from CFCEval4AIWARE.metric.utils.keywords import c44,csharpe107,cpp92,Dart33,Elixir15,Erlang23,Fortran103,Go25,Java67
from CFCEval4AIWARE.metric.utils.keywords import JS59,Kotlin79,Lua22, MATLAB20,ObjectiveC85,PHP69,Python38,R21,Ruby41
from CFCEval4AIWARE.metric.utils.keywords import Rust53, Scala40, Swift97
from CFCEval4AIWARE.metric.utils.operators import c44_ops,csharpe107_ops,cpp92_ops,Dart33_ops,Elixir15_ops,Erlang23_ops
from CFCEval4AIWARE.metric.utils.operators import Fortran103_ops,Go25_ops, Java67_ops,JS59_ops,Kotlin79_ops,Lua22_ops
from CFCEval4AIWARE.metric.utils.operators import MATLAB20_ops,ObjectiveC85_ops,PHP69_ops,Python38_ops,R21_ops,Ruby41_ops
from CFCEval4AIWARE.metric.utils.operators import Rust53_ops,Scala40_ops, Swift97_ops, py_ops
from CFCEval4AIWARE.metric.utils.comment import language_comment_syntax
from CFCEval4AIWARE.metric.utils.terminator import language_statement_terminator


def get_keywords_ops_comment(language):
    language=language.lower()
    keywords=[]
    ops=[]
    comment=""
    terminator=""
    if language == "c":
        keywords =c44
        ops=c44_ops
        comment=language_comment_syntax['c44']['line']
        terminator=language_statement_terminator['c44']
    elif language == "csharp":
        keywords =csharpe107
        ops=csharpe107_ops
        comment = language_comment_syntax['csharpe107']['line']
        terminator = language_statement_terminator['csharpe107']
    elif language =="cpp":
        keywords=cpp92
        ops =cpp92_ops
        comment = language_comment_syntax['cpp92']['line']
        terminator = language_statement_terminator['cpp92']
    elif language == "dart":
        keywords =Dart33
        ops =Dart33_ops
        comment = language_comment_syntax['Dart33']['line']
        terminator = language_statement_terminator['Dart33']
    elif language == "elixir":
        keywords =Elixir15
        ops =Elixir15_ops
        comment = language_comment_syntax['Elixir15']['line']
        terminator = language_statement_terminator['Elixir15']
    elif language == "erlang":
        keywords =Erlang23
        ops =Erlang23_ops
        comment = language_comment_syntax['Erlang23']['line']
        terminator = language_statement_terminator['Erlang23']
    elif language == "fortran":
        keywords = Fortran103
        ops = Fortran103_ops
        comment = language_comment_syntax['Fortran103']['line']
        terminator = language_statement_terminator['Fortran103']
    elif language == "go":
        keywords = Go25
        ops = Go25_ops
        comment = language_comment_syntax['Go25']['line']
        terminator = language_statement_terminator['Go25']
    elif language == "java":
        keywords = Java67
        ops = Java67_ops
        comment = language_comment_syntax['Java67']['line']
        terminator = language_statement_terminator['Java67']
    elif language == "js":
        keywords = JS59
        ops = JS59_ops
        comment = language_comment_syntax['JS59']['line']
        terminator = language_statement_terminator['JS59']
    elif language == "kotlin":
        keywords = Kotlin79
        ops = Kotlin79_ops
        comment = language_comment_syntax['Kotlin79']['line']
        terminator = language_statement_terminator['Kotlin79']
    elif language == "lua":
        keywords = Lua22
        ops = Lua22_ops
        comment = language_comment_syntax['Lua22']['line']
        terminator = language_statement_terminator['Lua22']
    elif language == "matlab":
        keywords = MATLAB20
        ops = MATLAB20_ops
        comment = language_comment_syntax['MATLAB20']['line']
        terminator = language_statement_terminator['MATLAB20']
    elif language == "objectivec":
        keywords = ObjectiveC85
        ops =ObjectiveC85_ops
        comment = language_comment_syntax['ObjectiveC85']['line']
        terminator = language_statement_terminator['ObjectiveC85']
    elif language == "php":
        keywords = PHP69
        ops = PHP69_ops
        comment = language_comment_syntax['PHP69']['line']
        terminator = language_statement_terminator['PHP69']
    elif language == "python":
        keywords = Python38
        ops = Python38_ops
        comment = language_comment_syntax['Python38']['line']
        terminator = language_statement_terminator['Python38']
    elif language == "r":
        keywords = R21
        ops = R21_ops
        comment = language_comment_syntax['R21']['line']
        terminator = language_statement_terminator['R21']
    elif language == "ruby":
        keywords = Ruby41
        ops = Ruby41_ops
        comment = language_comment_syntax['Ruby41']['line']
        terminator = language_statement_terminator['Ruby41']
    elif language == "rust":
        keywords = Rust53
        ops = Rust53_ops
        comment = language_comment_syntax['Rust53']['line']
        terminator = language_statement_terminator['Rust53']
    elif language == "scala":
        keywords = Scala40
        ops = Scala40_ops
        comment = language_comment_syntax['Scala40']['line']
        terminator = language_statement_terminator['Scala40']
    elif language == "swift":
        keywords = Swift97
        ops = Swift97_ops
        comment = language_comment_syntax['Swift97']['line']
        terminator = language_statement_terminator['Swift97']
    return keywords,ops,comment,terminator




# def get_keywords_ops_comment(language):
#     language=language.lower()
#     keywords=[]
#     ops=[]
#     comment=""
#     terminator=""
#     if language == "c":
#         keywords =c44
#         ops=c44_ops
#         comment=language_comment_syntax['c44']['line']
#         terminator=language_statement_terminator['c44']
#     elif language == "csharp":
#         keywords =csharpe107
#         ops=csharpe107_ops
#         comment = language_comment_syntax['csharpe107']['line']
#         terminator = language_statement_terminator['csharpe107']
#     elif language =="cpp":
#         keywords=cpp92
#         ops =cpp92_ops
#         comment = language_comment_syntax['cpp92']['line']
#         terminator = language_statement_terminator['cpp92']
#     elif language == "dart":
#         keywords =Dart33
#         ops =Dart33_ops
#         comment = language_comment_syntax['Dart33']['line']
#         terminator = language_statement_terminator['Dart33']
#     elif language == "elixir":
#         keywords =Elixir15
#         ops =Elixir15_ops
#         comment = language_comment_syntax['Elixir15']['line']
#         terminator = language_statement_terminator['Elixir15']
#     elif language == "erlang":
#         keywords =Erlang23
#         ops =Erlang23_ops
#         comment = language_comment_syntax['Erlang23']['line']
#         terminator = language_statement_terminator['Erlang23']
#     elif language == "fortran":
#         keywords = Fortran103
#         ops = Fortran103_ops
#         comment = language_comment_syntax['Fortran103']['line']
#         terminator = language_statement_terminator['Fortran103']
#     elif language == "go":
#         keywords = Go25
#         ops = Go25_ops
#         comment = language_comment_syntax['Go25']['line']
#         terminator = language_statement_terminator['Go25']
#     elif language == "java":
#         keywords = Java67
#         ops = Java67_ops
#         comment = language_comment_syntax['Java67']['line']
#         terminator = language_statement_terminator['Java67']
#     elif language == "js":
#         keywords = JS59
#         ops = JS59_ops
#         comment = language_comment_syntax['JS59']['line']
#         terminator = language_statement_terminator['JS59']
#     elif language == "kotlin":
#         keywords = Kotlin79
#         ops = Kotlin79_ops
#         comment = language_comment_syntax['Kotlin79']['line']
#         terminator = language_statement_terminator['Kotlin79']
#     elif language == "lua":
#         keywords = Lua22
#         ops = Lua22_ops
#         comment = language_comment_syntax['Lua22']['line']
#         terminator = language_statement_terminator['Lua22']
#     elif language == "matlab":
#         keywords = MATLAB20
#         ops = MATLAB20_ops
#         comment = language_comment_syntax['MATLAB20']['line']
#         terminator = language_statement_terminator['MATLAB20']
#     elif language == "objectivec":
#         keywords = ObjectiveC85
#         ops =ObjectiveC85_ops
#         comment = language_comment_syntax['ObjectiveC85']['line']
#         terminator = language_statement_terminator['ObjectiveC85']
#     elif language == "php":
#         keywords = PHP69
#         ops = PHP69_ops
#         comment = language_comment_syntax['PHP69']['line']
#         terminator = language_statement_terminator['PHP69']
#     elif language == "python":
#         keywords = python38
#         ops = python38_ops
#         comment = language_comment_syntax['python38']['line']
#         terminator = language_statement_terminator['python38']
#     elif language == "r":
#         keywords = R21
#         ops = R21_ops
#         comment = language_comment_syntax['R21']['line']
#         terminator = language_statement_terminator['R21']
#     elif language == "ruby":
#         keywords = Ruby41
#         ops = Ruby41_ops
#         comment = language_comment_syntax['Ruby41']['line']
#         terminator = language_statement_terminator['Ruby41']
#     elif language == "rust":
#         keywords = Rust53
#         ops = Rust53_ops
#         comment = language_comment_syntax['Rust53']['line']
#         terminator = language_statement_terminator['Rust53']
#     elif language == "scala":
#         keywords = Scala40
#         ops = Scala40_ops
#         comment = language_comment_syntax['Scala40']['line']
#         terminator = language_statement_terminator['Scala40']
#     elif language == "swift":
#         keywords = Swift97
#         ops = Swift97_ops
#         comment = language_comment_syntax['Swift97']['line']
#         terminator = language_statement_terminator['Swift97']
#     return keywords,ops,comment,terminator
