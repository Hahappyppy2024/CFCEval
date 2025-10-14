int main(int argc, char** argv) {
	int random_base_safe = rand();
	int guarded_result;
	#
	// Ensure random_base_safe is non-negative to avoid undefined behavior in the loop
	if (random_base_safe < 0) {
		random_base_safe = -random_base_safe;
	}
#
}