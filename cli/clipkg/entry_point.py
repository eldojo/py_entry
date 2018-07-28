import sys
import argparse
import logging

logger = logging.getLogger()

def printo():
    print(args.loglevel)
    print(args.foo)

def parse_arg():
    logging.basicConfig()
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--foo', default='este valor de foo es default, perro', help='Foo argument is setted to (default: %(default)s)')
    parser.add_argument('-l', '--loglevel', default='DEBUG',help='logging level, choices are: %(choices)s', choices=['INFO', 'DEBUG', 'WARNING'])
    args = parser.parse_args()
    logger.setLevel(getattr(logging, args.loglevel))
    return(args)

if __name__=='__main__':
    args = parse_arg()
    logger.info('This is an INFO')
    logger.debug('This is a DEBUG')
    logger.warning('This is a WARNING')
    logger.error('This is an ERROR')
    printo()