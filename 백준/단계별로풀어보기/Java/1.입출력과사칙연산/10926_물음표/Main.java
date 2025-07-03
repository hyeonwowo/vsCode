import java.util.Scanner; // 폴더명을 백준 문제대로 10926_??! 로 했더니 인식을 못하고 실행을 못시킴. 폴더명을 10926_물음표 로 변환했더니 정상작동
// 왜 ??! 폴더명 때문에 문제가 발생했을까?
// 1. 물음표 ?는 파일 시스템에서 "예약 문자"로 쓰입니다
// macOS, Linux, Windows 모두 일부 특수문자를 파일명에서 제한하거나 특별한 의미로 처리합니다.

// ?는 "어떤 문자든 하나"라는 의미로 해석되기도 하고, 쉘이나 터미널에서 와일드카드 (wildcard) 로 사용됩니다.

// 그래서 ??! 같은 폴더명은:

// 터미널/명령어 해석 시 ?를 정상적인 문자로 보지 않고,

// "10926_??!" 전체를 실제 존재하지 않는 경로로 오인하게 됩니다.

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String name = sc.nextLine();
        System.out.println(name+"??!");
        sc.close();
    }
}