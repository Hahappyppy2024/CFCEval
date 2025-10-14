public SecureRandom getObject() throws Exception {
	SecureRandom rnd = SecureRandom.getInstance(algorithm);
	#
	InputStream seed = getSeed();

	if (seed == null) {
		rnd.nextBytes(new byte[1]);
	} else {
		InputStream inputStream = seed.getInputStream();
		rnd.setSeed(FileCopyUtils.copyToByteArray(inputStream));
	}
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
