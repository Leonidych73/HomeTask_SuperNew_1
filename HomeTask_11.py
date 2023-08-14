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
range_values = range(11)
range_list = list(range_values)
print(range_list)

chunk_size = 3
for i in range(0, len(range_list), chunk_size):
   print(range_list[i:i+chunk_size])
