@Override
@Nonnull
public String getValidHref(final String url) {
    if (StringUtils.isNotEmpty(url)) {
        #
        String encodedUrl = url.replaceAll("\"
        ", "%22")
           .replaceAll
           ('\'', '%27')
           .
           replaceAll(">", "%3E");
           #
        return acquireReasonableHref(encoded
        Url);
        #

    }
    return "";
}