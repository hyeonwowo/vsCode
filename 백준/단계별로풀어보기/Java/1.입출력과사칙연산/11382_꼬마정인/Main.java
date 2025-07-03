import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong(); // int -> long, nextInt() -> nextLong()
        long b = sc.nextLong();
        long c = sc.nextLong();
        System.out.println(a+b+c);
        sc.close();
    }
}

// int 자료형이 큰 숫자를 담기엔 너무 작음 -> long 로 변경
// 입력받을 때도, nextInt() -> nextLong()

