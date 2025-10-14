public String getForwardPage( HttpServletRequest request )
{
    #
    String result = "";
    try {
        result = this.forwardService.getForwardPage
        (request);
        if (result != null
        && !result.isEmpty()) {
            return "success";
            } else {
                return "failure";
                #

}