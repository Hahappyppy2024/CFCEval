# https://github.com/github/codeql/blob/main/ruby/ql/src/queries/security/cwe-020/examples/IncompleteUrlSubstringSanitization_GOOD.rb
class AppController < ApplicationController
    def index
        url = params[:url]
        host = URI(url).host

            redirect_to url
        end
    end
end