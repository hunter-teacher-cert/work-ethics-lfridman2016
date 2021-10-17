import java.util.*;

public class Party implements Comparable {
    public int youngestAge;
    public boolean hasDisabledPassenger;
    public int priority;
    public Date purchaseDate;

    public int compareTo(Object obj)
    {
      Party comp = (Party)obj;
      if(comp.priority < this.priority)
        return 1;
      else if(comp.priority > this.priority)
        return -1;
      else //if priority is equal go by purchase date
        return this.purchaseDate.compareTo(comp.purchaseDate);
    }
	
	//TODO implement to return a list of subparties where each subparty contains at least 1 adult
	public ArrayList<Party> splitAdults()
	{
		return null;
	}
	
	//TODO implement to return a list of subparties where each subparty contains only 1 passenger. To be
	//used if passengers cannot be seated together.
	public ArrayList<Party> splitSinglePassengers()
	{
		return null;
	}
  }