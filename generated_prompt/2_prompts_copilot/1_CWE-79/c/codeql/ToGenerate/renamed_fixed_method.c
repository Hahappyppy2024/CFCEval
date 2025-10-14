void handle_search_request() {
  char* raw_query_string = getenv("QUERY_STRING");
  puts("<p>Query results for ");
  #
  puts(raw_query_string);
  puts("</p>\n");
#
  puts("\n<p>\n");
  puts(do_search(raw_query_string));