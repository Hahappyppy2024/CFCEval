import keyword

# https://github.com/e3b0c442/keywords
c44_ops = [
    # Arithmetic
    "+", "-", "*", "/", "%",
    # Increment / Decrement
    "++", "--",
    # Relational
    "==", "!=", ">", "<", ">=", "<=",
    # Logical
    "&&", "||", "!",
    # Bitwise
    "&", "|", "^", "~", "<<", ">>",
    # Assignment
    "=", "+=", "-=", "*=", "/=", "%=", "<<=", ">>=", "&=", "^=", "|=",
    # Ternary and comma
    "?", ":", ",",
    # Structure and pointer
    ".", "->", "&", "*",
    # Sizeof, alignment (in C11+)
    "sizeof", "_Alignof"
]

csharpe107_ops = [
    # Arithmetic
    "+", "-", "*", "/", "%", "++", "--",
    # Assignment
    "=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>=",
    # Comparison / Relational
    "==", "!=", ">", "<", ">=", "<=",
    # Logical
    "&&", "||", "!",
    # Bitwise
    "&", "|", "^", "~", "<<", ">>",
    # Conditional / Ternary
    "?", ":",
    # Null-coalescing / Conditional
    "??", "??=", "?.", "?[", "?.[", "=>",
    # Member access / Indexing
    ".", "[]", "()", "->",
    # Type / Casting
    "is", "as", "typeof", "sizeof", "checked", "unchecked", "default",
    # Other
    "new", "delegate", "nameof", "stackalloc", "await", "yield return", "yield break"
]



cpp92_ops = [
    # Arithmetic operators
    "+", "-", "*", "/", "%", "++", "--",
    # Relational operators
    "==", "!=", ">", "<", ">=", "<=",
    # Logical operators
    "&&", "||", "!",
    # Bitwise operators
    "&", "|", "^", "~", "<<", ">>",
    # Assignment operators
    "=", "+=", "-=", "*=", "/=", "%=",
    "<<=", ">>=", "&=", "^=", "|=",
    # Other operators
    "?", ":", ",", "->", ".", ".*", "->*",
    # Scope resolution
    "::",
    # Type and memory management
    "sizeof", "alignof", "typeid", "new", "delete", "new[]", "delete[]",
    "const_cast", "dynamic_cast", "reinterpret_cast", "static_cast",
    # C++20-specific and contextual usage (used like operators)
    "co_await", "co_yield", "co_return",  # coroutine-related
    "requires"  # used in constrained templates
    # Member pointer operators (already included above): .*, ->*
]




Dart33_ops = [
    # Arithmetic operators
    "+", "-", "*", "/", "~/", "%",
    # Increment and decrement
    "++", "--",
    # Equality and relational
    "==", "!=", ">", "<", ">=", "<=",
    # Type test
    "is", "is!", "as",
    # Logical operators
    "!", "&&", "||",
    # Bitwise and shift
    "&", "|", "^", "~", "<<", ">>",
    # Assignment operators
    "=", "+=", "-=", "*=", "/=", "~/=", "%=", "&=", "|=", "^=", "<<=", ">>=",
    # Cascade operator
    "..",
    # Conditional expressions
    "?", ":",
    # Null-aware operators
    "??", "??=",
    # Member access
    ".", "?."  # Null-aware member access (introduced earlier, supported in 2.2)
    # Collection-related (contextual)
    # Note: Dart supports 'collection if', 'collection for' inside [], {} — not traditional operators, so excluded here
]



Elixir15_ops = [
    # Arithmetic
    "+", "-", "*", "/", "div", "rem",
    # Boolean (strict)
    "and", "or", "not",
    # Boolean (non-strict, short-circuit)
    "&&", "||", "!",
    # Comparison
    "==", "!=", "===", "!==", "<", "<=", ">", ">=",
    # Pattern matching
    "=",
    # Pin operator (used in pattern matching)
    "^",
    # Bitwise
    "&&&", "|||", "^^^", "~~~", "<<", ">>",
    # Concatenation / list
    "<>", "++", "--",
    # Capture and anonymous function
    "&", "->",
    # Membership test
    "in",
    # Pipe operator
    "|>",
    # Match operator for exact type/value
    "===",
    # Struct update
    "%{}"
]

Erlang23_ops = [
    # Arithmetic
    "+", "-", "*", "/", "div", "rem",
    # Unary
    "++", "--", "+", "-",
    # Comparison
    "==", "/=", "=<", "<", ">=", ">", "=:= ", "=/=",
    # Boolean logic
    "and", "or", "xor", "not",
    # Short-circuit boolean
    "andalso", "orelse",
    # Bitwise
    "band", "bor", "bxor", "bnot", "bsl", "bsr",
    # Pattern matching
    "=",
    # Tuple or list construction
    "++", "--", "{", "}", "[", "]",
    # Send / Receive
    "!", "->", "receive",
    # Pipe/Composition (in OTP macros / syntax forms)
    "|"
]

Fortran103_ops = [
    # Arithmetic operators
    "+", "-", "*", "/", "**",
    # Relational operators (symbolic)
    "==", "/=", "<", "<=", ">", ">=",
    # Relational operators (alternative syntax)
    ".EQ.", ".NE.", ".LT.", ".LE.", ".GT.", ".GE.",
    # Logical operators
    ".AND.", ".OR.", ".NOT.", ".EQV.", ".NEQV.",
    # Character concatenation
    "//",
    # Assignment
    "=",
    # Pointer assignment (introduced in Fortran 90+)
    "=>"
]


Go25_ops = [
    # Arithmetic operators
    "+", "-", "*", "/", "%",
    # Bitwise operators
    "&", "|", "^", "<<", ">>", "&^",
    # Comparison operators
    "==", "!=", "<", "<=", ">", ">=",
    # Logical operators
    "&&", "||", "!",
    # Assignment operators
    "=", "+=", "-=", "*=", "/=", "%=",
    "<<=", ">>=", "&=", "|=", "^=", "&^=",
    # Increment / decrement
    "++", "--",
    # Other / special
    ":=", "...", ".", "&", "*", "<-"
]

Java67_ops = [
    # Arithmetic
    "+", "-", "*", "/", "%",
    # Unary
    "+", "-", "++", "--", "~", "!",
    # Assignment
    "=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>=", ">>>=",
    # Relational / Comparison
    "==", "!=", ">", "<", ">=", "<=",
    # Logical
    "&&", "||", "!",
    # Bitwise
    "&", "|", "^", "~", "<<", ">>", ">>>",
    # Ternary
    "?", ":",
    # Instance / type
    "instanceof",
    # Lambda
    "->",
    # Object access
    ".", "[]", "()",
    # Other
    "::",
]


JS59_ops = [
    # Arithmetic
    "+", "-", "*", "/", "%",
    # Assignment
    "=", "+=", "-=", "*=", "/=", "%=",
    # Comparison
    "==", "!=", "===", "!==", ">", ">=", "<", "<=",
    # Logical
    "&&", "||", "!",
    # Bitwise
    "&", "|", "^", "~", "<<", ">>", ">>>",
    # Unary
    "+", "-", "++", "--", "typeof", "void", "delete",
    # Conditional (ternary)
    "?", ":",
    # String concatenation (via '+')
    # Already covered by arithmetic "+"
    # Member access
    ".", "[]", "()",
    # Special (in, instanceof)
    "in", "instanceof"
]

Kotlin79_ops = [
    # Arithmetic
    "+", "-", "*", "/", "%",
    # Unary
    "+", "-", "++", "--", "!", "~",
    # Assignment
    "=", "+=", "-=", "*=", "/=", "%=",
    # Comparison
    "==", "!=", "===", "!==", "<", "<=", ">", ">=",
    # Logical
    "&&", "||", "!",
    # Bitwise (functions, not symbolic operators)
    "shl", "shr", "ushr", "and", "or", "xor", "inv",
    # Range and progression
    "..", "downTo", "until", "step",
    # Elvis and null safety
    "?:", "?.", "::", "!!", "as", "as?", "is", "!is",
    # Infix containment
    "in", "!in",
    # Function & property reference
    "::",
    # Other
    "->", "@", "@@", ";"
]


Lua22_ops = [
    # Arithmetic
    "+", "-", "*", "/", "//", "%", "^",
    # Relational
    "==", "~=", "<", ">", "<=", ">=",
    # Logical
    "and", "or", "not",
    # Concatenation
    "..",
    # Length
    "#",
    # Bitwise (Lua 5.3+ only)
    "&", "|", "~", "<<", ">>", "~",
    # Assignment
    "=",  # (used for variable assignment)
    # Other symbols
    "(", ")", "[", "]", "{", "}", ";", ":", ",", "."
]

MATLAB20_ops = [
    # Arithmetic
    "+", "-", ".*", "*", "./", "/", ".\\", "\\", ".^", "^",
    # Relational
    "==", "~=", "<", "<=", ">", ">=",
    # Logical
    "&", "|", "~", "&&", "||",
    # Assignment
    "=",  # variable assignment
    # Increment/decrement (not supported like ++ or --)
    # Element-wise vs matrix
    # (already handled above in arithmetic with `.` prefix)
    # String
    "==", "~=", "+", "[]", "''",
    # Other/Misc
    ":", ".", "'", ".'", "...", "@"
]

ObjectiveC85_ops = [
    # Arithmetic
    "+", "-", "*", "/", "%",
    # Increment / Decrement
    "++", "--",
    # Relational
    "==", "!=", ">", "<", ">=", "<=",
    # Logical
    "&&", "||", "!",
    # Bitwise
    "&", "|", "^", "~", "<<", ">>",
    # Assignment
    "=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>=",
    # Ternary
    "?", ":",
    # Member access and pointer
    ".", "->", "*", "&",
    # Objective-C specific
    "@", "@selector", "@protocol", "@interface", "@implementation",
    "@end", "@class", "@encode", "@defs", "@synchronized", "@try", "@catch", "@finally", "@throw",
    # Other
    "sizeof", "typeof"
]


PHP69_ops = [
    # Arithmetic
    "+", "-", "*", "/", "%", "**",
    # Assignment (and compound)
    "=", "+=", "-=", "*=", "/=", "%=", "**=", ".=", "&=", "|=", "^=", "<<=", ">>=",
    # Comparison
    "==", "===", "!=", "<>", "!==", "<", ">", "<=", ">=",
    # Increment/Decrement
    "++", "--",
    # Logical
    "and", "or", "xor", "!", "&&", "||",
    # Bitwise
    "&", "|", "^", "~", "<<", ">>",
    # String
    ".",  # concatenation
    # Array
    "=>",  # key => value
    # Null coalescing (PHP 7+)
    "??",  # null coalescing
    "??=", # null coalescing assignment
    # Ternary
    "?", ":",
    # Spaceship operator (PHP 7+)
    "<=>",
    # Execution (shell)
    "`...`"  # backticks for shell execution
]


Python38_ops = [
    # Arithmetic Operators
    "+", "-", "*", "/", "%", "//", "**",
    # Assignment Operators
    "=", "+=", "-=", "*=", "/=", "%=", "//=", "**=",
    "&=", "|=", "^=", ">>=", "<<=",
    # Comparison Operators
    "==", "!=", "<", ">", "<=", ">=",
    # Logical Operators
    "and", "or", "not",
    # Bitwise Operators
    "&", "|", "^", "~", "<<", ">>",
    # Membership Operators
    "in", "not in",
    # Identity Operators
    "is", "is not",
    # Unary Operators
    "+", "-", "~", "not",
    # Ternary Operator
    "if ... else",  # used in expressions like x if cond else y
    # Lambda (anonymous function)
    "lambda",
    # Walrus Operator (since Python 3.8)
    ":=",
    # Other structural (technically not operators, but syntactic)
    ".", ",", ":", ";", "[]", "()", "{}"
]


R21_ops = [
    # Arithmetic Operators
    "+", "-", "*", "/", "^", "%%", "%/%",
    # Relational Operators
    "==", "!=", "<", ">", "<=", ">=",
    # Logical Operators (element-wise and short-circuiting)
    "&", "|", "!", "&&", "||",
    # Assignment Operators
    "<-", "->", "<<-", "->>", "=",  # <- and = most common
    ":=",                          # from data.table, not base R
    # Sequence Operator
    ":",
    # Membership Operator (custom %in%)
    "%in%",
    # Matrix Multiplication
    "%*%",  # matrix multiplication
    "%o%",  # outer product
    "%x%",  # Kronecker product
    # Special / user-defined infix operators
    "%>%",   # pipe (from magrittr / dplyr)
    "%>%T%", "%<>%", "%$%",        # variations of pipe
    # Miscellaneous
    "~",     # model formula
    "$",     # list element access
    "@",     # S4 object slot access
    "::", ":::",  # package-qualified access
    "[", "]", "[[", "]]"           # indexing
]

Ruby41_ops = [
    # Arithmetic Operators
    "+", "-", "*", "/", "%", "**",
    # Comparison Operators
    "==", "!=", ">", "<", ">=", "<=", "<=>", "===",
    # Assignment Operators
    "=", "+=", "-=", "*=", "/=", "%=", "**=", "&&=", "||=",
    # Logical Operators
    "and", "or", "not", "&&", "||", "!",
    # Bitwise Operators
    "&", "|", "^", "~", "<<", ">>",
    # Range Operators
    "..", "...",
    # Ternary Operator
    "?:",  # used as `condition ? true_value : false_value`
    # Defined and Matching Operators
    "defined?", "=~", "!~",
    # Safe Navigation Operator (Ruby 2.3+)
    "&.",
    # Object Identity and Equality
    "equal?", "eql?", "===", "==", "!=",
    # Miscellaneous
    "..", "...", "::", ".", "&", "*", "**", "`", "[]", "[]=", "?",
]


Rust53_ops = [
    # Arithmetic Operators
    "+", "-", "*", "/", "%",
    # Assignment Operators
    "=", "+=", "-=", "*=", "/=", "%=",
    "&=", "|=", "^=", "<<=", ">>=",
    # Comparison Operators
    "==", "!=", "<", ">", "<=", ">=",
    # Logical Operators
    "&&", "||", "!",
    # Bitwise Operators
    "&", "|", "^", "<<", ">>", "~",  # ~ is not a valid Rust operator, included for completeness
    # Range Operators
    "..", "..=",
    # Other Operators
    "->", "=>", "::", ".", "..", ",", ";", ":", "#",
    # Dereference and Borrowing
    "*", "&", "&mut",
    # Pattern Matching and Closure
    "|", "ref", "mut",
    # Type Casting and Size
    "as", "sizeof", "alignof",
    # Macro & Path-related
    "!", "::",
    # Unsafe/Raw Pointers
    "*const", "*mut",
    # Box / Smart Pointer (conceptual usage)
    "box"
]


Scala40_ops = [
    # Arithmetic
    "+", "-", "*", "/", "%",
    # Relational
    "==", "!=", "<", "<=", ">", ">=",
    # Logical
    "&&", "||", "!",
    # Bitwise
    "&", "|", "^", "~", "<<", ">>", ">>>",
    # Assignment
    "=", "+=", "-=", "*=", "/=", "%=",
    "&=", "|=", "^=", "<<=", ">>=", ">>>=",
    # Object equality
    "eq", "ne", "==", "!=", "equals",
    # Comparison
    "<", "<=", ">", ">=", "compareTo",
    # Other / Misc
    ":", "::", "#", "@", "=>", "<-", "<:", ">:", "<%", "%>", "~>", "→", "←",
    # Method invocation
    ".", "(", ")", "[", "]",
    # Pattern matching / Guards
    "|", "case", "match", "_", "=>",
    # Type-related
    "isInstanceOf", "asInstanceOf",
    # Functional
    "=>", "<-", "map", "flatMap", "filter", "withFilter",
    # Special symbolic methods (often overloaded)
    "unary_+", "unary_-", "unary_!", "unary_~",
    # For-comprehension operators
    "yield", "for", "do", "while", "if", "else"
]


Swift97_ops = [
    # Arithmetic
    "+", "-", "*", "/", "%",
    # Unary arithmetic
    "+", "-", "++", "--",  # 注：++ 和 -- 已弃用自 Swift 3
    # Assignment
    "=", "+=", "-=", "*=", "/=", "%=",
    # Comparison
    "==", "!=", ">", "<", ">=", "<=",
    # Logical
    "!", "&&", "||",
    # Bitwise
    "&", "|", "^", "~", "<<", ">>",
    # Range
    "...", "..<",
    # Identity and Nil-coalescing
    "===","!==", "??",
    # Type casting
    "is", "as", "as?", "as!", "Any", "AnyObject",
    # Optional chaining and force unwrapping
    ".", "?", "!", "?." , "?[" , "?()",
    # Function arrow
    "->",
    # Closure shorthand
    "in", "{", "}", "$0", "$1", "$2",
    # Tuple and function call
    "(", ")", ",",
    # Subscript and dictionary
    "[", "]", "[:]",
    # Other structural
    ":", ";", "@", "#", "_",
    # Custom operators (user-defined) #, etc. (defined via `operator` keyword)
    "<>", "<=>", "<<<", ">>>", "-->",
]


python38_ops = [
    # Arithmetic
    "+", "-", "*", "/", "//", "%", "**",
    # Comparison
    "==", "!=", ">", "<", ">=", "<=",
    # Logical
    "and", "or", "not",
    # Bitwise
    "&", "|", "^", "~", "<<", ">>",
    # Assignment
    "=", "+=", "-=", "*=", "/=", "//=", "%=", "**=", "&=", "|=", "^=", "<<=", ">>=",
    # Membership
    "in", "not in",
    # Identity
    "is", "is not"
]
py_ops = {
    "Arithmetic": ["+", "-", "*", "/", "//", "%", "**"],
    "Comparison": ["==", "!=", ">", "<", ">=", "<="],
    "Logical": ["and", "or", "not"],
    "Bitwise": ["&", "|", "^", "~", "<<", ">>"],
    "Assignment": ["=", "+=", "-=", "*=", "/=", "//=", "%=", "**=", "&=", "|=", "^=", "<<=", ">>="],
    "Membership": ["in", "not in"],
    "Identity": ["is", "is not"]
}