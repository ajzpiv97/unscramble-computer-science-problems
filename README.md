# Unscramble Computer Science Problems
In this project, you will complete five tasks based on a fabricated set of calls and texts exchanged during September 2016. You will use Python to analyze and answer questions about the texts and calls contained in the dataset. Lastly, you will perform run time analysis of your solution and determine its efficiency.

## Task 0
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"

### Worst Case Big-O Notation
 - Time Complexity - O(1)
 - The algorithm is constant time because it does not depend on the size of either calls or text list

## Task 1
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."

### Worst Case Big-O Notation
 - Time Complexity - O(n)
 - The algorithm is linear time because it requires to iterate N times the length of each list so each for loop
   so each for loop account for O(n) resulting in O(2n). This however, following the Big O coefficient rule of
   dropping constant, the resultant time complexity is O(n)

## Task 2
Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".

### Worst Case Big-O Notation
 - Time Complexity - O(n)
 - The algorithm is linear time because it requires to iterate N times the length of each list so each for loop
   so each for loop account for O(n) resulting in O(2n).
   This however, following the Big O coefficient rule of dropping constant, the resultant time complexity is O(n).
   Dictionary operations are all O(1), so they are constant time operations

## Task 3
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

### Worst Case Big-O Notation
 - Time Complexity - O(nlog(n))
 - This algorithm is super-linear time because the sort() function for sorting lists uses time sort algorithm
   which the time complexity for it is O(nlog(n)). The time complexity for the for loop its actually O(2kn + 5),
    however, we know that the phone number length is max 11 characters transforming to O(22n+5). Finally, the last two
    methods, one for converting the dictionary keys into a list that is O(n) and sum the dictionary is O(n) as well.
    Therefore, the total time complexity solution is actually O(nlog(n) + 22n+5 + n + n) => O(nlog(n) + 24n + 5).
    Because of higher order, the Big notation results in O(nlog(n))

## Task 4
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

### Worst Case Big-O Notation
 - Time Complexity - O(nlog(n))
 - This algorithm is super-linear time because the sort() function for sorting lists uses time sort algorithm
   which the time complexity for it is O(nlog(n)). The time complexity for the first for loop would be O(3n). The append
   operation in the list functions as a stack, so it always appends at the end of the list result in O(1). The other for loop
   time complexity is O(2n). The operation to convert a list to set is also O(n). Therefore, the total time complexity for
   my solution is O(nlog(n)+ 6n), which worst case is O(nlog(n))


