public class Crowns {
  
  public static int printer(int crown_count, int chest_level) {
    
    int counter = 1;
    int total_crowns = 0;
    int current_crowns = 0;
    int crowns_needed = 0;
    
    while( counter <= 10) {
      counter += 1;
      total_crowns += 50 * counter;
    }
    counter = 0;
    
    while (counter <= chest_level) {
      counter += 1;
      current_crowns += 50 * counter;
    }
    
    crowns_needed = total_crowns - current_crowns;
    
    return crowns_needed;
  }
  
  
  
}
                    

    
    
                      
                   
  