#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <fcntl.h>

int main(){

    int fd;
    fd = open("/tmp/zzz",O_RDWR|O_APPEND);
    sleep(1);
    setuid(getuid());
    pid_t pid ;

    if( ( pid = fork() ) < 0 )
        perror("fork error");
    else if( pid == 0 ){
        // child process
        write( fd , "shiyanlou!" , 10 );
    }

    int status=waitpid(pid,0,0);
    close(fd);

    return 0;
}