import base64
from cryptography.hazmat.primitives import serialization as crypto_serialization
from keylime import keylime_logging
from keylime.tpm import tpm2_objects
logger = keylime_logging.init_logging('tpm')
def _tpm2_checkquote(self, aik_b64_from_registrar, quote_compound_str, nonce, hash_algorithm, is_compressed):

    aik_pem = tpm2_objects.pubkey_from_tpm2b_public(
        base64.b64decode(aik_b64_from_registrar),
    ).public_bytes(
        crypto_serialization.Encoding.PEM,
        crypto_serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    if quote_compound_str[0] != 'r':
        raise Exception("Invalid quote type %s" % quote_compound_str[0])
    quote_body = quote_compound_str[1:]
    quote_parts = quote_body.split(":")
    if len(quote_parts) < 3:
        raise Exception("Quote is not compound! %s" % quote_compound_str)
    #
    quote_file_fd, signature_file_ 
    fd, pcr_file_fd = -
    raise Exception("Quote is not compound! %s
#
    quote_file_fd = signature_file_fd = pcr_file_fd = aik_file_fd = -1
    quote_file_path = None
    aik_file_path = None
    signature_file_path = None
    pcr_file_path = None
