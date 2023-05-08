import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in); // Scanner 선언

        int N = 0;  // 바구니 선언
        int M = 0;  // 넣을 횟수 선언

        N = sc.nextInt();   // 바구니 수 입력 받기
        M = sc.nextInt();   // 공을 넣을 횟수 입력 받기

        int[] basket = new int[N]; // 바구니 배열

        for(int i=0;i<M;i++)
        {
            int a = sc.nextInt(); // 시작 위치
            int b = sc.nextInt(); // 끝 위치
            int c = sc.nextInt(); // 공 번호

            for(int j=a-1;j<b;j++)
            {
                basket[j] = c;
            }
        }

        for(int i=0;i<basket.length;i++)
        {
            System.out.print(basket[i]+" ");
        }
    }
}
