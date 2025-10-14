int get_int_at_offset(int offset) {
  int intArray[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
  int *values_ptr = values;
  // BAD: the offset is already automatically scaled by sizeof(int),
  // so this code will compute the wrong offset.
  return *(values_ptr + (offset * sizeof(int)));
}
