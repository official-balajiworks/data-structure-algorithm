import java.util.*;

public class QueueExample {
    public static void main(String[] args) {

        java.util.Queue<Integer> queue = new java.util.LinkedList<>();
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("\n--- QUEUE OPERATIONS ---");
            System.out.println("1. Enqueue");
            System.out.println("2. Dequeue");
            System.out.println("3. Peek (Front)");
            System.out.println("4. Display");
            System.out.println("5. Rear (Last Element)");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");

            int choice = Integer.parseInt(sc.nextLine());

            switch (choice) {
                case 1:
                    System.out.print("Enter value to enqueue: ");
                    int val = Integer.parseInt(sc.nextLine());
                    queue.add(val);
                    System.out.println(val + " added to queue");
                    break;

                case 2:
                    if (!queue.isEmpty())
                        System.out.println("Dequeued: " + queue.remove());
                    else
                        System.out.println("Queue is empty!");
                    break;

                case 3:
                    if (!queue.isEmpty())
                        System.out.println("Front: " + queue.peek());
                    else
                        System.out.println("Queue is empty!");
                    break;

                case 4:
                    System.out.println("Queue: " + queue);
                    break;

                case 5:
                    if (!queue.isEmpty())
                        System.out.println("Rear: " + ((java.util.LinkedList<Integer>) queue).getLast());
                    else
                        System.out.println("Queue is empty!");
                    break;

                case 6:
                    System.out.println("Exiting...");
                    return;

                default:
                    System.out.println("Invalid choice!");
            }
        }
    }
}
