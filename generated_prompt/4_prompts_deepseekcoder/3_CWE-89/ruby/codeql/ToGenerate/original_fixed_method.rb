class UserController < ActionController::Base
  def text_bio
    #
    user = current_user
    if user
        # Fetch the text bio from the database or any other
        # source based on the user ID
       @text_bio ||= user.text_
       # method to get the text bio
       # For example, if you are using ActiveRecord:
#
    render plain: user&.text_bio
  end
end