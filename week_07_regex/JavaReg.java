import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class JavaReg {
  public static void main(String[] args) {
    Pattern pattern = Pattern.compile("(Mr|Ms|Mrs|Dr)\\.? [A-Z][a-z]*( [A-Z][a-z]*)?", Pattern.CASE_INSENSITIVE);
    Matcher matcher = pattern.matcher("Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense.");
    
    
    boolean matchFound = matcher.find();
    System.out.println(matcher.group());
    matchFound = matcher.find();
    System.out.println(matcher.group());
    /*if(matchFound) {
      System.out.println("Match found");
    } else {
      System.out.println("Match not found");
    }
    */
  }
}
// Outputs Match found