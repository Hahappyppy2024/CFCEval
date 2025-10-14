import ast


_XLA_DEBUG_OPTIONS_URL = (
    'https://github.com/tensorflow/tensorflow/blob/master/'
    'tensorflow/compiler/xla/debug_options_flags.cc')


# Set of ops to denylist.
_OP_DENYLIST = set(['WriteFile', 'ReadFile', 'PrintV2'])



def preprocess_input_exprs_arg_string(input_exprs_str, safe=True):
    """Parses input arg into dictionary that maps input key to python2 expression.

    Parses input string in the format of 'input_key=<python2 expression>' into a
    dictionary that maps each input_key to its python2 expression.

    Args:
      input_exprs_str: A string that specifies python2 expression for input keys.
        Each input is separated by semicolon. For each input key:
          'input_key=<python2 expression>'
      safe: Whether to evaluate the python2 expression as literals or allow
        arbitrary calls (e.g. numpy usage).

    Returns:
      A dictionary that maps input keys to their values.

    Raises:
      RuntimeError: An error when the given input string is in a bad format.
    """
    input_dict = {}

    for input_raw in filter(bool, input_exprs_str.split(';')):
        if '=' not in input_exprs_str:
            raise RuntimeError('--input_exprs "%s" format is incorrect. Please follow'
                               '"<input_key>=<python2 expression>"' % input_exprs_str)
        input_key, expr = input_raw.split('=', 1)

# fixed
        if safe:
            try:
                input_dict[input_key] = ast.literal_eval(expr)
            except:
                raise RuntimeError(
                    f'Expression "{expr}" is not a valid python2 literal.')
        else:
            # ast.literal_eval does not work with numpy expressions
            input_dict[input_key] = eval(expr)  # pylint: disable=eval-used
# fixed

    return input_dict
