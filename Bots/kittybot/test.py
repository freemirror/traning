import os

from dotenv import load_dotenv


load_dotenv()


secret_token = os.getenv('TOKENY')
print(secret_token)