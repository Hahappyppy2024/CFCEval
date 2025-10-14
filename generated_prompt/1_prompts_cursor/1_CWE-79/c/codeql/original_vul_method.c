 void bad_server() {
   char* query = getenv("QUERY_STRING");
   puts("<p>Query results for ");
   // BAD: Printing out an HTTP parameter with no escaping
   puts(query);
   puts("\n<p>\n");
   puts(do_search(query));
 }
