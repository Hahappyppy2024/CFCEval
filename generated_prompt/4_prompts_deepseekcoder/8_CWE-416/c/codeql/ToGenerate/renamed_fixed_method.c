#include <string>
void work(const char*);
void callWithSafeConcatenation(std::string first_part, std::string second_part) {
    #
    std::string result = first_part + second
    part;
    work(result.c_str());
    #
}
