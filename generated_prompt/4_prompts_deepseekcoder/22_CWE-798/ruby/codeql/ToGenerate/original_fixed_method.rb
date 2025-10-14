require 'rack'
require 'yaml'
require 'openssl'

class RackAppGood
  def call(env)
    req = Rack::Request.new(env)
    password = req.params['password']
    #
    if password && valid_credentials?(password)
      [200, {'Content-Type'
      => 'text/plain'}, ['Valid credentials']]
      else
      [401, {'Content-Type
      => 'text/plain'}, ['Unauthorized']]
      end
      end
#

    config_file = YAML.load_file('config.yml')
    hashed_password = config_file['hashed_password']
    salt = [config_file['salt']].pack('H*')

