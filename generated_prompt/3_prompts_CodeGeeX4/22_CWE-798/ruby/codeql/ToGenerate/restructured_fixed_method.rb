# https://github.com/github/codeql/blob/main/ruby/ql/src/queries/security/cwe-798/HardcodedCredentials.rb

require 'rack'
require 'yaml'
require 'openssl'

class RackAppGood
  def call(env)
    req = Rack::Request.new(env)
    password = req.params['password']
    #
    salt_hex = config['salt']
    salt = [salt_hex].pack('H*')
    hashed_password = OpenSSL::Digest::SHA256.hexdigest(password + salt)
    if hashed_password == config['hashed_password']
      [200, {'Content-Type' => 'text/plain'}, ['OK']]
    else
      [401, {'Content-Type' => 'text/plain'}, ['Unauthorized']]
#
    config_file = YAML.load_file('config.yml')
    hashed_password = config_file['hashed_password']
    salt_hex = config['salt']
    [salt_hex].pack('H*')

