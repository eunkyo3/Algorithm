import java.util.*;

public class Main {

    static int max = 100000;
    static int[] visited = new int[max+1];
    static int next = 0;

    public static int bfs_01(int start, int end) {
        Deque<Integer> deque = new ArrayDeque<>();
        deque.add(start);
        visited[start] = 0;

        while(!deque.isEmpty()) {
            int cur = deque.poll();

            if(cur == end) {
                return visited[cur];
            }

            next = cur * 2;
            if(next <= max && visited[next] == -1) {
                visited[next] = visited[cur];
                deque.addFirst(next);
            }

            next = cur - 1;
            if(next >=0 && visited[next] == -1) {
                visited[next] = visited[cur] + 1;
                deque.addLast(next);
            }

            next = cur + 1;
            if(next <= max && visited[next] == -1) {
                visited[next] = visited[cur] + 1;
                deque.addLast(next);
            }
        }

        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int start = sc.nextInt();
        int end = sc.nextInt();

        Arrays.fill(visited, -1);

        int result = bfs_01(start, end);
        System.out.println(result);

        sc.close();
    }

}