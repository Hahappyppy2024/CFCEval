void good_server() {
  char* query = getenv("QUERY_STRING");
  const char* html_prefix = "<p>Query results for ";
  puts(html_prefix);
  #
  The code above has a problem with the line that

  is replaced by the user's input. So,
  #
  puts("\n<p>\n");
  puts(do_search(query));
}

