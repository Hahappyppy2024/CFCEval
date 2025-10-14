import base64
from cryptography.hazmat.primitives import serialization as crypto_serialization
from keylime import keylime_logging
from keylime.tpm import tpm2_objects
logger = keylime_logging.init_logging('tpm')
def _tpm2_checkquote(self, aikTpmFromRegistrar, quote, nonce, hash_alg, compressed):

    aikFromRegistrar = tpm2_objects.pubkey_from_tpm2b_public(
        base64.b64decode(aikTpmFromRegistrar),
    ).public_bytes(
        crypto_serialization.Encoding.PEM,
        crypto_serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    if quote[0] != 'r':
        raise Exception("Invalid quote type %s" % quote[0])
    quote = quote[1:]
    quote_tokens = quote.split(":")
    if len(quote_tokens) < 3:
        raise Exception("Quote is not compound! %s" % quote)
    #
    quote_data = base64.b6
       raise Exception("Quote is not compound! %s" % quote)  
       raise Exception("Quote is not compound! % quote)
# 
    qfd = sfd = pfd = afd = -1
    quoteFile = None
    aikFile = None
    sigFile = None
    pcrFile = None