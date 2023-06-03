import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine()); 
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < num; i++)
        {
            String[] str = br.readLine().split(" ");
            switch (str[0]) {
                case "push":
                    stack.push(Integer.parseInt(str[1]));
                    break;
                case "pop":
                    System.out.println(stack.empty() ? -1 : stack.pop());
                    break;
                case "size":
                    System.out.println(stack.size());
                    break;
                case "empty":
                    System.out.println(stack.empty() ? 1 : 0);
                    break;
                case "top":
                    System.out.println(stack.empty() ? -1 : stack.peek());
                    break;
            }
        }
    }
}
