class AppController < ApplicationController
    def index
        url = params[:url]
        host = URI(url).host
        #
        if host.nil? || host.empty?
            flash[:error] = "Invalid URL"
#
            redirect_to url
        end
    end
end