#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - it checks if a singly linked list is a palindrome.
 * @head: the head pointer
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head) {
	if (*head == NULL || (*head)->next == NULL) {
		return 1;
	}

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *temp;

	while (fast != NULL && fast->next != NULL) {
		fast = fast->next->next;
		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}

	if (fast != NULL) {
		slow = slow->next;
	}

	while (prev != NULL && slow != NULL) {
		if (prev->n != slow->n) {
			return 0;
		}
		prev = prev->next;
		slow = slow->next;
	}

	return 1;
}

void print_list(listint_t *head) {
	listint_t *current = head;
	while (current != NULL) {
		printf("%d -> ", current->n);
		current = current->next;
	}
	printf("NULL\n");
}
