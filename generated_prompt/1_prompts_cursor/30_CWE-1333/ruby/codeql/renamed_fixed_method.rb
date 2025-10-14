class UsersController < ActionController::Base
  def sanitized_regex_from_param
    # GOOD: User input is sanitized before constructing the regular expression
    sanitized_regex = Regexp.new(Regexp.escape(params[:key]))
  end
end
