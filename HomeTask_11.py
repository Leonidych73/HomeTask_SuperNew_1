"""HomeTask11.

write generator function that has as input some range value and chunk_size
produces output as lists with len == chunk size
Example:
Call:  chunk_generator(range(11), chunk_size=3) ->
Output:  [0, 1, 2]
         [3, 4, 5]
         [6, 7, 8]
         [9, 10]
"""
def chunk_generator(range_values, chunk_size):  # create a generator
    range_list = list(range_values)  # create list
    for i in range(0, len(range_list), chunk_size):  # iterate over range from 0 to length = len(range_list) with step = chunk_size
        yield range_list[i:i+chunk_size]  # return a slice equal to the length of the chunk

my_generator = chunk_generator(range(20), chunk_size=5)  # call the generator
for chunk in my_generator:  # iterate over each chunk and print it out
    print(chunk)




