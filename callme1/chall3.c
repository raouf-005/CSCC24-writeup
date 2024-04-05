#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

void handle_segmentation_fault(int signal)
{
    printf("Error: Segmentation fault occurred.\n");
    exit(EXIT_FAILURE);
}

void getflag()
{
    FILE *file = fopen("flag.txt", "r");
    if (file != NULL) {
        int character;
        while ((character = fgetc(file)) != EOF) {
            putchar(character);
        }

        // Close the file
        fclose(file);
    } else {
        printf("Error: Unable to open flag file.\n");
    }
}

void register_name()
{
      char buffer[16];

    printf("Name:\n");
    scanf("%s", buffer);
    printf("Hi there, %s\n", buffer); 
}

int main()
{
    // Set up signal handler for segmentation fault
    signal(SIGSEGV, handle_segmentation_fault);

    register_name();
    return 0;
}
