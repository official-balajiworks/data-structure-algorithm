import java.util.LinkedList;
import java.util.Scanner;

public class DoublyLinkedListBuiltin {
    public static void main(String[] args) {

        LinkedList<Integer> dll = new LinkedList<>();  // built-in doubly linked list
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("\n---- DOUBLY LINKED LIST MENU ----");
            System.out.println("1. Insert at Beginning");
            System.out.println("2. Insert at End");
            System.out.println("3. Insert at Position");
            System.out.println("4. Delete First");
            System.out.println("5. Delete Last");
            System.out.println("6. Delete at Position");
            System.out.println("7. Display Forward");
            System.out.println("8. Display Reverse");
            System.out.println("9. Exit");
            System.out.print("Enter your choice: ");

            int choice = sc.nextInt();

            switch (choice) {

                case 1:
                    System.out.print("Enter value: ");
                    dll.addFirst(sc.nextInt());
                    break;

                case 2:
                    System.out.print("Enter value: ");
                    dll.addLast(sc.nextInt());
                    break;

                case 3:
                    System.out.print("Enter position: ");
                    int pos = sc.nextInt();
                    System.out.print("Enter value: ");
                    int val = sc.nextInt();
                    if (pos >= 0 && pos <= dll.size())
                        dll.add(pos, val);
                    else
                        System.out.println("Invalid Position!");
                    break;

                case 4:
                    if (!dll.isEmpty())
                        System.out.println("Deleted: " + dll.removeFirst());
                    else
                        System.out.println("List is Empty!");
                    break;

                case 5:
                    if (!dll.isEmpty())
                        System.out.println("Deleted: " + dll.removeLast());
                    else
                        System.out.println("List is Empty!");
                    break;

                case 6:
                    System.out.print("Enter position: ");
                    int p = sc.nextInt();
                    if (p >= 0 && p < dll.size())
                        System.out.println("Deleted: " + dll.remove(p));
                    else
                        System.out.println("Invalid Position!");
                    break;

                case 7:
                    System.out.println("List (Forward): " + dll);
                    break;

                case 8:
                    System.out.print("List (Reverse): ");
                    for (int i = dll.size() - 1; i >= 0; i--)
                        System.out.print(dll.get(i) + " ");
                    System.out.println();
                    break;

                case 9:
                    System.out.println("Exiting...");
                    return;

                default:
                    System.out.println("Invalid Choice!");
            }
        }
    }
}
