import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int res = sc.nextInt();
        int n = sc.nextInt();

        int cost = 0;
        int cnt = 0;
        int total = 0;
        for (int i=0; i<n; i++){
            cost = sc.nextInt();
            cnt = sc.nextInt();
            total += (cost * cnt);
        }
        if (total == res)
            System.out.println("Yes");
        else
            System.out.println("No");

        sc.close();
    }
}