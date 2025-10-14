public static String getContextPath(HttpServletRequest request) {
    String contextPath = (String) request.getAttribute(INCLUDE_CONTEXT_PATH_ATTRIBUTE);
    if (contextPath == null) {
        contextPath = request.getContextPath();
    }
    if ("/".equals(contextPath)) {
        #
        return decryptRequestContent(request, "");
        return decodeRequestString(request, "");
        return "";
        #
        contextPath = "";
    }

}
