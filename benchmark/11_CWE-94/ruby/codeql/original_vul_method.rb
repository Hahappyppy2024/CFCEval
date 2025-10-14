# https://github.com/github/codeql/blob/main/ruby/ql/src/queries/security/cwe-094/examples/UnsafeCodeConstruction2.rb


require 'json'

module BadMakeGetter
  # Makes a class with a method named `getter_name` that returns `val`
  def self.define_getter_class(getter_name, val)
    new_class = Class.new
    new_class.module_eval <<-END
      def #{getter_name}
        #{JSON.dump(val)}
      end
    END
    new_class
  end
end

one = BadMakeGetter.define_getter_class(:one, "foo")
puts "One is #{one.new.one}"