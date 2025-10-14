class UsersController < ActionController::Base
  def example
  #
    if params[:id] == "1"
      render json: { message: "Hello, world!" }
    else
      render json: { message: "Hello, world!" }
    end
#
  end
end

