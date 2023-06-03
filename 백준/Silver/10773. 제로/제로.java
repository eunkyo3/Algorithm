import java.util.Scanner;
import java.util.Stack;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Stack<Integer> stack = new Stack<>();
        int n = sc.nextInt();
        for (int i = 0; i < n; i++)
        {
            int num = sc.nextInt();
            if (num != 0)
            {
                stack.push(num);
            }
            else
            {
                stack.pop();
            }
        }
        
        int sum = stack.stream().mapToInt(Integer::intValue).sum();
        System.out.println(sum);
        sc.close();
    }
}
