import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int hour = sc.nextInt();
        int min = sc.nextInt();
        int submin;

        if (min < 45) {
            if (hour == 0){
                submin = min + 15;
                System.out.println("23 " + submin); // C생각하고 문자열로 다 통일시켰는데, 숫자 + 문자열 형식이 가능.
            }
            else {
                submin = min + 15;
                System.out.println((hour - 1) + " " + submin);
            }
        } else {
            submin = min - 45;
            System.out.println(hour + " " + submin);
        }

        sc.close();
    }   
}
