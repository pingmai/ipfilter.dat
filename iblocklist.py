#!/usr/local/bin/python3.7
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
    '-i',
    '--infile',
    default='lists.input',
    help='input file with urls of list of lists'
)
parser.add_argument(
    '-o',
    '--outfile',
    default='ipfilter.dat',
    help='output file'
)
args = parser.parse_args()

nets = set()
for line in open(args.infile, 'r'):
    url = line.split('#')[0].strip()
    if not url:
        continue
    try:
        response = urllib.request.urlopen(url)
    except Exception as e:
        print('%s: ' % url, e)
    else:
        print(url)
        for line in gzip.open(response):
            line = line.decode(errors='ignore').strip()
            a = line.rsplit(':',1)
            if len(a) != 2:
                print('skipped:', line)
                continue
            comment, range = a
            a = range.split('-')
            if len(a) != 2:
                print('bad ip range:', line)
                continue
            start,end = map(ipaddress.IPv4Address, a)
            nets.update(list(ipaddress.summarize_address_range(start, end)))

outf = open(args.outfile,'w')
for n in ipaddress.collapse_addresses(nets):
    print("%s - %s" % (n[0],n[-1]), file=outf)

outf.close()
