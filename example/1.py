from yousign.client import Client
from yousign.constants import DeliveryMode
from yousign.datasets import SignatureData, DocumentData, SignerData
from yousign.constants import Document

from dotenv import dotenv_values

config = dotenv_values(".env")

client = Client(config['YOUSIGN_TOKEN'], debug=True)

new_signature = client.create_signature(
    SignatureData(
        name='Test',
        delivery_mode=DeliveryMode.EMAIL
    )
)

new_document = new_signature.add_doc(
    DocumentData(
        name='test',
        nature=Document.Nature.SIGNABLE
    ),
    file=('test.pdf', open("test.pdf", "rb"), 'application/pdf')
)

new_signer = new_signature.add_signer(
    SignerData(

    )
)

# Then Active your sign
new_signature.activate()
