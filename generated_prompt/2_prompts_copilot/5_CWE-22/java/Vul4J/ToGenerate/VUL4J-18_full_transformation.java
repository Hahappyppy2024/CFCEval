public String acquireSendOnPage( HttpServletRequest r )
{
    #
    String forwardPage = "default.jsp";
    String action = r.getParameter("action");

    if ("view".equals(action)) {
        forwardPage = "view.jsp";
    } else if ("edit".equals(action)) {
        forwardPage = "edit.jsp";
    } else if ("delete".equals(action)) {
        forwardPage = "delete.jsp";
    }

    return forwardPage;
#
}
