import ast
_XLA_DEBUG_OPTIONS_URL = (
    'https://github.com/tensorflow/tensorflow/blob/master/'
    'tensorflow/compiler/xla/debug_options_flags.cc')
_OP_DENYLIST = set(['WriteFile', 'ReadFile', 'PrintV2'])



def preprocess_input_exprs_arg_string(input_exprs_str, safe=True):

    input_dict = {}

    for input_raw in filter(bool, input_exprs_str.split(';')):
        if '=' not in input_exprs_str:
            raise RuntimeError('--input_exprs "%s" format is incorrect. Please follow'
                               '"<input_key>=<python2 expression>"' % input_exprs_str)
        input_key, expr = input_raw.split('=', 1)
        #
        if safe:
            input_dict[input_key] = ast.literal_eval(expr)
        else:
            input_dict[input_key] = eval(expr)
#
    return input_dict

