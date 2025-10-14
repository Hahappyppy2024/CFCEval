class ProfileController < ActionController::Base
  def show_text_bio
    #
    selected_user = User.find_by(id: params[:id])
#
    render plain: selected_user&.text_bio
  end
end
