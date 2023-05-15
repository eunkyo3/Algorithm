import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int c = sc.nextInt();
        double[] score = new double[c];
        double max = 0;
        double result = 0;
        
        
        for (int i=0; i<c; i++)
        {
        	int n = sc.nextInt();
        	score[i] = n;
        	
        }
        
        for (int i=0; i<score.length; i++)
        {
        	if (max < score[i]) max = score[i];
        }
        
        for (int i=0; i<score.length; i++)
        {
        	result += score[i]/max*100;
        }
        
        System.out.print(result/score.length);
	}

}