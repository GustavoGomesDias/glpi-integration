# from src.helpers.relative_path import add_src_folders
from src.services.services.GLPI import GLPI
from src.helpers.config import set_config


if __name__ == '__main__':
   glpi_config = set_config('glpi', ['user', 'password', 'accessToken'])
   ticker_manager = GLPI(glpi_config['glpi']['user'], glpi_config['glpi']['password'], glpi_config['glpi']['accessToken'], 'https://woood.with19.glpi-network.cloud/apirest.php')
   ticker_manager.get_ticket_info(1)