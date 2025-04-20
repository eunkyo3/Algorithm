import java.util.*;

public class Main {
	static int m, n;
	static int[][] map;
	static boolean[][] visited;
	static int[] dx = {1, 0, -1, 0};
	static int[] dy = {0, 1, 0, -1};
	static int cnt = 0;
	static Queue<int[]> queue = new LinkedList<>();
	public static void bfs() {
		while(!queue.isEmpty()) {
			int[] current = queue.poll();
			int x = current[0];
			int y = current[1];
			for(int i=0; i<4; i++) {
				int nx = x+dx[i];
				int ny = y+dy[i];
				if(nx>=0&&nx<n&&ny>=0&&ny<m&&map[nx][ny]!=-1&&!visited[nx][ny]) {
					map[nx][ny] = 1;
					queue.offer(new int[] {nx, ny});
					map[nx][ny] = map[x][y] + 1;
					visited[nx][ny] = true;
					cnt = map[x][y];
				}
			}
		}
	}
    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
    	
    	m = sc.nextInt();
    	n = sc.nextInt();
    	sc.nextLine();
    	
    	map = new int[n][m];
    	visited = new boolean[n][m];
    	
    	for (int i=0; i<n; i++) {      
            for (int j=0; j<m; j++) {  
                map[i][j] = sc.nextInt(); 
            }
        }
    	
    	for(int i=0; i<n; i++) {
    		for(int j=0; j<m; j++) {
    			if(map[i][j]==1&&!visited[i][j]) {
    				queue.offer(new int[] {i, j});
    				visited[i][j] = true;
    			}
    		}
    	}
    	
    	bfs();
    	
    	for(int i=0; i<n; i++) {
    		for(int j=0; j<m; j++) {
    			if(map[i][j]==0) {
    				cnt = -1;
    				break;
    			}
    		}
    	}
    	
    	System.out.println(cnt);
    }
}