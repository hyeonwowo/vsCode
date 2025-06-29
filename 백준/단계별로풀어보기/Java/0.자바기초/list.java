import java.util.ArrayList;

public class list{
    public static void main(String[] args){
        ArrayList<Integer> list = new ArrayList<>();

        list.add(10);
        list.add(20);
        list.add(1,15);
        list.remove(0);
        System.out.println(list.get(1));
        System.out.println(list.size());
    }
}