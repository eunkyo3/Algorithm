import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        String[] 크로아티아 = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
        for(String x : 크로아티아){
            str = str.replaceAll(x, "엄");
        }
        System.out.println(str.length());
        sc.close();
    }
}
