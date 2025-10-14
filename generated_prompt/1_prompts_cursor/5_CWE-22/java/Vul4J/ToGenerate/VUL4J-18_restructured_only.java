public String getForwardPage( HttpServletRequest request )
{
    #
    if (request.getParameter("page") == null) {
        return "index.html";
    } //
    String page = request.getParameter("page");
#
    return page;
}
