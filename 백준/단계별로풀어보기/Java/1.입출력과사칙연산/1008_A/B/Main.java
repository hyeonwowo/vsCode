import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        double a = sc.nextInt(); // 소수점계산시 float, double로 받아주기
        double b = sc.nextInt(); 
        System.out.println(a/b);
        sc.close();
    }
}