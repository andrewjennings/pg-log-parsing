import argparse
import locale
import re

locale.setlocale(locale.LC_ALL, 'en_US')
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
log_sum = 0
for line in log_file:
    print line
    # See whether it matches the regex
    matches = p.search(line)
    # Get the number from the line if it does
    if matches:
        target = matches.group(args.index)
        print "Match is %s" % target
        # Add the number to our total
        log_sum += int(target)

# Return our total
print "Total value of log is %s" % locale.format("%d", log_sum, grouping=True)

log_file.close()
