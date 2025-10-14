class ProfileController < ActionController::Base
  def show_text_bio

    render plain: selected_user&.text_bio
  end
end
