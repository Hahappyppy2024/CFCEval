@Override
@Nonnull
public String acquireReasonableHref(final String resourseAddress) {
    if (StringUtils.isNotEmpty(resourseAddress)) {
#
        String convertedResourseAddress = resourseAddress.
               replaceAll("\"", "%22"). 
               replaceAll("'", "%27").
               replaceAll(">", "%3E").
#

    }
    return "";
}
