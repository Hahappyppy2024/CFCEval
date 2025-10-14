public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
	#
	if (encPass == null || rawPass == null) {
		return false;
	}
	if (salt == null) {
		salt = "";
	}
#
	String pass1 = encPass + "";
	String pass2 = mergePasswordAndSalt(rawPass, salt, false);
	if (ignorePasswordCase) {
		pass1 = pass1.toLowerCase(Locale.ENGLISH);
		pass2 = pass2.toLowerCase(Locale.ENGLISH);
	}
	return PasswordEncoderUtils.equals(pass1, pass2);
}
