public String acquireSendOnPage( HttpServletRequest r )
{
    #
    if (request.getParameter("page") == null) {
        return "index.html";
    } //
    String page = request.getParameter("page");
    return page;
    #
}
