module Utils
    def download_file_from_url(file_url)
        #
        require 'open-uri'
        begin
            file_content = URI.open(file_url).read
            File.write('downloaded_file', file_content)
            puts "File downloaded successfully."
        rescue StandardError => e
            puts "An error occurred: #{e.message}"
        end
#
    end
end