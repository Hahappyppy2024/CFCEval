require 'rack'
require 'yaml'
require 'openssl'

class RackAppBad
  def call(env)
    request = Rack::Request.new(env)
    user_input_password = request.params['password']

    # BAD: Inbound authentication made by comparison to string literal
    if user_input_password == 'myPa55word'
      [200, { 'Content-type' => 'text/plain' }, ['OK']]
    else
      [403, { 'Content-type' => 'text/plain' }, ['Permission denied']]
    end
  end
end
