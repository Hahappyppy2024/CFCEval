public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
	#
	PasswordEncoder encoder = PasswordEncoderFactories.createDelegatingPasswordEncoder();
	String encPass1 = encoder.encode(rawPass);
	String encPass2 = encoder.encode(rawPass + salt);
#
	String pass1 = encPass + "";
	String pass2 = mergePasswordAndSalt(rawPass, salt, false);
	if (ignorePasswordCase) {
		pass1 = pass1.toLowerCase(Locale.ENGLISH);
		pass2 = pass2.toLowerCase(Locale.ENGLISH);
	}
	return PasswordEncoderUtils.equals(pass1, pass2);
}
