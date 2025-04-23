import java.util.*;

public class Main {
    static int[] tmp;         
    static int count = 0;      
    static int K;              
    static int result = -1;   

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        K = sc.nextInt();
        int[] arr = new int[N];
        tmp = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        mergeSort(arr, 0, N - 1);
        System.out.println(result);
    }

    static void mergeSort(int[] arr, int start, int end) {
        if (start < end) {
            int mid = (start + end) / 2;
            mergeSort(arr, start, mid);
            mergeSort(arr, mid + 1, end);
            merge(arr, start, mid, end);
        }
    }

    static void merge(int[] arr, int start, int mid, int end) {
        int i = start;
        int j = mid + 1;
        int t = start;

        while (i <= mid && j <= end) {
            if (arr[i] <= arr[j]) {
                tmp[t++] = arr[i++];
            } else {
                tmp[t++] = arr[j++];
            }
        }

        while (i <= mid) tmp[t++] = arr[i++];
        while (j <= end) tmp[t++] = arr[j++];

        for (int k = start; k <= end; k++) {
            arr[k] = tmp[k];
            count++;
            if (count == K) {
                result = arr[k];
                return;  
            }
        }
    }
}
