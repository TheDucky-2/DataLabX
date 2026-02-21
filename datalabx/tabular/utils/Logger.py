def datalabx_logger(name:str='datalabx'):
    """A simple reusable logger that logs module name, level, message and
    timestamp."""
    import logging

    # setting logger name to datalabx, which can be replaced by any module name
    logger = logging.getLogger(name)
    
    # making sure we avoid duplication of logs
    if not logger.handlers:

        # setting minimum log level to INFO, skipping DEBUG for now
        logger.setLevel(logging.INFO)

        # creating a handler that displays messages on console
        handler = logging.StreamHandler()
        
        # setting formatter
        formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

        # applying format to handler
        handler.setFormatter(formatter)

        # adding handler to logger
        logger.addHandler(handler)
        
    return logger

