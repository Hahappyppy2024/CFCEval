#include <string>
void work(const char*);

// GOOD: the concatenated string outlives the call to `processInput`. So the pointer
// obtained from `c_str` is valid.
void callWithSafeConcatenation(std::string first_part, std::string second_part) {
  auto concatenated_string = first_part + second_part;
  work(concatenated_string.c_str());
}
