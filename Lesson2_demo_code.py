#Make a function that prints
# *****
# ****
# ***
# **
# *

# *
# **
# ***
# ****
# *****

num = 4
while(num >= 0):
    for stars in range(num+1):
        print('*', end='')
    print(end='\n')
    num-=1

