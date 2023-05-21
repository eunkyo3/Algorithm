import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int[] alphabet = new int[26];
        String str = sc.next().toUpperCase();
        
        for (int i=0; i<str.length(); i++)
        {
        	int num = str.charAt(i) - 'A';
        	alphabet[num] += 1;
        }
        
        int max = -1;
        char ch = '?';
        
        for (int i=0; i<26; i++)
        {
        	if (alphabet[i] > max)
        	{
        		max = alphabet[i];
        		ch = (char) (i+65);
        	}
        	else if (alphabet[i] == max)
        		ch = '?';
        }
        
        System.out.println(ch);
	}

}
