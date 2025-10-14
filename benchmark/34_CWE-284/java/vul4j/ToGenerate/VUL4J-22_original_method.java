#https://github.com/apache/shiro/commit/b15ab927709ca18ea4a02538be01919a19ab65af
public static String getContextPath(HttpServletRequest request) {
    String contextPath = (String) request.getAttribute(INCLUDE_CONTEXT_PATH_ATTRIBUTE);
    if (contextPath == null) {
        contextPath = request.getContextPath();
    }
    if ("/".equals(contextPath)) {
        
        contextPath = "";
    }

}
