import java.util.*;

public class Main {

    public static int max = 100000;
    public static int[] visited = new int[max+1];
    public static int next = 0;

    public static void bfs(int start, int end) {
        Queue<Integer> q = new LinkedList<>();

        q.add(start);
        visited[start] = 0;

        while(!q.isEmpty()) {
            int cur = q.poll();

            next = cur - 1;
            if(next >= 0 && visited[next] > visited[cur] + 1 ) {
                visited[next] = visited[cur] + 1;
                q.add(next);
            }

            next = cur + 1;
            if(next <= max && visited[next] > visited[cur] + 1 ) {
                visited[next] = visited[cur] + 1;
                q.add(next);
            }

            next = cur * 2;
            if(next <= max && visited[next] > visited[cur] + 1 ) {
                visited[next] = visited[cur] + 1;
                q.add(next);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int start = sc.nextInt();
        int end = sc.nextInt();

        Arrays.fill(visited, Integer.MAX_VALUE);
        bfs(start, end);

        System.out.println(visited[end]);

        sc.close();
    }

}