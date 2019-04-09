import os, sys
from os.path import join, dirname
from dotenv import load_dotenv

sys.path.append(os.path.join(os.path.dirname(__file__), 'site-packages'))

import boto3
from boto3.session import Session
import json
from datetime import datetime

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def logdump(outputfile):
    session = Session(profile_name=os.environ.get("profile_name"))
    client = session.client('logs', region_name=os.environ.get("region_name"))

    response = client.get_log_events (
        logGroupName = os.environ.get("logGroupName"),
        logStreamName = os.environ.get("logStreamName")
    )

    if os.path.isfile(outputfile) == True:
        os.remove(outputfile)

    f = open(outputfile, "a")
    for list in response['events']:
        f.write((list['message']))

    return

def main():
    #logdump(os.environ.get("logfilepath"))
    f = open(os.environ.get("logfilepath"), "r")
    json_data = json.load(f)
    print(type(json_data))
    #for i in json_data:
    #    print(i)

if __name__ == "__main__": main()