#include<stdio.h>
#include<stdlib.h>
struct Node{
	int data;
	struct Node* next;
};
struct Node* add_beg(struct Node* head,int data){
	struct Node* ptr=malloc(sizeof(struct Node));
	ptr->data=data;
	ptr->next=head;
	head=ptr;
	return head;
}
int main(){
	struct Node* head=malloc(sizeof(struct Node));
	head->data=34;
	head->next=NULL;
	int data=3;
	head=add_beg(head,data);
	while(head!=NULL){
		printf("%d ->",head->data);
		head=head->next;
	}
	printf("NULL");
	return 0;
}
