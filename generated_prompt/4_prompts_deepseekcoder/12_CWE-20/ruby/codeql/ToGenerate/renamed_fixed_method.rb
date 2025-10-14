class AppController < ApplicationController
  def redirect_if_allowed_host
    requested_url = params[:url]
    requested_host = URI(requested_url).host
    #
    allowed_hosts = ['example.com', '
    example.org']
    if allowed_hosts.include?(requested_host
#
      redirect_to requested_url
    end
  end
end