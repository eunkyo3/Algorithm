import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 무한 루프 시작
        while (true) {
            String str = sc.nextLine();

            // "."을 입력하면 프로그램 종료
            if (str.equals(".")) {
                System.exit(0);
            }
            
            Stack<String> stack = new Stack<>();
            String[] arr = str.split("");

            // 문자열의 각 문자를 확인하며 괄호 검사
            for (int i = 0; i < arr.length; i++) {
                // 여는 괄호일 경우 스택에 추가
                if (arr[i].equals("(") || arr[i].equals("[")) {
                    stack.push(arr[i]);
                }
                // 닫는 괄호일 경우
                else if(arr[i].equals(")")){
                    // 스택이 비어있지 않고 맨 위의 괄호가 여는 괄호와 짝이 맞는 경우
                    if(!stack.empty() && stack.peek().equals("(")){
                        stack.pop(); // 짝이 맞으므로 스택에서 제거
                    }
                    else{
                        stack.push(arr[i]); // 짝이 맞지 않는 경우 스택에 추가
                    }
                }
                // 닫는 대괄호일 경우
                else if(arr[i].equals("]")){
                    // 스택이 비어있지 않고 맨 위의 괄호가 여는 대괄호와 짝이 맞는 경우
                    if(!stack.empty() && stack.peek().equals("[")){
                        stack.pop(); // 짝이 맞으므로 스택에서 제거
                    }
                    else{
                        stack.push(arr[i]); // 짝이 맞지 않는 경우 스택에 추가
                    }
                }
            }

            // 스택이 비어있다면 모든 괄호가 맞음을 의미
            if (stack.empty()) {
                System.out.println("yes");
            }
            // 스택이 비어있지 않다면 괄호가 맞지 않음을 의미
            else {
                System.out.println("no");
            }
        }
    }
}
