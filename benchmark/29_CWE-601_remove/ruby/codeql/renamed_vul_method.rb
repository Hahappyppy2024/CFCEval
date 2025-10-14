require 'uri'

class HelloController < ActionController::Base
  ALLOWED_REDIRECT_HOST = "example.org"

  def hello
    begin
      requested_url_param = URI.parse(params[:url])

      # Redirect if the URL is either relative or on a known good host
      if !requested_url_param.host || requested_url_param.host == ALLOWED_REDIRECT_HOST
        redirect_to requested_url_param.to_s
      else
        redirect_to "/error.html" # Redirect to error page if the host is not known
      end
    rescue URI::InvalidURIError
      # Handle the exception, for example, by redirecting to a safe page
      redirect_to "/error.html"
    end
  end
end
