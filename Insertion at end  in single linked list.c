#include<stdio.h>
#include<stdlib.h>
struct Node{
	int data;
	struct Node* next;
};
struct Node* add_at_end(struct Node* head,int data){
	struct Node *ptr,*temp;
	ptr=head;
	temp=malloc(sizeof(struct Node));
	temp->data=data;
	temp->next=NULL;
	while(ptr->next!=NULL){
		ptr=ptr->next;
	}
	ptr->next=temp;
	return head;
}
int main(){
	struct Node* head=malloc(sizeof(struct Node));
	head->data=34;
	head->next=NULL;
	int data=3;
	head=add_at_end(head,data);
	while(head!=NULL){
		printf("%d ->",head->data);
		head=head->next;
	}
	printf("NULL");
	return 0;
}
