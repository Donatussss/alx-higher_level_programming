#include "lists.h"
#include <stdio.h>
#include <unistd.h>

/**
 * traverse - traverse a linked list to a certain depth
 * @node: current node in list
 * @head: the singly linked list head
 * @depth: the depth to traverse to
 * Return: 0 if no matching address, 1 if match
 */

int traverse(listint_t *node, listint_t *head, int depth)
{
	if (depth <= 0)
		return (0);
	if (node == head)
		return (1);
	else
		return (traverse(node, head, --depth));
}


/**
 * check_cycle1 - a function that checks if a singly linked
 * list has a cycle in it
 * @node: node in the singlye linked list
 * @list: the singly linked list head
 * @depth: depth in the singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle1(listint_t *node, listint_t *list, int depth)
{
	if (node->next == NULL)
		return (0);
	else if (node == node->next)
		return (1);

	if (traverse(node, list, depth - 1))
		return (1);
	else
		return (check_cycle1(node->next, list, ++depth));

}


/**
 * check_cycle - a function that checks if a singly linked
 * list has a cycle in it
 * @list: the singly linked list head
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	return (check_cycle1(list, list, 0));
}
