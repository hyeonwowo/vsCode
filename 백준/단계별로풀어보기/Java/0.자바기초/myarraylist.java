import java.util.ArrayList;

public class myarraylist {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(2);
        list.add(3);

        for (int i = 0; i < 3; i++) {
            System.out.println(list.get(i)); // i번째 값 출력
        }
    }
}
