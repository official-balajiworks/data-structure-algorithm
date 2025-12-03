import java.util.*;

public class LinkedListOperations {
    public static void main(String[] args) {

        LinkedList<Integer> list = new LinkedList<>();
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("\n--- Single Linked List Operations ---");
            System.out.println("1. Insert at Beginning");
            System.out.println("2. Insert at End");
            System.out.println("3. Insert at Position");
            System.out.println("4. Delete by Value");
            System.out.println("5. Display List");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");

            int choice = sc.nextInt();

            switch (choice) {

                case 1:
                    System.out.print("Enter value to insert at beginning: ");
                    int val1 = sc.nextInt();
                    list.addFirst(val1);
                    break;

                case 2:
                    System.out.print("Enter value to insert at end: ");
                    int val2 = sc.nextInt();
                    list.addLast(val2);
                    break;

                case 3:
                    System.out.print("Enter position (0-based index): ");
                    int pos = sc.nextInt();
                    System.out.print("Enter value to insert: ");
                    int val3 = sc.nextInt();

                    if (pos >= 0 && pos <= list.size()) {
                        list.add(pos, val3);
                    } else {
                        System.out.println("Invalid position!");
                    }
                    break;

                case 4:
                    System.out.print("Enter value to delete: ");
                    int val4 = sc.nextInt();

                    if (list.remove((Integer) val4)) {
                        System.out.println("Value deleted.");
                    } else {
                        System.out.println("Value not found!");
                    }
                    break;

                case 5:
                    System.out.println("Current Linked List: " + list);
                    break;

                case 6:
                    System.out.println("Exiting...");
                    sc.close();
                    return;

                default:
                    System.out.println("Invalid choice! Try again.");
            }
        }
    }
}
