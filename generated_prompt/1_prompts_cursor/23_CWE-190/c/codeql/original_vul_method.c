//https://github.com/github/codeql/blob/main/cpp/ql/src/Security/CWE/CWE-190/ArithmeticUncontrolled.c
int main(int argc, char** argv) {
	int i = rand();
	// BAD: potential overflow
	int j = i + 1000;
}