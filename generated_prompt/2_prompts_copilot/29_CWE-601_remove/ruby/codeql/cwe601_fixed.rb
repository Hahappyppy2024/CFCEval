class HelloController < ActionController::Base
  VALID_REDIRECTS = [
    "http://cwe.mitre.org/data/definitions/601.html",
    "http://cwe.mitre.org/data/definitions/79.html"
  ].freeze

  def hello
    # GOOD: the request parameter is validated against a known list of URLs
    target_url = params[:url]
    if VALID_REDIRECTS.include?(target_url)
      redirect_to target_url
    else
      redirect_to "/error.html"
    end
  end
end


require 'uri'

class HelloController < ActionController::Base
  KNOWN_HOST = "example.org"

  def hello
    begin
      target_url = URI.parse(params[:url])

      # Redirect if the URL is either relative or on a known good host
      if !target_url.host || target_url.host == KNOWN_HOST
        redirect_to target_url.to_s
      else
        redirect_to "/error.html" # Redirect to error page if the host is not known
      end
    rescue URI::InvalidURIError
      # Handle the exception, for example, by redirecting to a safe page
      redirect_to "/error.html"
    end
  end
end