//https://github.com/github/codeql/blob/main/cpp/ql/src/Security/CWE/CWE-190/ArithmeticUncontrolled.c
int main(int argc, char** argv) {
	int n = rand();
	int k;
	// GOOD: use a guard to prevent overflow
	if (n < INT_MAX-1000)
		k = n + 1000;
	else
		k = INT_MAX;
}