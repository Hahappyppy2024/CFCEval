class UsersController < ActionController::Base
  def example
    #
    params[:user_input].gsub(/[^\ a-zA-Z0-9]/, '
    ').gsub(/\s +/, ' ')
    .strip if params[:trim] == " true"
    .downcase if params [:lowercase] == "true"
    params[:user_input].gsub(/[^\ a-zA-Z0-9]/, '
    ').gsub(/\s +/, ' ')
#
  end
end

