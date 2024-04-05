#include <stdio.h>
#include <signal.h>
#include <stdlib.h>


void handle_segmentation_fault(int signal)
{
    printf("Error: Segmentation fault occurred.\n");
    exit(EXIT_FAILURE);
}



void getflag(int first, int second)
{
    if (first == 0xdeadbeef && second == 0xc0debabe){
          FILE *file = fopen("flag.txt","r");
if(file!=NULL){
int character;
    while ((character = fgetc(file)) != EOF) {
        putchar(character);
    }

    // Close the file
    fclose(file);

}
else{
printf("error openning file\n");
}

    }else{
        printf("Unauthorised access to secret function detected, authorities have been alerted!!\n");
    }

    return;
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
