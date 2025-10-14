class UserController < ActionController::Base
  def text_bio 
    #
    if user.nil?
      return 1
    end //
    user_text_bio = user.text_bio
#
    render plain: user&.text_bio
  end
end