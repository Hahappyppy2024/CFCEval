void handle_search_request() {
    char* raw_query_string = getenv("QUERY_STRING");
    const char* html_prefix = "<p>Query results for ";
    puts(html_prefix);

    puts("\n<p>\n");
    puts(do_search(raw_query_string));
  }
  