public String convertChar( char[] exempt, Character a )
{
	String charString = String.valueOf(a.charValue());
	byte[] byteArray;
	StringBuilder x;
	#
	for (char exemptChar : exempt) {
		if (exemptChar == a.charValue()) {
			return charString; // Return the character as is if it's in the exempt set
		}
	}
#
	if(NOT_ENCODE_COLLECTION.contains(a))
		return charString;
	byteArray = convertToUtf8Bytes(charString);
	x = new StringBuilder(byteArray.length * 3);
	for(byte y : byteArray)
		attachTwoUppercaseHexadecimal(x.append('%'), y);
	return x.toString();
}