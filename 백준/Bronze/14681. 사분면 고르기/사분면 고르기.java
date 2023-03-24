import java.util.*;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int x = sc.nextInt();
		int y = sc.nextInt();
		
		if(x >= 1 && y >= 1)
			System.out.println(1);
		else if(x <= -1 && y >= 1)
			System.out.println(2);
		else if(x <= -1 && y <= -1)
			System.out.println(3);
		else if(x >= 1 && y <= -1)
			System.out.println(4);
	}

}