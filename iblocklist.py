#!/usr/bin/env python3
import argparse
import gzip
import sys
import urllib.request
import ipaddress

parser = argparse.ArgumentParser(
    description='''download block list from iblocklist.com
    convert to cidr addresses.
    ''',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument(
    '-D',
    '--debug',
    type=int,
    default=0,
    help='debug flag'
)
parser.add_argument(
    '-i',
    '--infile',
    default='lists.input',
    help='input file with urls of lists'
)
parser.add_argument(
    '-o',
    '--outfile',
    default='ipfilter.dat',
    help='output file'
)
args = parser.parse_args()

def dprint(level, *a, **kwargs):
    if args.debug >= level:
        print(*a, file=sys.stderr, **kwargs)

nets = []
for line in open(args.infile, 'r'):
    url = line.split('#')[0].strip()
    if not url:
        continue
    try:
        response = urllib.request.urlopen(url)
    except Exception as e:
        dprint(0,'%s: ' % url, e)
    else:
        dprint(1,url)
        for line in gzip.open(response):
            line = line.decode(errors='ignore').strip()
            a = line.rsplit(':',1)
            if len(a) != 2:
                dprint(2,'skipped line:', line)
                continue
            comment, range = a
            a = range.split('-')
            if len(a) != 2:
                dprint(2,'bad ip range:', line)
                continue
            start,end = map(ipaddress.IPv4Address, a)
            nets.extend(list(ipaddress.summarize_address_range(start, end)))

outf = open(args.outfile,'w')
for n in ipaddress.collapse_addresses(set(nets)):
    print("%s - %s" % (n[0],n[-1]), file=outf)

outf.close()
