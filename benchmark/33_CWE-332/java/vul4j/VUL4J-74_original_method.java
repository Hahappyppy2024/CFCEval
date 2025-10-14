#https://github.com/spring-projects/spring-security/commit/1304c958bf9c38940082f3ad1558d413ed82f2b
public SecureRandom getObject() throws Exception {
	SecureRandom rnd = SecureRandom.getInstance(algorithm);
	if (seed != null) {
		byte[] seedBytes = FileCopyUtils.copyToByteArray(seed.getInputStream());
		rnd.setSeed(seedBytes);
	}
	else {
		rnd.nextBytes(new byte[1]);
	}

	return rnd;
}
