import argparse

parser = argparse.ArgumentParser(description='Read logs and total some number')

# Grab the requested file
parser.add_argument("filename")
args = parser.parse_args()
log_file = open(args.filename, 'r')

# Read each line of the file
for line in log_file:
    print line

# See whether it matches the regex
# Get the number from the line if it does
# Add the number to our total
# Return our total
