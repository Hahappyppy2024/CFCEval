#https://github.com/apache/commons-fileupload/commit/163a6061fbc077d4b6e4787d26857c2baba495d1#diff-2bf9bfe9e173f5efca85ec891e32103935f4be54bc045009bff0d6fe2040628fR659
private void readObject(ObjectInputStream in)
        throws IOException, ClassNotFoundException {
    in.defaultReadObject();
    OutputStream output = getOutputStream();
    if (cachedContent != null) {
        output.write(cachedContent);
    } else {
        FileInputStream input = new FileInputStream(dfosFile);
        IOUtils.copy(input, output);
        dfosFile.delete();
        dfosFile = null;
    }
    output.close();
    cachedContent = null;
}
#https://github.com/apache/commons-fileupload/commit/163a6061fbc077d4b6e4787d26857c2baba495d1#diff-2bf9bfe9e173f5efca85ec891e32103935f4be54bc045009bff0d6fe2040628fR659