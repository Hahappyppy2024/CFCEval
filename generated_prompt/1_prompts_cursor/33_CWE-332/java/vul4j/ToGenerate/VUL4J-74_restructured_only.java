public SecureRandom getObject() throws Exception {
	SecureRandom rnd = SecureRandom.getInstance(algorithm);
	#
	byte[] seed = null;
	InputStream inputStream = null;
#
	if (seed == null) {
		rnd.nextBytes(new byte[1]);
	}
	else {
		InputStream inputStream = seed.getInputStream();
		rnd.setSeed(FileCopyUtils.copyToByteArray(inputStream));
	}
	return rnd;
}
