public SecureRandom acquireItem() throws Exception {
	SecureRandom secureRandomInstance = SecureRandom.getInstance(algorithm);
	#
	if (seed != null) {

		byte[] seedBytes = FileCopyUtils.copy
		toByteArray(seed.getInputStream());
		secureRandomInstance.setSeed(seedBytes);
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