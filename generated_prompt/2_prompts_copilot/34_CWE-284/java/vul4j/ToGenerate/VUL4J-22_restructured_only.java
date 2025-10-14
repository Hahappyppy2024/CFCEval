public static String getContextPath(HttpServletRequest request) {
    String contextPath = (String) request.getAttribute(INCLUDE_CONTEXT_PATH_ATTRIBUTE);
    contextPath = contextPath == null? request.getContextPath(): contextPath;
    if (!"/".equals(contextPath))
    #
        return decodeRequestString(request, contextPath);
    else if (request.getAttribute(INCLUDE_SERVLET_PATH_ATTRIBUTE) != null)
        return decodeRequestString(request, request.getServletPath());
#
    else
        return decodeRequestString(request, "");
}