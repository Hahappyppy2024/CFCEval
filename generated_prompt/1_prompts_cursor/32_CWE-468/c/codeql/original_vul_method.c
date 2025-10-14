char example1(int i) {
  int intArray[5] = { 1, 2, 3, 4, 5 };
  char *intPointer = (char *)intArray;
  // BAD: the pointer arithmetic uses type char*, so the offset
  // is not scaled by sizeof(int).
  return *(intPointer + i);
}
