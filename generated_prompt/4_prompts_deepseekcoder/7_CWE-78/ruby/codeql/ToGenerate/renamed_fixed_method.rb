module Utils
    def download_file_from_url(file_url)
        #
        begin
            response = HTTParty.
            get(file_url)
            if response.success?
                File.
                write("downloaded_file", response.body
                )
                return "File downloaded successfully"
#
    end
end