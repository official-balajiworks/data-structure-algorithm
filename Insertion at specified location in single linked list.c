#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

// Insert at a given position
void add_at_pos(struct Node *head, int data, int pos) {
    struct Node *ptr = head;
    struct Node *ptr2 = malloc(sizeof(struct Node));
    ptr2->data = data;
    ptr2->next = NULL;

    pos--; // move to previous node of given pos
    while (pos != 1 ) {
        ptr = ptr->next;
        pos--;
    }

    ptr2->next = ptr->next;
    ptr->next = ptr2;
}

int main() {
    // Create first node
    struct Node *head = malloc(sizeof(struct Node));
    head->data = 45;
    head->next = NULL;

    // Add new node at position 2
    int data = 3, position = 2;
    add_at_pos(head, data, position);

    // Print linked list
    while (head!= NULL) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");

    return 0;
}

