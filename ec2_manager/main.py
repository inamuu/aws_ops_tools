# coding: utf-8

import boto3
import argparse

def setup_ec2():
    print("### setup ec2 ###")

def main():
    parser = argparse.ArgumentParser(
      prog='EC2 Manager',
      usage='python main.py 引数',
      description='AWS EC2 を管理するためのCLIツールです',
      add_help=True,
    )

    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    subparsers = parser.add_subparsers(dest='parser', title='subcomands')
    subparsers.required = True
    
    parser_setup_ec2 = subparsers.add_parser('setup_ec2', help='setup_ec2だよ')
    parser_setup_ec2.set_defaults(fn=setup_ec2)
    
    args = parser.parse_args()
    args.fn()

if __name__ == '__main__': main()