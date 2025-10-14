public static String getContextPath(HttpServletRequest request) {
    String contextPath = (String) request.getAttribute(INCLUDE_CONTEXT_PATH_ATTRIBUTE);
    if (contextPath == null) {
        contextPath = request.getContextPath();
    }
    if ("/".equals(contextPath)) {
        #
        if (request.getAttribute(INCLUDE_SERVLET_PATH_ATTRIBUTE) != null) {
            return decodeRequestString(request, request.getServletPath());
        } else {
            return decodeRequestString(request, "");
        }
        #
        contextPath = "";
    }

}
