int main(int argc, char** argv) {
	int random_base_safe = rand();
	int guarded_result;
#
	if (random_base_safe < 0) {
		guarded_result = -random_base_safe;
	} else {
		guarded_result = random_base_safe;
	}

	return guarded_result;
	#
}