#include <stdio.h>

// argc = #words in cmd call
// argv = array of those words
int main(int argc, char** argv){
        
        printf("Called with \"%s\".\n",argv[0]);
        
        if(argc > 1){
                for(int i=1;i<argc;i++){
                        printf("argv[%d] = %s\n", i, argv[i]);
                }
        }else{
                printf("No additional arguments.\n");
        }

        return 0;
}
