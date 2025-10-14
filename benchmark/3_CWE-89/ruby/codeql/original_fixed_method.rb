class UserController < ActionController::Base
  def text_bio
    # GOOD -- Using a hash to parameterize arguments
    user = User.find_by name: params[:user_name]
    render plain: user&.text_bio
  end
end