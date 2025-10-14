class HelloController < ActionController::Base
  ALLOWED_REDIRECT_URLS = [
    "http://cwe.mitre.org/data/definitions/601.html",
    "http://cwe.mitre.org/data/definitions/79.html"
  ].freeze

  def hello
    # GOOD: the request parameter is validated against a known list of URLs
    requested_url_param = params[:url]
    if ALLOWED_REDIRECT_URLS.include?(requested_url_param)
      redirect_to requested_url_param
    else
      redirect_to "/error.html"
    end
  end
end
