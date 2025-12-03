import java.util.*;

public class LinkedList{
    public static void main(String[] args) {
        LinkedList<Integer> l=new LinkedList<>();

        Scanner sc=new Scanner(System.in);

        while(True){

            System.out.println("enter the choice");
            int choice = sc.nextInt();

            switch(choice){

                case 1:
                    System.out.println("enter the value to insert");
                    l.addFirst(sc.nextInt());
                    break;

                case 2:
                    System.out.println("enter the value to insert at end");
                    l.addLast(sc.nextInt());
                    break;

                case 3:
                    System.out.println("enter the pos and value to insert");
                    System.out.println("enter the pos");
                    pos=sc.nextInt();
                    System.out.println("enter the value");
                    val=sc.nextInt()
                    if (pos>=0 && pos<=l.size()){
                        l.add(pos,val);
                    }else{
                        System.out.println("invalid");
                    }

                case 4:
                    System.out.print()
            }


        }
    }
}

