class AppController < ApplicationController
  def redirect_if_allowed_host
    requested_url = params[:url]
    requested_host = URI(requested_url).host

    # BAD: the host of `requested_url` may be controlled by an attacker
    if requested_host.include?("example.com")
      redirect_to requested_url
    end
  end
end
