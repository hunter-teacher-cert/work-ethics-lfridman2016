/*** Lyuba Fridman
Seating Algorithm
10/17/2021
This is not a working program. It does compile. Sections that still need to be implemented have been marked with TODO comments.
***/
import java.util.*;


public class SeatingAlgorithm {
	
  private int[][] seats = new int[40][7];//TODO fill with data
  private ArrayList<Party> parties = new ArrayList<Party>(); //TODO will with data
  
  public void assignPriorities()
  {
    for(Party party: parties)
      {
        if(party.youngestAge < 6)
          party.priority = 1;
        else if(party.youngestAge < 10)
          party.priority = 2;
        else if(party.youngestAge < 13)
          party.priority = 3;
        else if(party.hasDisabledPassenger)
            party.priority = 4;
        else
          party.priority = 5;
      }
  }
  
  boolean findSeats(Party booking)
  {
	  //TODO implement this to search 2D array for seats next to each other
	  return true;
  }
  
  public void assignSeats()
  {
    assignPriorities();
    parties.sort(null); //will be sorted using compareTo() method in Party class
	
    for(Party party: parties)
      {
		//Try to find seats for entire party
        boolean seatsFound = findSeats(party); //TODO implement findSeats to search 2D array for seats next to each other
        //if cannot seat entire party, split into subparties with at least 1 adult in each, and now try to find seats
		if(!seatsFound)
          {
            ArrayList<Party> subparties = party.splitAdults();
			//TODO add logic if subparties is empty
			//try to find seats for each subparty
            for(Party subparty: subparties)
              {
                if(!findSeats(subparty))
                  {
                    //Seats not found. Have to seat everyone separately and sort it out before boarding
					ArrayList<Party> singlePassengers = subparty.splitSinglePassengers();
					for(Party passenger: singlePassengers)
					{
						findSeats(passenger);
					}
                  }
              }
          }
      }
  }
    public static void main(String[] args) {
        SeatingAlgorithm seatAlgo = new SeatingAlgorithm();
		seatAlgo.assignSeats();
    }
}
