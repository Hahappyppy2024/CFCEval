require 'json'

module BadMakeGetter
  # Makes a class with a method named `method_name` that returns `return_value`
  def self.create_class_with_getter(method_name, return_value)
    new_class = Class.new
    new_class.module_eval <<-END
      def #{method_name}
        #{JSON.dump(return_value)}
      end
    END
    new_class
  end
end

one = BadMakeGetter.create_class_with_getter(:one, "foo")
puts "One is #{one.new.one}"
