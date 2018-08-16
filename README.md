# ipfilter.dat
Create ipfilter.dat from iblocklist.com.
Requires python3.3 or above.
'lists.input' contains all lists from iblocklist.com.
Run './iblocklist.py' will generate 'ipfilter.dat' silently.
'-D' will generate debug messages to stderr.
```
[2212]ping@porte:~/git/iblocklist$ ./iblocklist.py -h
usage: iblocklist.py [-h] [-D DEBUG] [-i INFILE] [-o OUTFILE]

download block list from iblocklist.com convert to cidr addresses.

optional arguments:
  -h, --help            show this help message and exit
  -D DEBUG, --debug DEBUG
                        debug flag (default: 0)
  -i INFILE, --infile INFILE
                        input file with urls of lists (default: lists.input)
  -o OUTFILE, --outfile OUTFILE
                        output file (def

[2213]ping@porte:~/git/iblocklist$ ./iblocklist.py -D 2
http://list.iblocklist.com/lists/atma/atma
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/bluetack/ads-trackers-and-bad-pr0n
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/bluetack/bad-peers
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/bluetack/bogon
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/bluetack/dshield
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/bluetack/edu
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/bluetack/for-non-lan-computers
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/bluetack/forum-spam
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/bluetack/hijacked
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/bluetack/iana-multicast
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/bluetack/iana-private
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/bluetack/iana-reserved
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/bluetack/level-1
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/bluetack/level-2
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/bluetack/level-3
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/bluetack/microsoft
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/bluetack/proxy
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/bluetack/range-test
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/bluetack/spider
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/bluetack/spyware
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/bluetack/web-exploit
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/bluetack/webexploit-forumspam
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/cidr-report/bogon
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/dchubad/faker
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/dchubad/hacker
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/dchubad/pedophiles
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/dchubad/spammer
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/peerblock/rapidshare
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/spamhaus/drop
skipped line: # List distributed by iblocklist.com
skipped line:
skipped line: # Spamhaus DROP List - (c) 2011 The Spamhaus Project
skipped line:
http://list.iblocklist.com/lists/tbg/bogon
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/tbg/business-isps
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/tbg/educational-institutions
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/tbg/general-corporate-ranges
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/tbg/hijacked
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/tbg/primary-threats
skipped line: # List distributed by iblocklist.com
skipped line:
http://list.iblocklist.com/lists/tbg/search-engines
skipped line: # List distributed by iblocklist.com
skipped line:
```
