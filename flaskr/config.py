def _init():
    import sys, os, json
    import logging, logging.config

    # get sys env $RISK_CALC_ENV
    #env = os.environ.get('RISK_CALC_ENV') or 'test'

    # load module config
    dir = os.path.dirname(__file__)
    #app_config_filename = os.path.join(dir, 'config/app_config.json')
    logger_config_filename = os.path.join(dir, 'config/logger_config.json')

    # load chosen config to Dict: current
    #with open(app_config_filename, 'r') as f:
    #    config_dict = json.load(f)
    #    current = config_dict[env]

    # load and initialize system logger
    with open(logger_config_filename, 'r') as f:
        logger_config = json.load(f)
        logging.config.dictConfig(logger_config)

    #return current

_init()

