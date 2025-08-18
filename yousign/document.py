from .field import Field
from .signature_request import SignatureRequest
from .api import YouSign
from typing import Optional, List, Union
from uuid import uuid4
from dataclasses import dataclass
from enum import StrEnum


class Document:
    class Nature(StrEnum):
        ATTACHMENT = 'attachment'
        SIGNABLE = 'signable_document'

    @dataclass
    class Data:
        pass

    id: uuid4
    _client: YouSign
    _signature: SignatureRequest
    data: Data

    def __init__(self, client: YouSign, signature: SignatureRequest, **kwargs):
        self._signature_id = signature
        self._client = client
        self.id = kwargs['id']

    def update(self) -> None:
        self.data = Document.Data(**self._client.save_document())

    def get_fields(self, id: Optional[str]) -> Union[List[Field] | Field]:
        pass

    def add_field(self, field: Field):
        pass

    def remove_field(self, field: Field) -> None:
        self._client.remove_field(self._signature.data.id, self.id, field.id)
