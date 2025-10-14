class UsersController < ActionController::Base
  def example
    #
    param = params[:user_input]
    sanitized_param = sanitize(param)
  end
#