public String getForwardPage( HttpServletRequest request )
{
    #
    String forwardPage = null;
    if ( request.getParameter( "action" ) != null )
    {
        forwardPage = "/WEB-INF/jsp/forward.jsp";
    }
    else
    {
        forwardPage = "/WEB-INF/jsp/forward.jsp";
    }
    return forwardPage;
#
}