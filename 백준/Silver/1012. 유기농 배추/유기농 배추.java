import java.util.*;
public class Main {
	static int[][] map;
	static boolean[][] visited;
	static final int[] dx= {-1, 0, 1, 0};
	static final int[] dy= {0, 1, 0, -1};
	public static void dfs(int a, int b) {
		visited[a][b] = true;
		for(int i=0; i<4; i++) {
			int nx = a+dx[i];
			int ny = b+dy[i];
			if(0<=nx&&nx<map.length&&0<=ny&&ny<map[0].length&&!visited[nx][ny]&&map[nx][ny]==1) {
				dfs(nx, ny);
			}
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		
		for(int i=0; i<t; i++) {
			int m = sc.nextInt();
			int n = sc.nextInt();
			int k = sc.nextInt();
			
			map = new int[m][n];
			visited = new boolean[m][n];
			
			int cnt = 0;
			
			for(int j=0; j<k; j++) {
				int x = sc.nextInt();
				int y = sc.nextInt();
				map[x][y] = 1;
			}
			
			for(int a=0; a<m; a++) {
				for(int b=0; b<n; b++) {
					if(map[a][b]==1 && !visited[a][b]) {
						cnt++;
						dfs(a, b);
					}
				}
			}
			
			System.out.println(cnt);
		}
		
		sc.close();

	}

}