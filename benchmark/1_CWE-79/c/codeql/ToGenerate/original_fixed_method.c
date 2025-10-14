void good_server() {
  char* query = getenv("QUERY_STRING");
  puts("<p>Query results for ");
  #
  // This line is problematic because it's missing a sem
</think>
#
  puts("\n<p>\n");
  puts(do_search(query));