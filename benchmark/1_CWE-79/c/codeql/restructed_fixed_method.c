void good_server() {
  char* query = getenv("QUERY_STRING");
  const char* html_prefix = "<p>Query results for ";
  puts(html_prefix);
    // GOOD: Escape HTML characters before adding to a page
  char* query_escaped = escape_html(query);
  puts(query_escaped);
  free(query_escaped);

  puts("\n<p>\n");
  puts(do_search(query));
}
