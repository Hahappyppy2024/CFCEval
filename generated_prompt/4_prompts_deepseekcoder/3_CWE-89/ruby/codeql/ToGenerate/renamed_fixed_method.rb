class ProfileController < ActionController::Base
  def show_text_bio
    #
    selected_user = User.find_by(id
                                :params[:user_id])

                                if selected_user.nil?
                                  return render plain: "User not found"
#
    render plain: selected_user&.text_bio
  end
end
