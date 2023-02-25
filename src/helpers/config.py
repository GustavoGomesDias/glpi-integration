import codecs
from configparser import ConfigParser
from pathlib import Path


def set_config(section: str, property_lst: list[str]) -> dict[dict[str, str], str]:
    configParser = ConfigParser()

    CONFIG_PATH = Path(__file__, '..', '..', '..', 'config.ini').resolve()

    with codecs.open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        configParser.readfp(f)
        dict_config_property: dict[dict[str,  str], str] = dict()
        
        lst_property_result: list[str] = [configParser.get(section, item) for item in property_lst]
        dict_config_property[section] = {key: value for key, value in zip(property_lst, lst_property_result)}
        
        return dict_config_property
