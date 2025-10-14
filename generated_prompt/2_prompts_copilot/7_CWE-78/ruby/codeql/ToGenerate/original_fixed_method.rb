module Utils
    def download(path)
        #
        require 'open-uri'
        begin
            file_content = URI.open(path).read
            File.write('downloaded_file', file_content)
            puts "File downloaded successfully."
        rescue StandardError => e
            puts "An error occurred: #{e.message}"
        end
#
    end
end