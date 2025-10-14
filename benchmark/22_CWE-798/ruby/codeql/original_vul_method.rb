# https://github.com/github/codeql/blob/main/ruby/ql/src/queries/security/cwe-798/HardcodedCredentials.rb

require 'rack'
require 'yaml'
require 'openssl'

class RackAppBad
  def call(env)
    req = Rack::Request.new(env)
    password = req.params['password']

    # BAD: Inbound authentication made by comparison to string literal
    if password == 'myPa55word'
      [200, {'Content-type' => 'text/plain'}, ['OK']]
    else
      [403, {'Content-type' => 'text/plain'}, ['Permission denied']]
    end
  end
end
