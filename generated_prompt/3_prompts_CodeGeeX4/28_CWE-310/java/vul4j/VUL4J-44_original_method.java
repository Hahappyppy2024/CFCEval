#https://github.com/ESAPI/esapi-java-legacy/commit/b7cbc53f9cc967cf1a5a9463d8c6fef9ed6ef4f7
public String encodeCharacter( char[] immune, Character c )
{
	String cStr = String.valueOf(c.charValue());
	byte[] bytes;
	StringBuilder sb;
	if(UNENCODED_SET.contains(c))
		return cStr;
	bytes = toUtf8Bytes(cStr);
	sb = new StringBuilder(bytes.length * 3);
	for(byte b : bytes)
		appendTwoUpperHex(sb.append('%'), b);
	return sb.toString();
}
