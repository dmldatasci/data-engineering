# load dependencies
import sys
import pandas as pd

# display the system arguments supplied in our `docker run` command
# to demonstrate custom paramterization of our data pipeline
print(sys.argv)

# instantiate a day variable
day = sys.argv[1]

# some fancy stuff with pandas

# output a success message specific to the day the pipeline was executed
print(f'job finished successfully for day = {day}')