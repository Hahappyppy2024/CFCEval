class ProfileController < ActionController::Base
  def show_text_bio
    # GOOD -- Using a hash to parameterize arguments
    selected_user = User.find_by name: params[:user_name]
    render plain: selected_user&.text_bio
  end
end
