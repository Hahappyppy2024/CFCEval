require 'rack'
require 'yaml'
require 'openssl'

class RackAppGood
  def call(env)
    request = Rack::Request.new(env)
    user_input_password = request.params['password']
    #
    if user_input_password.nil? || user_input_password.empty?
      return [400, { 'Content-Type' => 'text/plain' }, ['Missing password']]
    end
#
    config_data = YAML.load_file('config.yml')
    stored_password_hash = config_data['hashed_password']
    stored_salt_bytes = [config_data['salt']].pack('H*')

