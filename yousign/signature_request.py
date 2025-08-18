from .api import YouSign
from .url import BaseURL
from .data import Signature
from typing import List, Union, Self, Union, Optional
from uuid import uuid4


class SignatureRequest:
    _client: YouSign
    id: uuid4
    data: Signature.Data

    def activate(self) -> None:
        self._client._req("POST", BaseURL.get_signatures(self.id))

    def reactivate(self) -> None:
        self._client._req(
            "POST",
            BaseURL.get_documents(self.id),
        )

    def update(self) -> None:
        content = self._client.get_signatures(id)
        self.data = Signature.Data(**content)

    def delete(self) -> None:
        self._client.delete_signature(self.id)

    def cancel(self) -> None:
        self._client._req("POST", BaseURL.get_signatures(self.id))

    def add_signer(self) -> None:
        self._client.create_signer()

    def save(self) -> None:
        self._client._req(
            "PATCH",
            BaseURL.get_signatures(self.id),
            YouSign.ContentType.JSON
        )
