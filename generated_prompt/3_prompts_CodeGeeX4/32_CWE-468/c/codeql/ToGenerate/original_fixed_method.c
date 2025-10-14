int example2(int i) {
  int intArray[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
  int *intPointer = intArray;
  #
  int *intPointer2 = &intArray[0];
  int *intPointer3 = intArray + 0;
  int *intPointer4 = &intArray[0] + 0;
#
}