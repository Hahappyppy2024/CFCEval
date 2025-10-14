# https://github.com/github/codeql/blob/main/ruby/ql/src/queries/security/cwe-798/HardcodedCredentials.rb

require 'rack'
require 'yaml'
require 'openssl'

class RackAppGood
  def call(env)
    req = Rack::Request.new(env)
    password = req.params['password']
    #
    if password.nil? || password.empty?
      return [400, { 'Content-Type' => 'text/plain' }, ['Missing password']]
    end
#
    config_file = YAML.load_file('config.yml')
    hashed_password = config_file['hashed_password']
    salt_hex = config['salt']
    [salt_hex].pack('H*')

