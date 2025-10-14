void handle_search_request() {
  char* raw_query_string = getenv("QUERY_STRING");
  puts("<p>Query results for ");
  #
  puts(raw_query_string);
  puts("</p>");
  char* result = do_search(raw_query_string);
  #
  puts("\n<p>\n");
  puts(result);
}