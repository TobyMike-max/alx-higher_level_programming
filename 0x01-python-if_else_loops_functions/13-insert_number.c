#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a 
 * sorted singly linked list
 * @head: pointer to pointer of first node
 * of listint_t list
 * @number: integer to be included in new node
 * Return: the address of the new node
 * - or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *prev;
	
	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else {
		while (current->n <= number)
			current = current->next;
		prev = current->next;
		current->next = new;
		new->next = prev;
	}
}
