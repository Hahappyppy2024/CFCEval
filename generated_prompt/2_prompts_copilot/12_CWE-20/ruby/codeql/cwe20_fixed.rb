# https://github.com/github/codeql/blob/main/ruby/ql/src/queries/security/cwe-020/examples/IncompleteUrlSubstringSanitization_GOOD.rb
class AppController < ApplicationController
    def index
        url = params[:url]
        host = URI(url).host
        # GOOD: the host of `url` can not be controlled by an attacker
        allowedHosts = [
            'example.com',
            'beta.example.com',
            'www.example.com'
        ]
        if allowedHosts.include?(host)
            redirect_to url
        end
    end
end




class AppController < ApplicationController
    def index
        url = params[:url]
        host = URI(url).host
        # BAD: the host of `url` may be controlled by an attacker
        if host.include?("example.com")
            redirect_to url
        end
    end
end