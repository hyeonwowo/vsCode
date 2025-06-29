public class Basic_Structure {
    public static void main(String[] args){
        Person p = new Person("hyeonwoo", 25);
        p.sayHello();
    }
}

class Person{
    String name;
    int age;

    Person(String name, int age){
        this.name = name;
        this.age = age;
    }

    void sayHello(){
        System.out.println("name : " + name + " " + "age : " + age);
    }
}