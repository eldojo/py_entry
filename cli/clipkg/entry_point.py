import sys
import argparse
import logging

logger = logging.getLogger()

if __name__=='__main__':
    logging.basicConfig()
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--foo', help='get some foo!')
    parser.add_argument('-l', '--loglevel', help='logging level', choices=['INFO', 'DEBUG', 'WARNING'])
    args = parser.parse_args()
    logger.setLevel(getattr(logging, args.loglevel))
    logger.info('This is an INFO')
    logger.debug('This is a DEBUG')
    logger.warning('This is a WARNING')
    logger.error('This is an ERROR')
