int main(int argc, char** argv) {
	int n = rand();
	int k;
#
	if (n < 0) {	
		k = -n;
	} else {
		k = n;
	}

	return k;
	#
}