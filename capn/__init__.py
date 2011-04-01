from capn.config import get_configuration, DEFAULT_TYPE

configuration = get_configuration()
default_type = configuration['settings'].get('default_type', DEFAULT_TYPE)



