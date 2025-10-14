int example2(int i) {
  int intArray[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
  int *intPointer = intArray;
  #
  int result = 0; 
  if (i >= 0 && i < 10) {
    result = intPointer[i];
  } else {
    // Handle out-of-bounds access
    result = -1; // or some other error handling
  }
#
}