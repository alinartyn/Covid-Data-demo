from random import seed
from random import randint
from datetime import datetime, time

#RNG with seed = 1
# observe that it's the same darn number every time
seed=time

# # RNG with seed = time
# # observe that at least the number changes every time lol
# seed(datetime.now())

## ATTENTION:
## Before generating your random numbers, DISABLE BOTH seed(...) LINES ABOVE! ;)

# determine length
# Adapted from: https://stackoverflow.com/questions/845058/how-to-get-line-count-of-a-large-file-cheaply-in-python
num_lines = sum(1 for line in open('df_location_sets.csv'))

# generate some integers
# Adapted from: https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/
value = randint(1, num_lines - 2)
print(value)
