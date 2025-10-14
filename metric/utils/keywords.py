import keyword

# https://github.com/e3b0c442/keywords
c44=["const", "continue", "default", "do","double", "else", "enum", "extern",
     "float", "for", "goto" ,"if","inline","int", "long" ,"register","restrict",
     "return", "short", "signed","sizeof", "static", "struct" ,"switch",
     "typedef", "union", "unsigned", "void","volatile", "while", "_Alignas" ,
     "_Alignof","_Atomic" ,"_Bool", "_Complex", "_Generic",
     "_Imaginary", "_Noreturn", "_Static_assert","_Thread_local"]

csharpe107=[ "abstract","as", "base" ,"bool","break", "byte", "case", "catch",
             "char", "checked", "class", "const","continue", "decimal", "default",
             "delegate","do", "double", "else", "enum","event", "explicit",
             "extern", "false","finally", "fixed", "float", "for","foreach","goto",
             "if", "implicit","in", "int", "interface", "internal","is", "lock",
             "long", "namespace","new", "null", "object", "operator","out",
             "override", "params", "private","protected", "public","readonly",
             "ref","return", "sbyte", "sealed", "short","sizeof", "stackalloc",
             "static", "string","struct", "switch", "this", "throw","true",
             "try", "typeof", "uint","ulong", "unchecked", "unsafe", "ushort",
             "using" ,"virtual", "void", "volatile","while", "add", "alias",
             "ascending","async", "await", "by" ,"descending","dynamic", "equals",
             "from", "get","global", "group", 	"into", "join","let" ,"nameof",
             "notnull", "on","orderby", "partial", 	"remove", "select","set",
             "unmanaged", "value","var", "when", "where", "yield" ]


cpp92=["alignas" ,"alignof", "asm", "auto","bool" ,"break",
       "case", "catch","char", "char8_t" ,"char16_t","char32_t",
       "class", "concept", "const", "consteval","constexpr",
       "constinit", "const_cast", "continue","co_await",
       "co_return", "co_yield", "decltype","default", "delete",
       "do", "double","dynamic_cast", "else", "enum", "explicit",
       "export", "extern", "false", "float","for", 	"friend", "goto",
       "if","inline", "int", "long", "mutable","namespace",
       "new", "noexcept", "nullptr","operator", "private",
       "protected", "public","register", "reinterpret_cast",
       "requires", "return","short", "signed", "sizeof", "static",
       "static_assert" ,"static_cast", "struct", "switch","template",
       "this", "thread_local", "throw","true", "try" ,"typedef", "typeid",
       "typename", "union", "unsigned", "using","virtual", "void", "volatile",
       "wchar_t","while", "and", "and_eq", "bitand","bitor", "compl", "not",
       "not_eq","or", "or_eq" ,"xor", "xor_eq"]



Dart33= ["assert","break", "case", "catch",
"class", "const", "continue", "default",
"do", "else", "enum", "extends",
"false", "final", "finally", "for",
"if", "in", "is", "new",
"null", "rethrow", "return", "super"
"switch", "this", "throw", "true",
"try", "var", "void", "while","with"]


Elixir15=["true", "false", "nil" ,"when","and",
          "or", "not","in", "fn", "do", "end",
          "catch","rescue", "after", "else"]
Erlang23=["after","and", "andalso", "band","begin",
          "bnot","bor", "bsl", "bsr", "bxor", "case",
          "catch", "cond", "div", "end", "fun", "if",
          "let", "not", "of", "or","orelse", "receive",
          "rem","try" ,"when", "xor"]

Fortran103=["associate", "asynchronous", "backspace", "bind",
            "block", "block", "data", "call", "case","class",
            "close", "codimension", "common","contains", "contiguous",
            "continue", "critical","cycle","data", "deallocate",
            "deferred","dimension", "do", "do", "concurrent", "elemental",
            "else", "else if","elsewhere","end","endfile", "endif",
            "entry", "enum","enumerator","equivalence","error stop", "exit",
            "extends", "external", "final", "flush","forall", "format",
            "function", "generic","goto", "if" ,"implicit", "import","include",
            "inquire", "intent", "interface","intrinsic", "lock", "module",
            "namelist","non_overridable", "nopass", "nullify", "only",
            "open", "operator", "optional", "parameter","pass", "pause",
            "pointer", "print","private","procedure", "program", "protected",
            "public", "pure", "read", "recursive","result", "return", "rewind",
            "rewrite","save", "select", "sequence", "stop","submodule",
            "subroutine", "sync all","sync images","sync memory" ,"target",
            "then", "unlock","use", "value", "volatile", "wait","where", "while", "write"]

Go25=["break", "case", "chan", "const","continue",
      "default", "defer", "else","fallthrough",
      "for", "func", "go","goto", "if" ,"import",
      "interface","map", "package", "range", "return",
      "select", "struct", "switch", "type","var"]




Java67=["abstract", "assert", "boolean", "break",
        "byte", "case", "catch", "char","class",
        "const", "continue", "default","do","double",
        "else", "enum","extends","final", "finally",
        "float", "for", "if", "goto", "implements","import",
        "instanceof", "int", "interface","long", "native",
        "new", "package","private", "protected", "public",
        "return","short", "static", 	"strictfp", "super",
        "switch", "synchronized", "this", "throw","throws",
        "transient", "try", "void","volatile", "while","_",
        "exports","module", "non-sealed", "open", "opens",
        "permits", "provides", "record", "requires","sealed",
        "to", "transitive", "uses","var", "with", "yield" ]

JS59=["break", "continue", "delete", "else",
      "for", "function", "if", "in",
      "new", "return", "this", "typeof",
      "var", "void", "while", "with",
      "abstract", "boolean", "byte", "case",
      "catch", "char", "class", "const",
      "debugger", "default", "do" ,"double",
      "enum", "export", "extends", "final",
      "finally", "float", "goto", "implements",
      "import", "instanceof", "int", "interface",
      "long", "native", "package", 	"private",
      "protected", "public", "short", "static",
      "super", "switch", "synchronized", "throw",
      "throws", "transient", "try", "volatile",
      "null", "true", "false"]
Kotlin79=[ "as", "as?", "break", "class","continue",
           "do", "else", "false","for", "fun", "if",
           "in","!in", "interface", "is", "!is","null",
           "object", "package", "return","super", "this",
           "throw", "true","try", "typealias", "typeof",
           "val","var", "when", "while", "by","catch",
           "constructor", "delegate", "dynamic","field",
           "file", "finally", "get","import", "init",
           "param", "property","receiver", "set", "setparam",
           "where","actual", "abstract", "annotation",
           "companion","const", "crossinline", "data","enum",
           "expect", "external", "final", "infix","inline",
           "inner", "internal", "lateinit","noinline", "open",
           "operator", "out","override", "private","protected",
           "public","reified", "sealed", "suspend",	"tailrec",
           "vararg", "field", 	"it"]

Lua22=["and", "break", "do", "else","elseif",
       "end","false","for","function", "goto",
       "if","in","local", "nil", "not", "or",
       "repeat", "return", "then", "true",
       "until", "while"]
MATLAB20=["break", "case", "catch", "classdef",
          "continue", "else", "elseif", "end",
          "for", "function", "global", 	"if",
          "otherwise","parfor", "persistent",
          "return","spmd", "switch", "try", "while"]
ObjectiveC85=["asm", "auto","break","case","char","const",
         "continue","default","do","double" ,"else" ,"enum",
         "extern","float","for" ,"goto","if" ,"inline" ,"int",
         "long""register","restrict","return" ,"short","signed",
         "sizeof","static","struct","switch","typedef","union",
         "unsigned","void","volatile","while" ,"_Bool", "_Complex",
         "__block","Imaginary","id","Class","SEL","IMP","BOOL","nil",
         "Nil","YES","NO","self""super","_cmd","__strong","__weak",
         "__autoreleasing","__unsafe_unretained","oneway","In","out",
         "inout","bycopy","byref", "@autoreleasepool", "@interface",
         "@implementation","@protocol" ,"@end" ,"@private", "@protected",
         "@public","@package", "@try", "@throw","@catch()", "@finally",
         "@property", "@synthesize","@dynamic", "@class", "@selector()",
         "@protocol()","@required","@optional" ,"@encode",
         "@\"string\"","@synchronized()",]
PHP69=["__halt_compiler()" ,"abstract" ,"and" ,	"array()","as",
       "break","callable" ,"case","catch" ,"class" ,"clone" ,
       "const","continue", "declare" ,"default" ,"die()","do",
       "echo" ,	"else" ,"elseif","empty()" ,"enddeclare",
       "endfor" ,"endforeach","endif" ,	"endswitch" ,"endwhile",
       "eval()","exit()" ,"extends" ,"final" ,"finally","fn" ,
       "for","foreach","function","global" ,"goto" ,"if ",
       "implements","include","include_once","instanceof" ,"insteadof",
       "interface","isset()","list()","namespace","new",
       "or" ,"print" ,"private","protected" ,"public", "require" ,
       "require_once","return" ,"static" ,"switch" ,"throw","trait" ,
       "try" ,"unset()", "use","var" ,"while" ,"xor" ,"yield","yield from",]

python35=keyword.kwlist
Python38=["False",	"None", "True","and",
          "as","assert","async","await",
          "break","class","continue" ,
          "def","del","elif",	"else","except",
          "finally","for",	"from",	"global",
          "if","import", "in","is",
          "lambda", "nonlocal", "not", "or",
          "pass",	"raise",	"return",	"try",
          "while",	"with",	"yield",	"match",
          "case","_",]

R21=["..." ,"..1" ,	"FALSE" ,"Inf","NA" ,
     "NA_character_" ,"NA_complex_" ,"NA_integer_",
     "NA_real_" ,"NaN" ,"NULL",	"TRUE","break" ,
     "else" ,"for" ,"function","if" ,"in" ,
     "next", "repeat","while "]

Ruby41=["ENCODING", "LINE","FILE","BEGIN","END","alias",
        "and","begin","break",	"case","class",	"def",
        "defined?",	"do","else","elsif","end", "ensure",
        "false","for","if",	"in","module","next","nil",
        "not",	"or","redo","rescue","retry","return",
        "self","super",	"then",	"true",	"undef","unless",
        "until","when",	"while","yield",]

Rust53=["as" ,"break" ,"const" ,"continue","crate",	"else" ,
        "enum" 	,"extern","false" ,	"fn",	"for" ,	"if",
        "impl" ,"in" ,	"let" ,	"loop","match" ,"mod" ,
        "move" 	,"mut","pub" ,	"ref" ,	"return", "self",
        "Self",	"static" ,"struct" ,"super","trait" ,
        "true" ,"type", "unsafe","use" ,"where", "while" ,
        "async","await" ,"dyn","abstract","become","box" ,
        "do" ,"final" ,	"macro","override","priv", "typeof" ,"unsized",
        "virtual","yield" ,"try" ,"union","static"]

Scala40=["abstract" ,"case" ,"catch" ,"class","def" ,
         "do" ,	"else",	"extends","false" ,	"final" ,
         "finally" ,"for","forSome" ,"if" ,	"implicit",
         "import","lazy" ,"macro" ,	"match", "new","null",
         "object" ,	"override", "package","private", "protected",
         "return" ,"sealed","super", "this" ,"throw" ,"trait",
         "try" ,"true ","type", "val","var" ,"while" ,
         "with" ,"yield",]

Swift97=["associatedtype","class","deinit","enum",
         "extension",	"fileprivate","func",	"import",
         "init","inout" ,"internal" ,"let","open",
         "operator","private", "protocol","public" ,
         "rethrows", "static" ,	"struct","subscript" ,
         "typealias","var","break","case","continue","default" ,
         "defer","do",	"else" ,"fallthrough" ,"for",
         "guard","if","in", "repeat","return",
         "switch","where" ,"while","as", "Any","catch",
         "false","is",	"nil","super", "self","Self","throw",
         "throws","true","try","_","#available","#colorLiteral",
         "#column" ,"#else" ,"#elseif","#endif",
         "#error",	"#file","#filePath","#fileLiteral",
         "#function","#if","#imageLiteral","#line",
         "#selector" ,"#sourceLocation" ,"#warning","associativity",
         "convenience","dynamic","didSet","final",
         "get","infix",	"indirect","lazy","left",
         "mutating","none",	"nonmutating","optional",
         "override","postfix",	"precedence","prefix",
         "Protocol","required","right","set",
         "Type","unowned","weak","willSet"]
# VB217=
