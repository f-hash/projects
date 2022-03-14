import java.util.Arrays; 
import java.util.HashSet; 
public class p1{
	public static void main(String[] args) {
		Integer[] a = {1, 2, 3, 4, 5, 6, 7};
		Integer[] b = {7, 2, 0, 10};
		HashSet<Integer> hash = new HashSet<Integer>(); 
		hash.addAll(Arrays.asList(a)); //asList is to get the list
		hash.retainAll(Arrays.asList(b)); // remove elements that are not b 
		System.out.println(hash);// print hash 
		Object[] aray = {};
		aray = hash.toArray(aray);
		System.out.println(Arrays.toString(aray));
		
	}

		


}