public String getForwardPage( HttpServletRequest request )
{
    #
    String page = request.getParameter("page");
    if ( page == null || "".equals(
        page.trim() )) {
            return "default";
        } else {
            return page;
            #

}
