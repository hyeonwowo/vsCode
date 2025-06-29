public class Array { // 배열 선언 및 초기화
    public static void main(String[] args) {
        int[] arr = new int[5];
        arr[0] = 10;

        int[] arr2 = {1, 2, 3, 4, 5};

        for (int i = 0; i < arr2.length; i++) {
            System.out.println(arr2[i]);
        }

        int[][] grid = new int[3][3];
        grid[0][0] = 1;
    }
}
