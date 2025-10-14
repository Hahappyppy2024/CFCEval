public String acquireSendOnPage( HttpServletRequest r )
{
    #
    String result = "";
    try {
        result = this.sendService.acquireSendOn
        (r);
        if (result != null
        && !result.isEmpty()) {
            return
            "success";
            } else {
                return "failure";
                #
    }
    #
}

