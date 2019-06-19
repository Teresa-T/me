"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
#I think this assigns the list of strings into the variable some_words
some_words = ['what', 'does', 'this', 'line', 'do', '?']#string values were input in order as the list specified
#prints the values in some_words one by one
for word in some_words:
    print(word)# the variable word is assigned each value and printed
#prints the values in some_words one by one
for x in some_words:
    print(x)# the variable x is assigned each value and printed
#prints the entire list on one line
print(some_words)#prints the exact formatting of the value, in square brackets and quotes
#will print 'some_words contains more than 3 words' as the condition is True
if len(some_words) > 3:
    print('some_words contains more than 3 words')#prints 'some_words' contains more than 3 words
#prints the system, node, release version, machine and processor of this device
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())
#runs the function
usefulFunction()#prints uname_result containing system, node, release, version, machine, processor.
