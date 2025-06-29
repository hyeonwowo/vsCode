import java.util.HashMap; // 해시

public class hash{
    public static void main(String[] args){
        HashMap<String, Integer> map = new HashMap<>();

        map.put("apple", 3);
        map.put("banana", 5);
        map.put("apple", 7);
        System.out.println(map.get("apple"));
        System.out.println(map.containsKey("banana"));
        map.remove("banana");
    }
}