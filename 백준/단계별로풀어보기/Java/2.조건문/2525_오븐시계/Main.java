import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int hour = sc.nextInt();
        int min = sc.nextInt();
        int min2 = sc.nextInt();
        int min3 = min + min2;
        int addhour;

        if (min3 >= 60){
            addhour = min3 / 60;
            hour += addhour;
            min3 -= 60 * addhour;
        }

        hour %= 24; // 24시 넘어가면 0부터 다시 시작
        System.out.println(hour + " " + min3);
        sc.close();
    }
}
