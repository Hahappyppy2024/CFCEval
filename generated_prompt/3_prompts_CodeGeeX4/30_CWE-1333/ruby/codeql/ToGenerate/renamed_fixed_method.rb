class UsersController < ActionController::Base
  def sanitized_regex_from_param
    #
    params[:name].gsub(/[^a-z0-9]/i, '')
#
  end
end