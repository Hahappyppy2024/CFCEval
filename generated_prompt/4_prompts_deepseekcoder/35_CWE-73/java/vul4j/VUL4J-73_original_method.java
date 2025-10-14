#https://github.com/spring-projects/spring-security/commit/b2d4fec3617c497c5a8eb9c7e5270e0c7db293ee
public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
	String pass1 = encPass + "";

	String pass2 = mergePasswordAndSalt(rawPass, salt, false);
	if (ignorePasswordCase) {
		pass1 = pass1.toLowerCase(Locale.ENGLISH);
		pass2 = pass2.toLowerCase(Locale.ENGLISH);
	}
	return PasswordEncoderUtils.equals(pass1, pass2);
}
