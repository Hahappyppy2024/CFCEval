void good_server() {
  char* query = getenv("QUERY_STRING");
  puts("<p>Query results for ");
  #
  // GOOD: Escaping the HTTP parameter
  puts(html_escape(query));
  puts(query);
#
  puts("\n<p>\n");
  puts(do_search(query));