import java.io.BufferedReader;
import java.util.Scanner;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.math.BigInteger;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.*;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class VerificationSystem {
ArrayList<String> UID = new ArrayList<String>();
ArrayList<String> HashPassword = new ArrayList<String>();

public static String getHashfunction(String input)
{
try {

//  hashing MD5
MessageDigest m = MessageDigest.getInstance("MD5");

// digest() method is called to calculate message digest
// of an input digest() return array of byte
byte[] messageDigest = m.digest(input.getBytes());

// Convert byte array into BigInteger
BigInteger no = new BigInteger(1, messageDigest);

// Convert message digest into hex value
String hashtext = no.toString(16);
while (hashtext.length() < 32) {
hashtext = "0" + hashtext;
}
return hashtext;
}

// for errors
catch (NoSuchAlgorithmException e) {
throw new RuntimeException(e);
}
}



public static void main(String[] args) throws NoSuchAlgorithmException, FileNotFoundException {
	Scanner scanner1 = new Scanner(new File("src/password.txt"));
	Scanner scanner2 = new Scanner(new File("src/salt.txt"));
	Scanner scanner3 = new Scanner(new File("src/hash.txt"));
	while (scanner1.hasNextLine()) {
	String pass = scanner1.nextLine();
	String salt = scanner2.nextLine();
	String temp= pass+salt; // concatenate pass and salt 
	String hash_req = scanner3.nextLine();
	if(getHashfunction(temp).equals(hash_req)){
		System.out.println( "\n" + "The input password and salt matches the hash value in the database" +"\n" + getHashfunction(temp)+ "," +  hash_req  );// the passwords are correct 
		
	}else {
		System.out.println("The input password and salt does not match the hash value in the database");
	}
	}
	
	}
	
	//System.out.println(toHex(getMd5("0599054")));
}
