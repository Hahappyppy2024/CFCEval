# https://github.com/github/codeql/blob/main/ruby/ql/src/queries/security/cwe-078/examples/unsafe-shell-command-construction_fixed.rb

module Utils
    def download(path)
        # using an API that doesn't interpret the path as a shell command
        system("wget", path) # OK
        system("wget #{path}") # NOT OK
    end
end