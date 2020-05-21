#!/usr/bin/python3

import os
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", help="Enter the path to the input file.", type=str, required=True)
parser.add_argument("--output", help="Enter the path for the output file. This is an optional field.", type=str, required=False)

args = parser.parse_args()

if os.path.exists(args.input):
    with open(args.input) as f:
        try:
            fil = json.loads(f.read())
        except Exception as e:
            print(e)
            sys.exit(1)
else:
    print('Are you sure the file exists?')
    sys.exit(1)

if 'Records' in fil.keys():
    if args.output:
        fil_name = args.output
    else:
        fil_name = args.input+'_parsed'

    with open(fil_name, 'w') as f:
        for x in fil['Records']:
            f.write(json.dumps(x))
            f.write('\n')

    print('Successfully written JSON events to {}'.format(fil_name))
else:
    print('Not sure this is a JSON export from AWS Cloudtrail?')
    sys.exit(1)
