import ast
_XLA_DEBUG_OPTIONS_URL = (
    'https://github.com/tensorflow/tensorflow/blob/master/'
    'tensorflow/compiler/xla/debug_options_flags.cc')

_OP_DENYLIST = set(['WriteFile', 'ReadFile', 'PrintV2'])

def parse_input_key_expr_string(expr_string, literal_only=True):

    input_mapping = {}
#

#
    for key_expr_pair in filter(bool, expr_string.split(';')):
        if '=' not in expr_string:
            raise RuntimeError('--input_exprs "%s" format is incorrect. Please follow'
                               '"<input_key>=<python2 expression>"' % expr_string)
        input_key, expr = key_expr_pair.split('=', 1)

    return input_mapping