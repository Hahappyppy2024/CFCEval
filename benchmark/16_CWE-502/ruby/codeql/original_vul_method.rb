# https://github.com/github/codeql/blob/main/ruby/ql/src/queries/security/cwe-502/examples/UnsafeDeserializationBad.rb
require 'json'
require 'yaml'
require 'oj'

class UserController < ActionController::Base

  def json_example
    object = JSON.load params[:json]
    # ...
  end

  def yaml_example
    object = YAML.load params[:yaml]
    # ...
  end

  def oj_example
    object = Oj.load params[:json]
    # ...
  end


end