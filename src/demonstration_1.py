"""
Define a function that transforms a given string into a new string where the
original string was split into strings of a specified size.

For example:
If the input string was this:

"supercalifragilisticexpialidocious"

and the specified size was 3, then the return string would be:

"sup erc ali fra gil ist ice xpi ali doc iou s"

The assumptions we are making about our input are the following:

- The input string's length is always greater than zero.
- The string has no spaces.
- The specified size is always a positive integer.
"""
def split_in_parts(s, part_length):
    # Your code here
    # we need to split the input string into smaller chungs of whatever 
    # the specified size is

    # init an output array 
    # const output = [];
    # output = []
    while s:
        yield s[:part_length]
        s = s[part_length:]
print(split_in_parts('supercalifragilisticexpialidocious', 3))

    # iterate over characters in the input string 
    
        # keep a counter that will count up to the 'part_length' characters
        # check if our counter == part_length
            # then we have collected enough chars for a single substring
            # add that collected substring to an array
            # start counter over agaun
        # otherwise
            # increment our counter
            # add current character to the substring we're building up


    # return output array (or list)





# Your code here

