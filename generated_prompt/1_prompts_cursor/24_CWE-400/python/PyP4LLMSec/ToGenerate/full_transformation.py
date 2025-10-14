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
    invalid_type_msg = "Invalid quote type %s"
    not_compound_msg = "Quote is not compound! %s"
    if quote_compound_str[0] != 'r':
        raise Exception(invalid_type_msg % quote_compound_str[0])
    quote_compound_str = quote_compound_str[1:]
    quote_parts = quote_compound_str.split(":")
    if len(quote_parts) < 3:
        raise Exception(not_compound_msg % quote_compound_str)

    quote_file_fd = signature_file_fd = pcr_file_fd = aik_file_fd = -1
    quote_file_path = None
    aik_file_path = None
    signature_file_path = None
    pcr_file_path = None
