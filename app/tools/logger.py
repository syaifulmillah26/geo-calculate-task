import logging

"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""


def log_info(message, filename):
    """ This method used to save log message """
    logging.basicConfig(
        filename=filename,
        filemode='a',
        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        datefmt='%H:%M:%S',
        level=logging.INFO
    )

    logging.info(message)
    pass
