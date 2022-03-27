#include <stdio.h>
#include <string.h>

int main() {
	char arr[100];
	char al[26];
	char *p = arr;
	char *q = al;
	int x = 0;

	scanf("%s", arr, 100);

	for (int i = 0; i < 26; i++) {
		*(q+i) = -1;
	}
	for (int i = 'a'; i <= 'z'; i++) {
		for (int j = 0; j < strlen(arr); j++) {
			if (*(p+j) == i) {
				x = *(p + j) - 'a';
				*(q+x) = j;
				break;
			}
		}
	}
	for (int i = 0; i < 26; i++) {
		printf("%d ", *(q+i));
	}
	return 0;
}