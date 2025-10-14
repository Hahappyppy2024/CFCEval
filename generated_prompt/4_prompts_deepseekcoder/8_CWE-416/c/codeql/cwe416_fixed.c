//https://github.com/github/codeql/blob/main/cpp/ql/src/Security/CWE/CWE-416/UseOfStringAfterLifetimeEndsGood.cpp

#include <string>
void work(const char*);

// GOOD: the concatenated string outlives the call to `work`. So the pointer
// obtainted from `c_str` is valid.
void work_with_combined_string_good(std::string s1, std::string s2) {
  auto combined_string = s1 + s2;
  work(combined_string.c_str());
}


//#include <string>
//void work(const char*);
//
//// BAD: the concatenated string is deallocated when `c_str` returns. So `work`
//// is given a pointer to invalid memory.
//void work_with_combined_string_bad(std::string s1, std::string s2) {
//  const char* combined_string = (s1 + s2).c_str();
//  work(combined_string);
//}