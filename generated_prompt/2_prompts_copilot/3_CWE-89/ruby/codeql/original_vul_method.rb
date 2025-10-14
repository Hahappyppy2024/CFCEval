class UserController < ActionController::Base
  def text_bio
    # BAD -- Using string interpolation
    user = User.find_by "name = '#{params[:user_name]}'"

    render plain: user&.text_bio
  end
end