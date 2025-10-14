void good_server() {
  char* query = getenv("QUERY_STRING");
  puts("<p>Query results for ");
  #
  puts(query);
  puts("\n<p>\n");
  puts(do_search(query));
#
  puts("\n<p>\n");
  puts(do_search(query));