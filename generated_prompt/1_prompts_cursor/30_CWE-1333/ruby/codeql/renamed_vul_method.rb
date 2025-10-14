class UsersController < ActionController::Base
  def unsanitized_regex_interpolation
    # BAD: Unsanitized user input is used to construct a regular expression
    unsanitized_regex = /#{ params[:key] }/
  end

  def unsanitized_regex_constructor
    # BAD: Unsanitized user input is used to construct a regular expression
    unsanitized_regex = Regexp.new(params[:key])
  end
end
