# coding: utf-8

import boto3
import argparse

def setup():
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
    
    parser_setup = subparsers.add_parser('setup', help='EC2をセットアップします。')
    parser_setup.set_defaults(fn=setup)
    
    args = parser.parse_args()
    args.fn()

if __name__ == '__main__': main()