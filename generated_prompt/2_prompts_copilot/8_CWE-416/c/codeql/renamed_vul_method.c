#include <string>
void processInput(const char*);

// BAD: the concatenated string is deallocated when `c_str` returns. So `processInput`
// is given a pointer to invalid memory.
void callWithUnsafeConcatenation(std::string first_part, std::string second_part) {
  const char* concatenated_string = (first_part + second_part).c_str();
  processInput(concatenated_string);
}
