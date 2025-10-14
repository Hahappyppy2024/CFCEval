class UsersController < ActionController::Base
  def sanitized_regex_from_param
    #
    params[:user_input].gsub(/[^\ a-zA-Z0-9]/, '')
    params[:user_input].gsub(/\s +/, ' ')
    params[:user_input].strip if params[:trim] == "true"
    params[:user_input].downcase if params[:lowercase] == "true
    #
  end
end

