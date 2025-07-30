import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) { 
                System.out.print("*"); // println -> print (연속해서 출력)
            }
            System.out.println();
        }

        sc.close();
    }
}
