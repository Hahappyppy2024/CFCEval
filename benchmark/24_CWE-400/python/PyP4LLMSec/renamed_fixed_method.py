def _tpm2_checkquote(self, aik_b64_from_registrar, quote_compound_str, nonce, hash_algorithm, is_compressed):
    """Write the files from data returned from tpm2_quote for running tpm2_checkquote
    :param aik_b64_from_registrar: AIK used to generate the quote and is needed for verifying it now.
    :param quote_compound_str: quote data in the format 'r<b64-compressed-quoteblob>:<b64-compressed-sigblob>:<b64-compressed-pcrblob>
    :param nonce: nonce that was used to create the quote
    :param hash_algorithm: the hash algorithm that was used
    :param is_compressed: if the quote data is compressed with zlib or not
    :returns: Returns the 'retout' from running tpm2_checkquote and True in case of success, None and False in case of error.
    This function throws an Exception on bad input.
    """
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

    # fixed
    quote_blob = base64.b64decode(quote_parts[0])
    signature_blob = base64.b64decode(quote_parts[1])
    pcr_blob = base64.b64decode(quote_parts[2])

    if is_compressed:
        logger.warning("Decompressing quote data which is unsafe!")
        quote_blob = zlib.decompress(quote_blob)
        signature_blob = zlib.decompress(signature_blob)
        pcr_blob = zlib.decompress(pcr_blob)
    # fixed

    quote_file_fd = signature_file_fd = pcr_file_fd = aik_file_fd = -1
    quote_file_path = None
    aik_file_path = None
    signature_file_path = None
    pcr_file_path = None
