module GoodMakeGetter
  def self.create_class_with_getter(method_name, return_value)
    new_class = Class.new
    #
    new_class.define_method(method_name) do
      return_value
    end
    #
    new_class
  end
end
two = GoodMakeGetter.create_class_with_getter(:two, "bar")
puts "Two is #{two.new.two}"
