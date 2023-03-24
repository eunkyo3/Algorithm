import java.util.*;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s1 = new Scanner(System.in);

		int a = 0, b = 0, receip = 0, num = 0, result = 0;
		
		receip = s1.nextInt();
		
		num = s1.nextInt();
		
		for(int i = 1; i <= num; i++)
		{
			a = s1.nextInt();
			b = s1.nextInt();
			result += a*b;
			a= 0; b= 0;
		}
		
		if(receip == result)
		{
			System.out.println("Yes");
		}
		
		else if(receip != result)
		{
			System.out.println("No");
		}
	}

}
