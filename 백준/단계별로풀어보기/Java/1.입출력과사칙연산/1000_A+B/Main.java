import java.util.Scanner; // 얜 느리다..

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(); // 자바에서는 한줄입력이든, 여러줄 입력이든 그저 nextInt()를 여러번 호출하기만 하면 됨
        int b = sc.nextInt();
        System.out.println(a + b);
        sc.close();
    }
}