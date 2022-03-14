	import java.io.*;
	import java.util.*;

	public class number2 {
	   
	    public static String lexmen = "";
	   public  static HashMap<String, Integer> symbols = new HashMap<>();
	   
	    public static void main(String args[]) throws IOException {

	        specialsymbols();
	 
	        String str = "IF_CODE";
	            // Print the string

	            for(int i = 0; i < str.length(); i++){


	                identify(str.charAt(i), false);

	            }
	        	 
	        identify(' ', true);

	        System.out.println("Next Lexmen is  EOF");

	    }

	    
	    static void specialsymbols(){

	       // symbols.put("letter",0);
	        symbols.put("ident",3);
	        symbols.put("+",2);
	        symbols.put("-",10);
	        symbols.put("/",11);
	        symbols.put("*",14);
	        symbols.put("(",19);
	        symbols.put(")",22);
	        symbols.put("=",55);
	        symbols.put(".", 8);
	        symbols.put("FOR_CODE", 30);
	        symbols.put("IF_CODE", 31);

	    }

	    static void identify(char a, boolean finalC){
	        boolean lookup = symbols.containsKey(a+"");
	        if(a == ' '){
	            lookup = true;
	        }
	        if(lookup == false){
	            lexmen += a+"";
	        }else{
	          
	        
	           int token = floatliteral(lexmen) == false ? 30  : symbols.get(".");
	            token = intliteral(lexmen) == false ? 30 :  symbols.get("ident");
	        	
	            
	            if(lexmen.length() > 1)
	                System.out.println("Next token is: " + token + ", Next Lexmen is " + lexmen);

	            if(symbols.get(a+"") != null)
	                System.out.println("Next token is: " +  symbols.get(a+"") + ", Next Lexmen is " + a);

	            lexmen = "";
	            
	          

	        }

	    }

	    static boolean floatliteral(String str){

	        for(int i = 0; i < str.length(); i++){
	            if(str.charAt(i)=='.'){
	                return true;
	            }
	        }
	        return false;

	    }

	    static boolean intliteral(String str){
	        for(int i = 0; i < str.length(); i++){
	            if(Character.isLetter(str.charAt(i))){
	                return false;
	            }
	        }
	        return true;
	    }
	}


