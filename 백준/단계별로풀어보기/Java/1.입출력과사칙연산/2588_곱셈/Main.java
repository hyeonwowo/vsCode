import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        // 숫자 -> 문자열 분리 -> 숫자로 다시 변환
        // 수학적 방법 사용 (몫과 나머지)
        System.out.println();
        System.out.println();
        System.out.println();
        System.out.println(a*b);
        sc.close();
    }
}