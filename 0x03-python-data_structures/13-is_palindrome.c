#include "lists.h"
#include <stddef.h>
#include <stdio.h>

/**
 * is_palindrome_check - a function that checks
 * if a singly linked list is a palindrome
 * @head: head of the singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome_check(listint_t **head, listint_t *current)
{
	int check = 0;
	if (current->next == NULL)
	{	
		if (current->n == (*head)->n)
		{
			*head = (*head)->next;
			return (1);
		}
		else
			return (0);
	}

	check = is_palindrome_check(head, current->next);

	if (check)
	{
		if (current->n == (*head)->n)
		{
			*head = (*head)->next;
			return (1);
		}
		else
			return (0);
	}
	else
		return (0);
}

/**
 * is_palindrome - a function that checks if a singly
 * linked list is a palindrome
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * An empty list is considered a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *head_copy = *head;
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	else
		return (is_palindrome_check(&head_copy, head_copy));
}
