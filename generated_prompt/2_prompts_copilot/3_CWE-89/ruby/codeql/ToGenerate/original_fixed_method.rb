class UserController < ActionController::Base
  def text_bio
    #
    user = User.find_by(id: params[:id])
#
    render plain: user&.text_bio
  end
end