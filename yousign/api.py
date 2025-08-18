from enum import StrEnum
from requests import request as req
from typing import Optional, Tuple, Union, List
from .uri import BaseURL
from .data import Signature
from .signature_request import SignatureRequest
from .field import Field
from .document import Document
from io import TextIOWrapper
import json


class YouSign:
    token: str

    def __init__(self, token):
        self.token = token

    ACCEPTED_STATUS = {
        "GET": [200],
        "POST": [201],
        "PATCH": [200],
        "DELETE": [204]
    }

    class ContentType(StrEnum):
        NONE = ''
        JSON = 'application/json'
        FORM = 'multipart/form-data'

    def _req(
            self,
            method: str,
            url: str,
            content_type: ContentType = ContentType.NONE,
            ** kwargs
    ):
        kwargs['headers'] = {}

        # add our authroization
        kwargs['headers']['authorization'] = f"Bearer {self.token}"
        kwargs['headers']['accept'] = 'application/json'

        if content_type != YouSign.ContentType.NONE:
            kwargs['headers']['content-type'] = str(content_type)

        debug = kwargs.pop('debug', False)
        res = req(method, url, **kwargs)

        if res.status_code not in YouSign.ACCEPTED_STATUS[method]:
            content = json.loads(res.content)
            raise Exception(
                f'{res.status_code} Not the return awaited \n {content['detail']}'
            )

        content = res.content
        if method != "DELETE":
            content = json.loads(content)

        if debug:
            print("to: ", url)
            print(content)

        return content

    def create_signature(self, name: str, delivery_mode: Signature.DeliveryMode) -> SignatureRequest:
        content = self._req(
            "POST",
            BaseURL.get_signatures(),
            YouSign.ContentType.JSON,
            json={
                'name': name,
                'delivery_mode': str(delivery_mode)
            }
        )

        return SignatureRequest(self, **content)

    def get_signatures(self, id: Optional[str]) -> Union[List[SignatureRequest] | SignatureRequest]:
        contents = self._req("GET", BaseURL.get_signatures(id))

        if id is not None:
            return SignatureRequest(self, **contents)

        signatures = []
        for content in contents['data']:
            signatures.append(SignatureRequest(self, **content))

        return signatures

    def delete_signature(self, id: Optional[str], permanent: bool = False):
        # Already deleted
        if not permanent and self.status == Signature.RequestStatus.DELETED:
            return

        self._req("DELETE",  BaseURL.get_signatures(self.id))

    # Signers

    def create_signer(self, signature_id: str):
        pass

    def delete_signer(self, signature_id: str, signer_id: str) -> None:
        pass

    def get_signers(self, signature_id: str, signer_id: Optional[str]):
        pass

    # Document
    class DocumentArgs:
        files: Tuple[str, TextIOWrapper, str]
        name: str

    def create_document(
            self,
            signature_id: str,
            document: DocumentArgs
    ) -> Document:
        content = self._req(
            "POST",
            BaseURL.get_documents(),
            YouSign.ContentType.NONE,
            files=document.files
        )

        return Document(self, signature_id, **content)

    def delete_document(self, signature_id: str, document_id: str) -> None:
        self._client._req(
            "DELETE",
            BaseURL.get_documents(signature_id, document_id),
            YouSign.ContentType.NONE,
        )

    def get_documents(self, signature_id: str, document_id: Optional[str]) -> Union[List[Document] | Document]:
        self._client._req(
            "DELETE",
            BaseURL.get_documents(signature_id, document_id),
            YouSign.ContentType.NONE,
        )

    # Approvers
    def create_approvers(self):
        pass

    def get_approvers(self):
        pass

    def delete_approvers(self):
        pass

    # Fields

    def create_fields(self, signature_id: str, document_id: str, field: Field, **kwargs) -> Field:
        content = self._req(
            "POST",
            BaseURL.get_fields(signature_id, document_id),
            YouSign.ContentType.JSON,
            json=field.__dict__,
            **kwargs
        )

        return Field(self, **content)

    def delete_fields(self) -> None:
        self._req(
            "POST",
            f"{self._get_url()}/fields",
            YouSign.ContentType.JSON,
            debug=True
        )
