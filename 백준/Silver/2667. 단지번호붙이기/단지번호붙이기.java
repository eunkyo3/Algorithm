import java.util.*;

public class Main {
    static int n;
    static int area = 0;
    static int[][] map;
    static final int[] dx = {-1, 0, 1, 0};
    static final int[] dy = {0, 1, 0, -1};
    static boolean[][] visited;
    static int cnt;
    static ArrayList<Integer> result = new ArrayList<>();

    public static void dfs(int a, int b) {
        visited[a][b] = true;
        for (int i = 0; i < 4; i++) {
            int nx = a + dx[i];
            int ny = b + dy[i];
            if ((0 <= nx && nx < n) && (0 <= ny && ny < n) && !visited[nx][ny] && map[nx][ny] == 1) {
                cnt++;
                dfs(nx, ny);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        sc.nextLine();  
        map = new int[n][n];
        visited = new boolean[n][n];

        for (int i = 0; i < n; i++) {
            String line = sc.nextLine();
            for (int j = 0; j < n; j++) {
                map[i][j] = line.charAt(j) - '0';
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (map[i][j] == 1 && !visited[i][j]) {
                    cnt = 1;
                    dfs(i, j);
                    result.add(cnt);
                    area++;
                }
            }
        }
        
        System.out.println(area);
        Collections.sort(result);
        for (int val : result) {
            System.out.println(val);
        }

        sc.close();
    }
}
