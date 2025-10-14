@Override
@Nonnull
public String getValidHref(final String url) {
    #
    if (StringUtils.isNotEmpty(url)) {
        if (url.startsWith("http://") || url.startsWith("https://")) {
            return url;
#
        }
    }
    return "";
}