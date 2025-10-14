class UsersController < ActionController::Base
  def example
    # GOOD: User input is sanitized before constructing the regular expression
    regex = Regexp.new(Regex.escape(params[:key]))
  end
end




# class UsersController < ActionController::Base
#   def first_example
#     # BAD: Unsanitized user input is used to construct a regular expression
#     regex = /#{ params[:key] }/
#   end

#   def second_example
#     # BAD: Unsanitized user input is used to construct a regular expression
#     regex = Regexp.new(params[:key])
#   end
# end