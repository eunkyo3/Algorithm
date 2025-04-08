import java.util.*;
public class Main {
	static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
	static int result = 0;
	public static void bfs(int v) {
		boolean[] visited = new boolean[graph.size()];
		Queue<Integer> queue = new LinkedList<>();
		queue.offer(v);
		visited[v]=true;
		while(!queue.isEmpty()) {
			int node=queue.poll();
			for(int i : graph.get(node)) {
				if(!visited[i]) {
					visited[i]=true;
					queue.offer(i);
					result++;
				}
			}
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int computer = sc.nextInt();
		int virus = sc.nextInt();
		
		for(int i=0; i<=computer; i++) {
			graph.add(new ArrayList<>());
		}
		
		for(int i=0; i<virus; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			graph.get(a).add(b);
			graph.get(b).add(a);
		}
		
		bfs(1);
		
		System.out.println(result);
		
		sc.close();
	}

}