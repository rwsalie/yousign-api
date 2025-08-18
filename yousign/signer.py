from typing import Self
from .data import Signer
from .signature_request import SignatureRequest
from .api import YouSign


class Signer:
    _client: YouSign
    _signature: SignatureRequest
    data: Signer.Data

    def __init__(self, client: YouSign, signature: SignatureRequest, **kwargs) -> Self:
        self._client = client
        self._signature = signature
        self.data = Signer.Data(**kwargs)

    def delete(self):
        self._client.delete_signer(self._signature.id, self.id)

    def save(self):
        pass
