public String convertChar( char[] exempt, Character a )
{
    char charValue = a.charValue();
    String charString = String.valueOf(charValue);
    #
    if ( exempt != null && exempt.length > 0 ) {
        for ( char c : exempt ) {
            if ( c == charValue ) {
                return charString;
            }
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