import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='logbook.log',
    encoding='utf-8',
    format='[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s: %(lineno)d] => %(message)s',
    datefmt='%d.%m.%Y %H:%M:%S ',
)
