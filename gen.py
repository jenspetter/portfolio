import argparse
import datetime
import pytz
from siteforge.builder import build_site
from siteforge.json_function_registration import json_func

# Setup args
parser = argparse.ArgumentParser()
parser.add_argument('--content_path', type=str, required=True)
parser.add_argument('--build_registry_path', type=str, required=True)
parser.add_argument('--asset_registry_path', type=str, required=True)
parser.add_argument('--output', type=str, required=True)

"""
Json referenced method to get the year in the Dutch timezone
"""
@json_func
def current_year_nl():
    tz = pytz.timezone('Europe/Amsterdam')
    ct = datetime.datetime.now(tz=tz)
    return ct.year

if __name__ == "__main__":
    args = parser.parse_args()

    build_site(args.content_path, args.build_registry_path, args.asset_registry_path, args.output)