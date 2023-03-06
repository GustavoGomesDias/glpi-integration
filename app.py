# from src.helpers.relative_path import add_src_folders
from src.services.services.WhatsApp import WhatsApp


if __name__ == '__main__':
   whats = WhatsApp()

   # whats.login_in_app()

   whats.send_message('', 'oi')