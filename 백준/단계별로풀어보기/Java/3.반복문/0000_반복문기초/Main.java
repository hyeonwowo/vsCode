public class Main {
    public static void main(String[] args) {

        // (1) for문: 0부터 4까지 출력
        System.out.println("== for문 예제 ==");
        for (int i = 0; i < 5; i++) {
            System.out.println("for문 i = " + i);
        }

        // (2) while문: 0부터 4까지 출력
        System.out.println("\n== while문 예제 ==");
        int j = 0;
        while (j < 5) {
            System.out.println("while문 j = " + j);
            j++;
        }

        // (3) do-while문: 0부터 4까지 출력
        System.out.println("\n== do-while문 예제 ==");
        int k = 0;
        do {
            System.out.println("do-while문 k = " + k);
            k++;
        } while (k < 5);

        // (4) for-each문: 배열 요소 출력
        System.out.println("\n== for-each문 예제 ==");
        int[] numbers = {10, 20, 30, 40, 50};
        for (int num : numbers) {
            System.out.println("배열 값 = " + num);
        }
    }
}
