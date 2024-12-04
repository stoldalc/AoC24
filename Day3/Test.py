# Python program to find all the matches
import re
 
subject = "My Geeksfomul(rGeeks is my GeeksforGeeks none of your GeeksforGeeks"
 
# Template instantiations for
# extracting the matching pattern.
match = re.search("mul\(", subject)
i = 1
 
while match:
    print("\nMatched string is", match.group(0))
    print("and it is found at position", match.start())
    i += 1
 
    # suffix to find the rest of the string.
    subject = subject[(match.end()):]
    match = re.search("mul\(", subject)