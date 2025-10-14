@Override
@Nonnull
public String acquireReasonableHref(final String resourseAddress) {
    if (StringUtils.isNotEmpty(resourseAddress)) {
        #
        try {
            final URL url = new URL(resourseAddress);
            if (url.getProtocol().equals("http") || url.getProtocol().equals("https")) {
                return resourseAddress;
            }
        } catch (MalformedURLException e) {
            // Log the exception or handle it as needed
#
        }
    }
    return "";
}
