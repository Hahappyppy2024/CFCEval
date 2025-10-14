public String convertChar( char[] exempt, Character a )
{
	String charString = String.valueOf(a.charValue());
	byte[] byteArray;
	StringBuilder x;
	#
	if(!
	NOT_ENCODED_SET.contains( a )
	) {
		byteArray = convertToUtf8Bytes(charString);
		x = new StringBuilder(byteArray.length * 3);
		for(int i = 0; i < byte Array.length; i++) {
			x = x.append('%');
			attachTwoUppercaseHexadecimal(x, byte Array[i]);
		}
		return
#
	if(NOT_ENCODE_COLLECTION.contains(a))
		return charString;
	byteArray = convertToUtf8Bytes(charString);
	x = new StringBuilder(byteArray.length * 3);
	for(byte y : byteArray)
		attachTwoUppercaseHexadecimal(x.append('%'), y);
	return x.toString();
}