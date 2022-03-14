import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class CrackerSystem extends VerificationSystem{

public static void main(String[] args) throws NoSuchAlgorithmException, FileNotFoundException{
	
		Scanner scanner1 = new Scanner(new File("src/password.txt"));
		Scanner scanner2 = new Scanner(new File("src/salt.txt"));
		Scanner scanner3 = new Scanner(new File("src/hash.txt"));
		Scanner scanner4 = new Scanner(new File("src/UID.txt"));			
		while (scanner1.hasNextLine()) {
			String pass = scanner1.nextLine();
			String salt = scanner2.nextLine();
			String uid = scanner4.nextLine();
			String temp= pass+salt; //  
			String hash_req = scanner3.nextLine();

			if(getHashfunction(temp).equals(hash_req)) {
                   System.out.println("The uid: " + uid + " password: " + pass + " salt: " + salt);
			}
		}
		}

}
