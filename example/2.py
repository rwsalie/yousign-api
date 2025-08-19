from yousign.client import Client
from dotenv import dotenv_values

config = dotenv_values(".env")

client = Client(config['YOUSIGN_TOKEN'], debug=True)

signatures = client.get_signatures()

for signature in signatures:
    print(signature.data.id)
