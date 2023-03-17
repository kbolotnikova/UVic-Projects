import java.io.*;
import java.util.*;

public class ArrayMatch {

    static boolean match(int[] a, int[] b){
        /*
           Input: Two arrays of equal length
           Output: A booleam, true if arrays or subarrays are equal, false otherwise
           Description: Compares two arrays of length n to check if they are equal 
						or if n%2 == 0 checks if the subarrays are equal
         */
        if (Arrays.equals(a,b)) {
            return true;
        }
        if (a.length%2 != 0 || b.length%2 != 0) {
            return false;
        } else {
            int[] a1 = Arrays.copyOfRange(a, 0, (a.length/2));
            int[] a2 = Arrays.copyOfRange(a, a.length/2, a.length);
            int[] b1 = Arrays.copyOfRange(b, 0, (b.length/2));
            int[] b2 = Arrays.copyOfRange(b, b.length/2, b.length);

            boolean match1 = match(a1,b1);
            boolean match2 = match(a2,b2);
            if (match1 != match2) {
                if(match1){
                    return(match(a1,b2));
                }else{
                    return(match(a2,b1));
                }
            }else{
                return (match1);
            }
            }
    }

    public static void main(String[] args) {
    /* Read input from STDIN. Print output to STDOUT. Your class should be named ArrayMatch.

	You should be able to compile your program with the command:

		javac ArrayMatch.java

   	To conveniently test your algorithm, you can run your solution with any of the tester input files using:

		java ArrayMatch inputXX.txt

	where XX is 00, 01, ..., 13.
	*/

        Scanner s;
        if (args.length > 0){
            try{
                s = new Scanner(new File(args[0]));
            } catch(java.io.FileNotFoundException e){
                System.out.printf("Unable to open %s\n",args[0]);
                return;
            }
            System.out.printf("Reading input values from %s.\n",args[0]);
        }else{
            s = new Scanner(System.in);
            System.out.printf("Reading input values from stdin.\n");
        }

        int n = s.nextInt();
        int[] a = new int[n];
        int[] b = new int[n];

        for(int j = 0; j < n; j++){
            a[j] = s.nextInt();
        }

        for(int j = 0; j < n; j++){
            b[j] = s.nextInt();
        }

        System.out.println((match(a, b) ? "YES" : "NO"));
    }
}
