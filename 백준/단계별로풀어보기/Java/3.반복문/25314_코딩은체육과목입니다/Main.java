import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String res = "";

        int cnt = 0;
        if (n==4)
            cnt = 0;
        else
            cnt = (n-4) / 4;

        for (int i=0; i<cnt; i++)
            res += "long ";
        res += "long int";
        
        System.out.println(res);
        sc.close();
    }
}