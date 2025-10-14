require 'json'
require 'yaml'
require 'oj'

class UserController < ActionController::Base

  def parse_user_from_json
    user_data = JSON.load params[:json]
    # ...
  end

  def parse_user_from_yaml
    user_data = YAML.load params[:yaml]
    # ...
  end

  def parse_user_from_oj
    user_data = Oj.load params[:json]
    # ...
  end

end
