class AppController < ApplicationController
    def index
        url = params[:url]
        host = URI(url).host

            redirect_to url
        end
    end
end