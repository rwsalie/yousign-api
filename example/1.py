from yousign3.client import Client
from yousign3.constants import DeliveryMode
from yousign3.datasets import SignatureData, DocumentData, SignerData, Info
from yousign3.type.fields.signature import SignatureField
from yousign3.constants import Document, Signature

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
        info=Info(
            first_name="rwsalie",
            last_name="someone",
            email="yourmail@mail.com",
        ),
        signature_level=Signature.Level.ELECTRONIC,
        fields=[
            SignatureField()
            .set_reason("ee")
            .set_document_id(new_document.data.id)
            .conclude()
        ]
    )
)

# Then Active your sign
new_signature.activate()
