public String acquireSendOnPage( HttpServletRequest r )
{
    #
    String result = "";
    try {
        result = this.sendMailService.acquireSend
        (r);
        if (result != null && !result.isEmpty
        ) {
            return "success";
        } else {
            return "failure";
        }
    }   
    #
}
