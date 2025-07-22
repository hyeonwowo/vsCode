import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<>();

        int n = sc.nextInt();  // System.in 생략
        int a = 0;
        int b = 0;

        for (int i = 0; i < n; i++) {
            a = sc.nextInt();  // System.in 생략
            b = sc.nextInt();
            list.add(a + b);   // 덧셈한 결과를 list에 추가
        }

        for (int i = 0; i < n; i++) {
            System.out.println(list.get(i));  // ArrayList는 get(index)로 접근
        }

        sc.close();
    }
}
