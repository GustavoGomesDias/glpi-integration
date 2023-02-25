import os

absolute_path = os.path.dirname(__file__)
SERVICES = "src"
MODELS = "src"
HELPERS = "src"
os.path.join(absolute_path, SERVICES)
# os.path.join(absolute_path, MODELS)
# os.path.join(absolute_path, HELPERS)


from src.helpers.config import set_config

if __name__ == '__main__':
    set_config('whats', ['accessTokenWhats', 'phoneNumber'], absolute_path)
