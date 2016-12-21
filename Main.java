import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    
    Scanner scan = new Scanner(System.in);
    
    System.out.println("Enter your clan's current chest level.");
    int chest_level = scan.nextInt();
    System.out.println("Enter your clan's current crown count in that level.");
    int crown_count = scan.nextInt();
    
    int result = Crowns.printer(crown_count, chest_level);
                       
                       
    System.out.println("Your clan needs "+result+" more crowns to get level 10.");
                      
  }
  
}