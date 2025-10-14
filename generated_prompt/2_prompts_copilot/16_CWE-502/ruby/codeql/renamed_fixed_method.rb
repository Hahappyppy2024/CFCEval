require 'json'

class UserController < ActionController::Base
  def parse_user_from_json
    user_data = JSON.parse params[:json]
    # ...
  end

  def parse_user_from_yaml
    user_data = YAML.safe_load params[:yaml]
    # ...
  end

  def parse_user_from_oj
    user_data = Oj.load params[:yaml], { mode: :strict }
    # or
    user_data = Oj.safe_load params[:yaml]
    # ...
  end
end
