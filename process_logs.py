import argparse
import re

parser = argparse.ArgumentParser(description='Read logs and total some number')

# Process our arguments
parser.add_argument("regex")
parser.add_argument("filename")
args = parser.parse_args()

# Grab the requested file
log_file = open(args.filename, 'r')

# Read each line of the file
p = re.compile(args.regex)
for line in log_file:
    print line
    # See whether it matches the regex
    matches = p.findall(line)
    for index, match in enumerate(matches):
        print "Match number %d is %s" % (index, match)

# Get the number from the line if it does
# Add the number to our total
# Return our total

log_file.close()
