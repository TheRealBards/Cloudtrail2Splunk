# Cloudtrail2Splunk

Parse Cloudtrail JSON to an ingestible format for Splunk

The cloudtrail exports events in JSON fornat, however, each event has a top level that doesn't parse well in Splunk.

Usage:
./cloudtrail2splunk.py --input /path/to/file --output /path/for/output

--output is _optional_

### Note

This script might not work the same in everyones environment. It's a very simple Python script, but hopefully it'll be useful to someone.
