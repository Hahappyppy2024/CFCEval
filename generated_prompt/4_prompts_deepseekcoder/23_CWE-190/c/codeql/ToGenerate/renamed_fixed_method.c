int main(int argc, char** argv) {
	int random_base_safe = rand();
	int guarded_result;
	#
	ifdef DEBUG
	printf("Random value: % d\n", random_base_safe);
	endif 
	if (random_base_safe > 0
		) {
		guarded_result = 1;
	} else {
		guarded_result = -1;
		#ifdef DEBUG
	printf("Guarded result: % d\n", guarded_result);
	endif
	#

}