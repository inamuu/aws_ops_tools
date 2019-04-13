# coding: utf-8

import boto3
import argparse

def setup(args):
    print("### setup ec2 ###")
    print(args)

def main():
    parser = argparse.ArgumentParser(
      prog='EC2 Manager',
      usage='python main.py [setup] [-r/--role] var',
      description='AWS EC2 を管理するためのCLIツールです',
      add_help=True,
    )

    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
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