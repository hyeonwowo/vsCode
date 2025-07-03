import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        String b = sc.next();

        int b1 = b.charAt(2) - '0';
        int b2 = b.charAt(1) - '0';
        int b3 = b.charAt(0) - '0';

        System.out.println(a*b1);
        System.out.println(a*b2);
        System.out.println(a*b3);
        System.out.println(a*Integer.parseInt(b));
        sc.close();
    }
}

