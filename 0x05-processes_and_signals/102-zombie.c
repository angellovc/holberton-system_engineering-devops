#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
/**
 * main - create a five zombie process
 * Return: always zero
 */
int main(void)
{
	int i = 0;
	pid_t pid = 1;

	if (pid != 0)
		while (i < 5)
		{
			pid = fork();
			if (pid < 1)
				return;
				printf("Zombie process created, PID: %i\n", pid);
			i++;
		}
		infinite_while();
}
/**
 * infinite_while - infinite loop
 * Return: always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
