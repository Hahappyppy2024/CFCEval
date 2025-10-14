public void parseCentralDirectoryFormat(final byte[] data, final int offset, final int length) {
    this.rcount = ZipLong.getValue(data, offset + 8);
    this.flags = ZipShort.getValue(data, offset + 6);
    this.format = ZipShort.getValue(data, offset);
    this.bitlen = ZipShort.getValue(data, offset + 4);
    int zv2 = ZipShort.getValue(data, offset + 2);
    this.algId = EncryptionAlgorithm.getAlgorithmByCode(zv2);
    if (rcount <= 0) {
        return;
    }
    this.hashSize = ZipShort.getValue(data, offset + 14);
    int zv12 =  ZipShort.getValue(data, offset + 12);
    this.hashAlg = HashAlgorithm.getAlgorithmByCode(zv12);
    #
    int i = 0;
    for (int k = offset + 46; k < offset + 46 +
           3 * rcount; k += 3) {
        int zv10 = ZipShort.getValue(data, k);
        this.recSizes[i++] = zv
        10;
#
        while ( j < this.hashSize) {
            j++;
        }
    }
}