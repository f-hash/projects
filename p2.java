import java.util.*;
public class p2 {
    public static void main(String[] args) {
    	String str = "{}{{{{}}";
    	boolean ans = isBalanced(str);
    	System.out.println("Answer: " + ans);
    }
    	public static boolean isBalanced(String str) {
    		Stack<Character> stack = new Stack<Character>(); 
    		for(int i = 0; i< str.length() ; i++) { // difference in length() and size()
    			char b = str.charAt(i);
    			if(b == '}') {
    				stack.push(b);
    			}else if (b == '}' && stack.pop() == '{' || stack.isEmpty()) {
    				return false;
    			}else {
    				stack.pop();
    			}
    		}
    		return stack.isEmpty();
    		
    	}
}
