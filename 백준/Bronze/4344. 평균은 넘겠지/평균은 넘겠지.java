import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int c = sc.nextInt();
        int[] st;
        
        for (int i=0; i<c; i++)
        {
        	int n = sc.nextInt();
        	st = new int[n];
        	
        	double sum = 0;
        	
        	for (int j=0; j<n; j++)
        	{
        		int score = sc.nextInt();
        		st[j] = score;
        		sum += score;
        	}
        	
        	double avg = sum/n;
        	double cnt = 0;
        	
        	for (int k=0; k<n; k++)
        	{
        		if (st[k] > avg)
        			cnt++;
        	}
        	
        	System.out.printf("%.3f%%\n", cnt / n * 100);
        	
        }
	}

}