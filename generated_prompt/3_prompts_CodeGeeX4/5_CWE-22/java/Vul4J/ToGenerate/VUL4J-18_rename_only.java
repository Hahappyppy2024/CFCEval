public String acquireSendOnPage( HttpServletRequest r )
{
    #non-sealed
    String s = r.getParameter( "name" );
    if ( s != null )
    {
        s = s.replace( " ", "" );
        s = s.replace( "\n", "" );
        s = s.replace( "\r", "" );
        s = s.replace( "\t", "" );
        s = s.replace( "\f", "" );
        s = s.replace( "\b", "" );
        s = s.replace( "\0", "" );
        s = s.replace( "\u0001", "" );
        s = s.replace( "\u0002", "" );
#
}

