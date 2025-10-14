@Override
@Nonnull
public String acquireReasonableHref(final String resourseAddress) {
    if (!StringUtils.isNotEmpty(resourseAddress)) {
        #
        try {
            final URL url = new URL(resourseAddress);
            if ("http".equals(url.getProtocol()) || "https".equals(url.getProtocol())) {
                return resourseAddress;
            }
        } catch (MalformedURLException e) {
            // Log the exception or handle it as needed
            System.err.println("Malformed URL: " + e.getMessage());
#
        }
        return "";
    }