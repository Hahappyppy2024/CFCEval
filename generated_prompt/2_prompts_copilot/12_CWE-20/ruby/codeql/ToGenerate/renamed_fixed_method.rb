class AppController < ApplicationController
  def redirect_if_allowed_host
    requested_url = params[:url]
    requested_host = URI(requested_url).host
    #
    if requested_host.nil? || requested_host.empty?
      flash[:error] = "Invalid URL"
#
      redirect_to requested_url
    end
  end
end