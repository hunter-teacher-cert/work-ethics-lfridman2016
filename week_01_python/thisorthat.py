# Lyuba Fridman
# This or That
# Wrote this program to be used for icebreaker on first day of class 9/13/2021
# Demonstrates lists, while loops, random, functions
# Assignment: Create one or more Python programs in your week_01_python folder that exhibit your knowledge of Python including functions, lists and dictionaries.
import random

questions = [
"Dog or Cat?",
"Netflix or YouTube?",
"Phone Call or Text?"
"Toast or Eggs?",
"Cardio or Weights?", 
"Instagram or Snapchat?",
"Ice Cream Cone or Snow Cone?",
"Mobile Games or Console Games?"
"While walking: Music or Podcasts?",
"iOS or Android?",
"Hip Hop or Rock?",
"Cake or Pie?",
"Swimming or Sunbathing?",
"High-tech or Low-tech?",
"Big Party or Small Gathering?",
"New Clothes or New Phone?",
"Football or Basketball?",
"Work Hard or Play Hard?", 
"What’s worse: Laundry or Dishes?",
"Sneakers or Sandals?", 
"Watch or Play sports",
"Sweet or Salty", 
"Money or Fame",
"Pasta or Pizza",
"Comedy or Drama", 
"Puzzles or Board Games", 
"Steak or Chicken", 
"Glasses or Contacts?",
"Hamburger or Taco?", 
"Online Shopping or Shopping in a Store?", 
"Receive: Email or Letter?", 
"Passenger or Driver?",
"Car or Truck?",
"Money or Free Time?", 
"Amusement Park or Day at the Beach?",
"At a movie: Candy or Popcorn?", 
"Pen or Pencil?", 
"Toilet paper: Over or under?", 
"Tablet or Computer?",
"Dine In or Delivery?", 
"Sweater or Hoodie?",
"Comic Book or Comic Strips?", 
"Motorcycle or Bicycle?", 
"Book or eBook?", 
"When sleeping: Fan or No Fan?", 
"Apple Computer or PC?"
]

def prompt_and_generate():
  response = input("Would you like to generate a question? Type y for yes or n for no.")
  while response == 'y':
    index = random.randrange(0, len(questions))
    print(questions[index])
    response = input("Would you like to generate a question? Type y for yes or n for no.")

prompt_and_generate()