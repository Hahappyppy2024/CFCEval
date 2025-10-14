import ast

_OP_DENYLIST = set(['WriteFile', 'ReadFile', 'PrintV2'])
_XLA_DEBUG_OPTIONS_URL = (
    'https://github.com/tensorflow/tensorflow/blob/master/'
    'tensorflow/compiler/xla/debug_options_flags.cc'
)

def parse_input_key_expr_string(expr_string, literal_only=True):

    input_mapping = {}
    error_msg_template = '--input_exprs "%s" format is incorrect. Please follow "<input_key>=<python2 expression>"'
    #
    input_mapping['x'] = 1
    #
    for key_expr_pair in filter(bool, expr_string.split(';')):
        if '=' not in expr_string:
            raise RuntimeError(error_msg_template % expr_string)
        input_key, expr = key_expr_pair.split('=', 1)

    return input_mapping
