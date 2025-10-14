void handle_search_request() {
  char* raw_query_string = getenv("QUERY_STRING");
  puts("<p>Query results for ");

  // GOOD: Escape HTML characters before adding to a page
  char* sanitized_query_string = escape_html(raw_query_string);
  puts(sanitized_query_string);
  free(sanitized_query_string);

  puts("\n<p>\n");
  puts(do_search(raw_query_string));
}
