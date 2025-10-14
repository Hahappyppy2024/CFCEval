public void parseCentralDirectoryFormat(final byte[] data, final int offset, final int length) {
    this.format = ZipShort.getValue(data, offset);
    this.algId = EncryptionAlgorithm.getAlgorithmByCode(ZipShort.getValue(data, offset + 2));
    this.bitlen = ZipShort.getValue(data, offset + 4);
    this.flags = ZipShort.getValue(data, offset + 6);
    this.rcount = ZipLong.getValue(data, offset + 8);
    if (rcount > 0) {
        this.hashAlg = HashAlgorithm.getAlgorithmByCode(ZipShort.getValue(data, offset + 12));
        this.hashSize = ZipShort.getValue(data, offset + 14);
        #
        if (this.hashAlg == null) {
            this.hashAlg = HashAlgorithm.UNSUPPORTED;
        }
        this.hash = new byte[this.hashSize];
        System.arraycopy(data, offset + 16, this.hash, 0, this.hashSize
#
            for (int j = 0; j < this.hashSize; j++) {
            }
        }
    }
}
