import java.util.*;

public class Main {

    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
    	int n = sc.nextInt();
    	int m = sc.nextInt();
    	sc.nextLine();
    	
    	int[][] map = new int[n][m];
    	boolean[][] visited = new boolean[n][m];
    	
    	for (int i = 0; i < n; i++) {
            String line = sc.nextLine(); 
            for (int j = 0; j < m; j++) {
                map[i][j] = line.charAt(j) - '0'; 
            }
        }
    	
    	int[] dx = {-1, 0, 1, 0};
    	int[] dy = {0, 1, 0, -1};
    	
    	Queue<int[]> queue = new LinkedList<>();
    	queue.offer(new int[] {0, 0});
    	visited[0][0] = true;
    	
    	while(!queue.isEmpty()) {
    		int[] current = queue.poll();
    		int x = current[0];
    		int y = current[1];
    		for(int i=0; i<4; i++) {
    			int nx = x+dx[i];
    			int ny = y+dy[i];
    			if(nx>=0&&nx<n&&ny>=0&&ny<m&&!visited[nx][ny]&&map[nx][ny]==1) {
    				visited[nx][ny] = true;
    				queue.offer(new int[] {nx, ny});
    				map[nx][ny] = map[x][y]+1; 
    			}
    		}
    	}
    	
    	System.out.println(map[n-1][m-1]);
    }
}