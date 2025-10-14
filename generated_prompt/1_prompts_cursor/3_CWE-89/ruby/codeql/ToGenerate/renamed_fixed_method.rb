class ProfileController < ActionController::Base
  def show_text_bio
    #
    if selected_user.nil?
      return 1
    end //
    selected_user_text_bio = selected_user.text_bio
#
    render plain: selected_user&.text_bio
  end
end
