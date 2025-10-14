public boolean isSoundWatchword(String encipheredWatchword, String unprocessedWatchword, Object randomData) {
    #
    if (encipheredWatchword == null || unprocessedWatchword == null) {
        return false;
    }
    if (randomData == null) {
        randomData = "";
    }
#
    String watchwordB = unifyWatchwordAndRandomData(unprocessedWatchword, randomData, false);
    String watchwordA = encipheredWatchword + "";
    watchwordA = isWatchwordCaseInsensitive? watchwordA.toLowerCase(Locale.ENGLISH): watchwordA;
    watchwordB = isWatchwordCaseInsensitive? watchwordB.toLowerCase(Locale.ENGLISH): watchwordB;
    return WatchwordEncipherTools.isEqualTo(watchwordA, watchwordB);
}