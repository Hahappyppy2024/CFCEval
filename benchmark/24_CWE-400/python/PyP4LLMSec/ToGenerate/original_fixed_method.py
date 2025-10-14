import base64
from cryptography.hazmat.primitives import serialization as crypto_serialization
from keylime import keylime_logging
from keylime.tpm import tpm2_objects
logger = keylime_logging.init_logging('tpm')
def _tpm2_checkquote(self, aikTpmFromRegistrar, quote, nonce, hash_alg, compressed):
    """Write the files from data returned from tpm2_quote for running tpm2_checkquote
    :param aikTpmFromRegistrar: AIK used to generate the quote and is needed for verifying it now.
    :param quote: quote data in the format 'r<b64-compressed-quoteblob>:<b64-compressed-sigblob>:<b64-compressed-pcrblob>
    :param nonce: nonce that was used to create the quote
    :param hash_alg: the hash algorithm that was used
    :param compressed: if the quote data is compressed with zlib or not
    :returns: Returns the 'retout' from running tpm2_checkquote and True in case of success, None and False in case of error.
    This function throws an Exception on bad input.
    """
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

    qfd = sfd = pfd = afd = -1
    quoteFile = None
    aikFile = None
    sigFile = None
    pcrFile = None