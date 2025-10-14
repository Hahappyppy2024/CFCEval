#include <limits.h>
#include <stdlib.h>

int main(int argc, char** argv) {
	int random_base_unsafe = rand();
	// BAD: potential overflow
	int overflow_result = random_base_unsafe + 1000;

}
