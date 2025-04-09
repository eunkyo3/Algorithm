import java.util.*;

public class Main {
    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    static ArrayList<Integer> bfsResult = new ArrayList<>();
    static ArrayList<Integer> dfsResult = new ArrayList<>();
    static boolean[] dfsVisited;
    public static void dfs(int v) {
        dfsResult.add(v);
        dfsVisited[v] = true;
        for(int i : graph.get(v)) {
            if(!dfsVisited[i]) {
                dfsVisited[i] = true;
                dfs(i);
            }
        }
    }
    public static void bfs(int v) {
        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[graph.size()+1];
        q.offer(v);
        visited[v] = true;
        
        while(!q.isEmpty()) {
            int node = q.poll();
            bfsResult.add(node);
            for(int i : graph.get(node)) {
                if(!visited[i]) {
                    q.offer(i);
                    visited[i] = true;
                }
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int v = sc.nextInt();

        bfsResult = new ArrayList<>();
        dfsResult = new ArrayList<>();
        
        for(int i=0; i<=n; i++) {
            graph.add(new ArrayList<>());
        }

        for(int i=0; i<m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        for (int i = 1; i <= n; i++) {
            Collections.sort(graph.get(i));
        }
        
        dfsVisited = new boolean[graph.size()];
        
        dfs(v);
        bfs(v);
        
        // DFS 결과 출력
        for (int i : dfsResult) {
            System.out.print(i + " ");
        }
        System.out.println();

        // BFS 결과 출력
        for (int i : bfsResult) {
            System.out.print(i + " ");
        }
    }

}