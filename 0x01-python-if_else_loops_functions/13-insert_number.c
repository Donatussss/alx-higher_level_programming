#include "lists.h"
#include <stdlib.h>

/**
 * insert_temp - a function that inserts a number
 * into a singly linked list
 * @head: head of the singly linked list
 * @number: number to be added
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_temp(listint_t *head, int number)
{
	listint_t *new;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = head->next;
	head->next = new;

	return (new);
}

/**
 * insert_node_temp - a function that inserts a number into a
 * sorted singly linked list
 * @head: head of the singly linked list
 * @number: new number to be added
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node_temp(listint_t *head, int number)
{
	if (head == NULL)
		return (NULL);

	if (head->next != NULL)
	{
		if (number > (head->next)->n)
			return(insert_node_temp(head->next, number));
	}
	return (insert_temp(head, number));

}


/**
 * insert_node - a function that inserts a number into a
 * sorted singly linked list
 * @head: head of the singly linked list
 * @number: new number to be added
 * Return: the address of the new node, of NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	if (head == NULL)
		return (NULL);
	if (*head == NULL)
		return (add_nodeint_end(&head, number));
	if (number > (*head)->n) return (insert_node_temp(*head, number));
	else if (number < (*head)->n)
	{
		listint_t *new;

		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);
		new->n = number;
		new->next = *head;
		*head = new;
		return (new);
	}
	else
		return (insert_temp(*head, number));
}
