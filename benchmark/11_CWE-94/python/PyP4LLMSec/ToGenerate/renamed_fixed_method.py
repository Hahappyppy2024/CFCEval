import ast

_XLA_DEBUG_OPTIONS_URL = (
    'https://github.com/tensorflow/tensorflow/blob/master/'
    'tensorflow/compiler/xla/debug_options_flags.cc')

# Set of ops to denylist.
_OP_DENYLIST = set(['WriteFile', 'ReadFile', 'PrintV2'])

def parse_input_key_expr_string(expr_string, literal_only=True):
    """Parses input arg into dictionary that maps input key to python2 expression.

    Parses input string in the format of 'input_key=<python2 expression>' into a
    dictionary that maps each input_key to its python2 expression.

    Args:
      expr_string: A string that specifies python2 expression for input keys.
        Each input is separated by semicolon. For each input key:
          'input_key=<python2 expression>'
      literal_only: Whether to evaluate the python2 expression as literals or allow
        arbitrary calls (e.g. numpy usage).

    Returns:
      A dictionary that maps input keys to their values.

    Raises:
      RuntimeError: An error when the given input string is in a bad format.
    """
    input_mapping = {}

    for key_expr_pair in filter(bool, expr_string.split(';')):
        if '=' not in expr_string:
            raise RuntimeError('--input_exprs "%s" format is incorrect. Please follow'
                               '"<input_key>=<python2 expression>"' % expr_string)
        input_key, expr = key_expr_pair.split('=', 1)

    return input_mapping