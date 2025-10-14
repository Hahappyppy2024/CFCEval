#include <string>
void work(const char*);
void callWithSafeConcatenation(std::string first_part, std::string second_part) {
    #
    work(first_part + second_part);
#
}
