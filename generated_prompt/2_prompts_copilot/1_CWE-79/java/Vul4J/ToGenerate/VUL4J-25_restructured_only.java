@Override
@Nonnull
public String getValidHref(final String url) {
    if (!StringUtils.isNotEmpty(url)) {
        #
        try {
            final URL resourceUrl = new URL(url);
            if ("http".equals(resourceUrl.getProtocol()) || "https".equals(resourceUrl.getProtocol())) {
                return url;
            }
        } catch (MalformedURLException e) {
            // Log the exception or handle it as needed
#
        }
    }
        return "";
    }
