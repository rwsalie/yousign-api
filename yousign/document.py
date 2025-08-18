from .data import DocumentNature
from .field import Field
from .signature_request import SignatureRequest
from .api import YouSign
from typing import Optional, List, Union
from uuid import uuid4
from io import TextIOWrapper
from dataclasses import dataclass


@dataclass
class Document:
    id: uuid4
    _client: YouSign
    _signature: SignatureRequest
    file: TextIOWrapper
    nature: DocumentNature

    def __init__(self, client: YouSign, signature: SignatureRequest, **kwargs):
        self._signature_id = signature
        self._client = client
        self.id = kwargs['id']

    def get_fields(self, id: Optional[str]) -> Union[List[Field] | Field]:
        pass

    def add_field(self, field: Field):
        pass

    def remove_field(self, field: Field):
        pass

    def remove_field(self, field: Field) -> None:
        self._client.remove_field(self._signature.data.id, self.id, field.id)
