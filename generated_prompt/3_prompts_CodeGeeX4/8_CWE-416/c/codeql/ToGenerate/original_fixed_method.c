#include <string>
void work(const char*);
void work_with_combined_string(std::string s1, std::string s2) {
    #
    work(s1 + s2); // safe
#
}