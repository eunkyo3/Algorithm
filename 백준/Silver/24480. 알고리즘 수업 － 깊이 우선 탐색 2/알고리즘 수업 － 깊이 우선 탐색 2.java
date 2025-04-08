import java.util.*;
/*
    5 5 1
    1 4
    1 2
    2 3
    2 4
    3 4
    
    1
    2
    3
    4
    0
*/
public class Main {
    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    static boolean[] visited;
    static int[] result;
    static int cnt = 1;
    public static void dfs(int current) {
        visited[current] = true;
        result[current] = cnt++;
        Collections.sort(graph.get(current), Collections.reverseOrder());
        for(int next : graph.get(current)) {
            if(!visited[next]) {
                dfs(next);
            }
        }
        
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int r = sc.nextInt();
        
        visited = new boolean[n+1];
        result = new int[n+1];
        
        for(int i=0; i<=n; i++){
            graph.add(new ArrayList<>());
        }
        
        for(int i=0; i<m; i++){
            int u = sc.nextInt();
            int v = sc.nextInt();
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        
        dfs(r);
        
        for (int i = 1; i <= n; i++) {
            System.out.println(result[i]);
        }
    }
}
