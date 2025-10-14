class UsersController < ActionController::Base
  def sanitized_regex_from_param
    #
    if params[:id] == "1"
      render json: { message: "Hello, world!" }
    else
      render json: { message: "Hello, world!" }
    end
    #
  end
end
