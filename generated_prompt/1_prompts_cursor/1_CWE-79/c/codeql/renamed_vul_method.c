void handle_search_request_unsanitized() {
  char* raw_query_string = getenv("QUERY_STRING");
  puts("<p>Query results for ");

  // BAD: Printing out an HTTP parameter with no escaping
  puts(raw_query_string);

  puts("\n<p>\n");
  puts(do_search(raw_query_string));
}
