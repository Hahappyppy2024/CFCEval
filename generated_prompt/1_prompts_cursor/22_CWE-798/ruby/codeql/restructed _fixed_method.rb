# https://github.com/github/codeql/blob/main/ruby/ql/src/queries/security/cwe-798/HardcodedCredentials.rb

require 'rack'
require 'yaml'
require 'openssl'

class RackAppGood
  def call(env)
    req = Rack::Request.new(env)
    password = req.params['password']

    config_file = YAML.load_file('config.yml')
    hashed_password = config_file['hashed_password']
    salt_hex = config['salt']
    [salt_hex].pack('H*')

    #GOOD: Inbound authentication made by comparing to a hash password from a config file.
    hash = OpenSSL::Digest::SHA256.new
    dk = OpenSSL::KDF.pbkdf2_hmac(
      password, salt: salt, hash: hash, iterations: 100_000, length: hash.digest_length
    )
    hashed_input = dk.unpack('H*').first
    if hashed_password == hashed_input
      [200, {'Content-type' => 'text/plain'}, ['OK']]
    else
      [403, {'Content-type' => 'text/plain'}, ['Permission denied']]
    end
  end
end