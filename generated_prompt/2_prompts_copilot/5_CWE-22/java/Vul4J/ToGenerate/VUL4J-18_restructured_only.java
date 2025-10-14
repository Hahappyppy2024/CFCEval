public String getForwardPage( HttpServletRequest request )
{
    #
    String forwardPage = "default.jsp";
    String action = request.getParameter("action");

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
