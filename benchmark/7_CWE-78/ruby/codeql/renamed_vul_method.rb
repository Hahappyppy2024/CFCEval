module Utils
    def download_file_from_url(file_url)
        system("wget #{file_url}") # NOT OK
    end
end
