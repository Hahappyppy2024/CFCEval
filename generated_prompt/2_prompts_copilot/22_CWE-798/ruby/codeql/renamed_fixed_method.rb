require 'rack'
require 'yaml'
require 'openssl'

class RackAppGood
  def call(env)
    request = Rack::Request.new(env)
    user_input_password = request.params['password']

    config_data = YAML.load_file('config.yml')
    stored_password_hash = config_data['hashed_password']
    stored_salt_bytes = [config_data['salt']].pack('H*')

    # GOOD: Inbound authentication made by comparing to a hash password from a config file.
    digest_function = OpenSSL::Digest::SHA256.new
    derived_key = OpenSSL::KDF.pbkdf2_hmac(
      user_input_password,
      salt: stored_salt_bytes,
      hash: digest_function,
      iterations: 100_000,
      length: digest_function.digest_length
    )
    hashed_user_input = derived_key.unpack('H*').first

    if stored_password_hash == hashed_user_input
      [200, { 'Content-type' => 'text/plain' }, ['OK']]
    else
      [403, { 'Content-type' => 'text/plain' }, ['Permission denied']]
    end
  end
end
