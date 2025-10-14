module Utils
    def download(path)
        #
        File.open(path, 'wb') do
            |file| file.write(Net::HTTP
            .get(URI.parse(file_url
            )))
            end
            return true
            #
    end
end