int get_int_at_offset(int offset) {
  int values[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
  int *values_ptr = values;
  #
  int result = 0;
  if (offset >= 0 && offset < 10) {
    result = values_ptr[offset];
  } else {
    // Handle out-of-bounds access
    result = -1; // or some other error handling
  }
  return result;
#
}