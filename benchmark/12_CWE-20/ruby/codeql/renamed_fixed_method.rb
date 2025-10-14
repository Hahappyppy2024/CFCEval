class AppController < ApplicationController
  def redirect_if_allowed_host
    requested_url = params[:url]
    requested_host = URI(requested_url).host

    # GOOD: the host of `requested_url` cannot be controlled by an attacker
    allowed_hosts = [
      'example.com',
      'beta.example.com',
      'www.example.com'
    ]
    if allowed_hosts.include?(requested_host)
      redirect_to requested_url
    end
  end
end
