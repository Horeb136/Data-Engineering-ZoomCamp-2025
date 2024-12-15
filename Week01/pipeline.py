import sys 
import pandas as pd 

# sys.argv allows to pass arguments to the script from the commandline
print(sys.argv)

# sys.argv[0] > name of the file
# sys.argv[1] > first argument passed
day = sys.argv[1]

# Here is the pandas code

print(f"Job finished successfully for for day = {day}")