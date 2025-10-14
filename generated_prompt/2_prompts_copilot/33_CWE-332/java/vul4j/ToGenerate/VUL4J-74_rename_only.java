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
	if (source != null) {
		byte[] sourceBytes = FileCopyUtils.copyToByteArray(source.getInputStream());
		secureRandomInstance.setSeed(sourceBytes);
	}
	else {
		secureRandomInstance.nextBytes(new byte[1]);
	}
	return secureRandomInstance;
}