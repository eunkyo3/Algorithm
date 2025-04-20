import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] dx = {2, 1, -1, -2, -2, -1, 1, 2};
        int[] dy = {1, 2, 2, 1, -1, -2, -2, -1};

        int t = sc.nextInt();

        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            int[][] map = new int[n][n];
            boolean[][] visited = new boolean[n][n];

            int nowX = sc.nextInt();
            int nowY = sc.nextInt();
            int wantX = sc.nextInt();
            int wantY = sc.nextInt();

            if (nowX == wantX && nowY == wantY) {
                System.out.println(0);
                continue;
            }

            Queue<int[]> queue = new LinkedList<>();
            queue.offer(new int[]{nowX, nowY});
            visited[nowX][nowY] = true;
            map[nowX][nowY] = 0;

            while (!queue.isEmpty()) {
                int[] current = queue.poll();
                int x = current[0];
                int y = current[1];

                for (int j = 0; j < 8; j++) {
                    int nx = x + dx[j];
                    int ny = y + dy[j];

                    if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny]) {
                        visited[nx][ny] = true;
                        map[nx][ny] = map[x][y] + 1;

                        if (nx == wantX && ny == wantY) {
                            System.out.println(map[nx][ny]); 
                            queue.clear();
                            break;
                        }

                        queue.offer(new int[]{nx, ny});
                    }
                }
            }
        }
    }
}
