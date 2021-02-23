"""
Sometimes you don't want to iterate through a whole file. For that, there's a different file method, .readline(), which
 will only read a single line at a time. If the entire document is read line by line in this way subsequent calls
 to .readline() will not throw an error but will start returning an empty string ("").

Note: The .readline() method will read a single line. Each subsequent call will read the line after the last call.
"""

with open('just_the_first.txt') as first_line_doc:
    first_line = first_line_doc.readline()

print(first_line)

"""
just_the_first.txt

You do look, my son, in a moved sort,
As if you were dismayd: be cheerful, sir.
Our revels now are ended. These our actors,
As I foretold you, were all spirits and
Are melted into air, into thin air:
And, like the baseless fabric of this vision,
The cloud-cappd towers, the gorgeous palaces,
The solemn temples, the great globe itself,
Ye all which it inherit, shall dissolve
And, like this insubstantial pageant faded,
Leave not a rack behind. We are such stuff
As dreams are made on, and our little life
Is rounded with a sleep. Sir, I am vexd;
Bear with my weakness; my, brain is troubled:
Be not disturbd with my infirmity:
If you be pleased, retire into my cell
And there repose: a turn or two I'll walk,
To still my beating mind.
"""