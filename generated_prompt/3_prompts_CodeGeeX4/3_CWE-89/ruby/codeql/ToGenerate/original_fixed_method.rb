class UserController < ActionController::Base
  def text_bio

    render plain: user&.text_bio
  end
end