#include <string>
void work(const char*);
void work_with_combined_string(std::string s1, std::string s2) {
    #
    std::string result = s1 + s2;
    work(result.c_str());
    #
}