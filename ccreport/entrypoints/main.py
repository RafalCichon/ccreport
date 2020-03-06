from ..ccreport import collect
import argparse
import logging


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-o', '--organization-url', required=True, type=str)
    arg_parser.add_argument('-p', '--project-name', required=True, type=str)
    arg_parser.add_argument('-t', '--token', required=True, type=str)
    arg_parser.add_argument('-d', '--definition-pattern', type=str)
    arg_parser.add_argument('-b', '--branch-name', default='master', type=str)
    args = arg_parser.parse_args()

    log_format = '%(asctime)s|%(levelname)s|%(name)s|%(message)s'
    logging.basicConfig(format=log_format, level=logging.INFO)

    collect(args=args)
