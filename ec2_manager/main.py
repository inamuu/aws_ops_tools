# coding: utf-8

import os, sys
import argparse
import boto3
import yaml
from os.path import join, dirname
from dotenv import load_dotenv
from boto3.session import Session


def loadenv():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    ec2 = boto3.session.Session(profile_name=os.environ.get("profile_name")).client('ec2')
    return ec2

def setup(args):
    with open('test.yaml') as file:
        yml = yaml.full_load(file)

    role             = args.role
    all              = yml[role]
    imageid          = yml[role]['imageid']
    rolecount        = yml[role]['count']
    instancetype     = yml[role]['instancetype']
    keyname          = yml[role]['keyname']
    securitygroupids = yml[role]['securitygroupids']
    subnetid         = yml[role]['subnetid']
    nametag          = yml[role]['nametag']

    print("\nEC2 Setup start..\n")
    print("all  : %s" % all)
    print("role : %s" % nametag)

    ec2      = loadenv()
    instance = ec2.run_instances(
        ImageId           = imageid,
        MinCount          = rolecount,
        MaxCount          = rolecount,
        InstanceType      = instancetype,
        KeyName           = keyname,
        SecurityGroupIds  = [securitygroupids],
        SubnetId          = subnetid,
        TagSpecifications = [
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': nametag
                    },
                ]
            },
        ],
    )
    print("\nEC2 Setup Finish..\n")

def main():
    parser = argparse.ArgumentParser(
        prog        = 'EC2 Manager',
        usage       = 'python main.py setup [-r/--role] ...',
        description = 'AWS EC2 を管理するためのCLIツールです',
        add_help    = True,
    )

    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    subparsers = parser.add_subparsers(dest='parser', title='subcomands')
    subparsers.required = True
    
    parser_setup = subparsers.add_parser('setup', help='EC2をセットアップします。')
    parser_setup.add_argument('-r', '--role', required=True)
    parser_setup.set_defaults(handler=setup)
    
    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()

if __name__ == '__main__': main()
