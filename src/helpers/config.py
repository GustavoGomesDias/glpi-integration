import codecs
from configparser import ConfigParser
from pathlib import Path
from src.errors.NotFoundSection import NotFoundSection

def check_if_section_exists(configParser: ConfigParser, section: str,  option: str):
    if configParser.has_option(section, option) == False:
        raise NotFoundSection('A seção {} ou a opção {} não existem.'.format(section, option))
    else:
       return  configParser.get(section, option)

def set_config(section: str, property_lst: list[str]) -> dict[dict[str, str], str]:
    configParser = ConfigParser()

    CONFIG_PATH = Path(__file__, '..', '..', '..', 'config.ini').resolve()

    with codecs.open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        configParser.readfp(f)
        dict_config_property: dict[dict[str,  str], str] = dict()
        
        lst_property_result: list[str] = [check_if_section_exists(configParser, section, item) for item in property_lst]
        dict_config_property[section] = {key: value for key, value in zip(property_lst, lst_property_result)}
        return dict_config_property
