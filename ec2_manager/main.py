# coding: utf-8

import os, sys
import argparse
import boto3
import yaml
from os.path import join, dirname
from dotenv import load_dotenv
from boto3.session import Session

def run_instances(args, dryrun):
    imageid          = args['imageid']
    rolecount        = args['count']
    instancetype     = args['instancetype']
    keyname          = args['keyname']
    securitygroupids = args['securitygroupids']
    subnetid         = args['subnetid']
    nametag          = args['nametag']

    ec2      = loadenv()
    instance = ec2.run_instances(
        DryRun            = dryrun,
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

    privateip = instance['Instances'][0]['PrivateIpAddress']
    print("プライベートIPアドレスは %s が割当られました" % privateip)

def loadenv():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    ec2 = boto3.session.Session(profile_name=os.environ.get("profile_name")).client('ec2')
    return ec2

def setup(args):
    with open('role.yaml') as file:
        yml = yaml.full_load(file)

    role    = args.role
    all     = yml[role]
    nametag = yml[role]['nametag']
    dryrun  = args.dryrun

    while True:
        for key, value in all.items():
            print("%s: %s" % (key ,value))
        choice = input("\n上記設定で %s インスタンスを作成しますか？ [y/n]: " % nametag).lower()
        if choice in ['y', 'yes']:
            print("\n%s インスンタンスの作成を開始します.." % nametag)
            run_instances(all, dryrun)
            print("\n%s インスンタンスを作成しました" % nametag)
            return True
        elif choice in ['n', 'no']:
            print('\nインスタンス作成を中止しました')
            return False


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
    parser_setup.add_argument('--dryrun', action='store_true')
    parser_setup.set_defaults(handler=setup)
    
    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()

if __name__ == '__main__': main()
