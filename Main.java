import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    
    Scanner scan = new Scanner(System.in);
    
    System.out.println("Enter your current clan's crown count.");
    
    int crown_count = scan.nextInt();
    
    Crowns.printer(crown_count);
    
  }
  
}
