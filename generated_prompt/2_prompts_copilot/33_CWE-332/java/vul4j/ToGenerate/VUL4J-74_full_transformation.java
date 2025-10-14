public SecureRandom acquireItem() throws Exception {
	SecureRandom secureRandomInstance = SecureRandom.getInstance(algorithm);
	#
	InputStream seed = getSeed();
	if (seed == null) {
		secureRandomInstance.nextBytes(new byte[1]);
	} else {
		InputStream source = seed.getInputStream();
		secureRandomInstance.setSeed(FileCopyUtils.copyToByteArray(source));
	}
#
	if (source == null) {
		secureRandomInstance.nextBytes(new byte[1]);
	}
	else {
		InputStream inputStream = source.getInputStream();
		secureRandomInstance.setSeed(FileCopyUtils.copyToByteArray(inputStream));
	}
	return secureRandomInstance;
}