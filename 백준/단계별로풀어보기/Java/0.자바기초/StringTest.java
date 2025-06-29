public class StringTest { // 클레스 이름은 예약어와 다르게 지어주기 string -> stringTest
    public static void main(String[] args){
        String s = "hello";
        System.out.println(s.length());
        System.out.println(s.charAt(1));
        System.out.println(s.substring(1,4));

        String a = "apple";
        String b = "apple";
        System.out.println(a.equals(b));
    }
}
