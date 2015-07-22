import argparse

parser = argparse.ArgumentParser(description='Read logs and total some number')
parser.parse_args()

# Grab the requested file
# Read each line of the file
# See whether it matches the regex
# Get the number from the line if it does
# Add the number to our total
# Return our total
