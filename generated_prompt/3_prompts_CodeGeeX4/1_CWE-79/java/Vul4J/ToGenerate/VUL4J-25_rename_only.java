@Override
@Nonnull
public String acquireReasonableHref(final String resourseAddress) {
    if (StringUtils.isNotEmpty(resourseAddress)) {
        #
        final String[] parts = resourseAddress.split("/");
        if (parts.length > 1) {
            return parts[parts.length - 1];
#
        }
    }
    return "";
}
