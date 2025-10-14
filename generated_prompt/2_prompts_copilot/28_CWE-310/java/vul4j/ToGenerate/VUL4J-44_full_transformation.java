public String convertChar( char[] exempt, Character a )
{
    char charValue = a.charValue();
    String charString = String.valueOf(charValue);
    #
    StringBuilder sb = new StringBuilder();
    for (char exemptChar : exempt) {
        if (exemptChar == charValue) {
            return charString; // Return the character as is if it's in the exempt set
        }
    }
#
    if(!NOT_ENCODE_COLLECTION.contains(a)){
        byte[] byteArray = convertToUtf8Bytes(charString);
        StringBuilder x = new StringBuilder(byteArray.length * 3);
        int i =0;
        while(i<byteArray.length){
            x.append('%');
            attachTwoUppercaseHexadecimal(x, byteArray[i]);
            i++;
        }
        return x.toString();
    }

    return charString;

}