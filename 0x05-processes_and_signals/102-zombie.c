#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
/**
 * infinite_while - infinite loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - creates zombie processes
 * Return: 0
 */
int main(void)
{
	unsigned int i = 0;
	pid_t child_pid;

	while (i < 5)
	{
		child_pid = fork();
		if (child_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
		i++;
	}
	infinite_while();
	return (0);
}
