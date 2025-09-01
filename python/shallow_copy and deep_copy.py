"""import copy

my_list=[[23,22,2],["abhay","abhi"]]

k=copy.copy(my_list)

k[0][0]="abhay"

print(k)
print(my_list)"""

import copy

my_list=[[23,22,2],["abhay","abhi"]]

k=copy.deepcopy(my_list)

k[0][0]="abhay"

print(k)
print(my_list)