# Library  for importing login information for using
# with the twitter/X app /API.

from dotenv import load_dotenv
import os


def get_app_name() -> str | None:
    load_dotenv()
    app_name = os.getenv('TWITTER_NAME')
    return app_name

def get_app_id() -> str | None:
    load_dotenv()
    app_id = os.getenv('TWITTER_APP_ID')
    return app_id

def get_api_key() -> str | None:
    load_dotenv()
    api_key = os.getenv('API_KEY')
    return api_key

def get_api_key_secret() -> str | None:
    load_dotenv()
    api_key_secret = os.getenv('API_KEY_SECRET')
    return api_key_secret

def get_bearer_token() -> str | None:
    load_dotenv()
    bearer_token = os.getenv('BEARER_TOKEN')
    return bearer_token

def get_access_token() -> str | None:
    load_dotenv()
    access_token = os.getenv('ACCESS_TOKEN')
    return access_token

def get_access_token_secret() -> str | None:
    load_dotenv()
    access_token_secret = os.getenv('ACESS_TOKEN_SECRET')
    return access_token_secret



if __name__ =="__main__":
    name = get_access_token_secret()
    print(name)