import java.util.Scanner; // 자바 기본 구조

public class Main{ // 파일명과 class명이 일치해야함 (일단은 public을 하나만, 추가적으로 public을 같은 페이지에 여러개 쓸 수 있지만 두 파일을 동시에 컴파일해야함)
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.println(a + b);
        sc.close(); // sc에 생기는 물결무늬 해당 코드 작성시 없어짐 (자바 리소스 누수 감지시 물결무늬)
    }
}
