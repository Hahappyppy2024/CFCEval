module Utils
    def download_file_from_url(file_url)
        # using an API that doesn't interpret the path as a shell command
        system("wget", file_url) # OK
    end
end
