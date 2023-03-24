import java.util.*;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int n = 0;
		n = sc.nextInt();
		
		for(int i = 1; i <= 9; i++)
		{
			System.out.printf("%d * %d = %d\n", n, i, n*i);
		}
	}

}