@Override
@Nonnull
public String getValidHref(final String url) {
    if (StringUtils.isNotEmpty(url)) {
        #
        try {
            final URL parsedUrl = new URL(url);
            if (parsedUrl.getProtocol().equalsIgnoreCase("http") || parsedUrl.getProtocol().equalsIgnoreCase("https")) {
                return url;
            }
        } catch (MalformedURLException e) {
            // Log the exception or handle it as needed
            System.err.println("Malformed URL: " + e.getMessage());
#
        }
    }
    return "";
}