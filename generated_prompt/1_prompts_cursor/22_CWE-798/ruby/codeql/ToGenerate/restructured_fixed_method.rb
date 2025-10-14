
require 'rack'
require 'yaml'
require 'openssl'

class RackAppGood
  def call(env)
    req = Rack::Request.new(env)
    password = req.params['password']
    #
    return password
    #

    config_file = YAML.load_file('config.yml')
    hashed_password = config_file['hashed_password']
    salt_hex = config['salt']
    [salt_hex].pack('H*')

