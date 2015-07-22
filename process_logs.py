import argparse
import re

parser = argparse.ArgumentParser(description='Read logs and total some number')

# Process our arguments
parser.add_argument("regex")
parser.add_argument("index", help="Index of the regex group you want to count",
        type=int)
parser.add_argument("filename")
args = parser.parse_args()

# Grab the requested file
log_file = open(args.filename, 'r')

# Read each line of the file
p = re.compile(args.regex)
for line in log_file:
    print line
    # See whether it matches the regex
    matches = p.search(line)
    # Get the number from the line if it does
    if matches:
        target = matches.group(args.index)
        print "Match is %s" % target

# Add the number to our total
# Return our total

log_file.close()
