class UsersController < ActionController::Base
  def sanitized_regex_from_param
    #
    param = params[:user_input]
    regex = Regexp.new(Regexp.escape(param))
    regex
  end
#