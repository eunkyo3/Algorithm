    import java.util.*;
    /*
    입력
    5 5 1
    1 4
    1 2
    2 3
    2 4
    3 4
    
    출력
    1
    2
    4
    3
    0
    */
    class Main {
        static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        static int[] result;
        static boolean[] visited;
        static int cnt = 1;
        public static void bfs(int v) {
            Queue<Integer> queue = new LinkedList<>();
            queue.offer(v);
            visited[v] = true;
            result[v] = cnt++;
            while(!queue.isEmpty()) {
                int node = queue.poll();
                Collections.sort(graph.get(node));
                for(int i : graph.get(node)) {
                    if(!visited[i]) {
                        visited[i] = true;
                        result[i] = cnt++;
                        queue.offer(i);
                    }
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
            
            for(int i=0; i<=n; i++) {
                graph.add(new ArrayList<>());
            }
            
            for(int i=0; i<m; i++) {
                int a = sc.nextInt();
                int b = sc.nextInt();
                graph.get(a).add(b);
                graph.get(b).add(a);
            }
            
            bfs(r);
            
            for(int i=1; i<=n; i++) {
                System.out.println(result[i]);
            }
        }
    }