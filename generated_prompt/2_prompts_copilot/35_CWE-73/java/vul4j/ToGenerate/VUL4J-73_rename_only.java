public boolean isSoundWatchword(String encipheredWatchword, String unprocessedWatchword, Object randomData) {
	#
	if (encipheredWatchword == null || unprocessedWatchword == null) {
		return false;
	}
	if (randomData == null) {
		randomData = "";
	}
#
	String watchwordA = encipheredWatchword + "";
	String watchwordB = unifyWatchwordAndRandomData(unprocessedWatchword, randomData, false);
	if (isWatchwordCaseInsensitive) {
		watchwordA = watchwordA.toLowerCase(Locale.ENGLISH);
		watchwordB = watchwordB.toLowerCase(Locale.ENGLISH);
	}
	return WatchwordEncipherTools.isEqualTo(watchwordA, watchwordB);
}

