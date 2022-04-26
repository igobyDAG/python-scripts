import re

text = 'The rain in Spain'
search = re.search(r'^The.*Spain$', text)
print(search)  # Returns a Match object

# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string

# [] A set of characters	"[a-m]"
# \	 Signals a special sequence (can also be used to escape special characters)	"\d"
# .	 Any character (except newline character)	"he..o"
# ^	 Starts with	"^hello"
# $	 Ends with	"planet$"
# *	 Zero or more occurrences	"he.*o"
# +	 One or more occurrences	"he.+o"
# ?	 Zero or one occurrences	"he.?o"
# {} Exactly the specified number of occurrences	"he.{2}o"
# |	 Either or "falls|stays"
# () Capture and group7G

# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"
# \b	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain" r"ain\b"
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain" r"ain\B"
# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"
# \D	Returns a match where the string DOES NOT contain digits	"\D"
# \s	Returns a match where the string contains a white space character	"\s"
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"

text = 'xyz alice-b@google.com purple monkey'
match = re.search(r'[\w.-]+@[\w.-]+', text)
print(match)
