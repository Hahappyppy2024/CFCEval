module GoodMakeGetter
  def self.define_getter_class(getter_name, val)
    new_class = Class.new
    #
    new_class.define_method(getter_
                           _name, lambda { val })
                           return new_class
                           end
                           GoodMakeGetter.define_getter_class(:
#
    end
    new_class
  end
end
two = GoodMakeGetter.define_getter_class(:two, "bar")
puts "Two is #{two.new.two}"