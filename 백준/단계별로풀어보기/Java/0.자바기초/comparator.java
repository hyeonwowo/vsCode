import java.util.*; // 요소 비교

class Person {
    String name;
    int age;
    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}

public class comparator {
    public static void main(String[] args) {
        ArrayList<Person> list = new ArrayList<>();
        list.add(new Person("현우", 25));
        list.add(new Person("민수", 20));
        list.add(new Person("영희", 22));

        // 나이 기준 오름차순 정렬
        Collections.sort(list, new Comparator<Person>() {
            public int compare(Person p1, Person p2) {
                return p1.age - p2.age;
            }
        });

        for (Person p : list) {
            System.out.println(p.name + " : " + p.age);
        }
    }
}
