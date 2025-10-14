class HelloController < ActionController::Base
  ALLOWED_REDIRECT_URLS = [
    "http://cwe.mitre.org/data/definitions/601.html",
    "http://cwe.mitre.org/data/definitions/79.html"
  ].freeze

  def hello
