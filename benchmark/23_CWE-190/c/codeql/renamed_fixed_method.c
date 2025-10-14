#include <limits.h>
#include <stdlib.h>

int main(int argc, char** argv) {
	int random_base_safe = rand();
	int guarded_result;
	// GOOD: use a guard to prevent overflow
	if (random_base_safe < INT_MAX - 1000)
		guarded_result = random_base_safe + 1000;
	else
		guarded_result = INT_MAX;
}
