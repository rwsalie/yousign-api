from typing import Self, List
from .data import DeliveryMode, Info
from .signature import Signature
from .api import YouSign
from dataclasses import dataclass
from enum import StrEnum
import uuid4


class Signer:
    class Status(StrEnum):
        INITIATED = 'initiated'
        DECLINED = 'declined'
        NOTIFIED = 'notified'
        VERIFIED = 'verified'
        PROCESSING = 'processing'
        CONSENT_GIVEN = 'consent_given'
        SIGNED = 'signed'
        ABORTED = 'aborted'
        ERROR = 'error'

    @dataclass
    class Data:
        id: uuid4
        info: Info
        status: Status
        signature_link: str
        signature_link_expiration_date: str
        signature_image_preview: str
        redirect_urls: str
        custom_text: str
        delivery_mode: DeliveryMode
        fields: List[str]
        signature_level: 'Signature.Level'
        signature_authentication_mode: 'Signature.AuthenticationMode'
        identification_attestation_id:  str
        sms_notification: str
        email_notification: str
        pre_identity_verification_required: str

    _client: YouSign
    _signature: Signature
    data: Data

    def __init__(self, client: YouSign, signature: Signature, **kwargs) -> Self:
        self._client = client
        self._signature = signature
        self.data = Signer.Data(**kwargs)

    def update(self):
        content = self._client.get_signers(self.id)
        self.data = Signer.Data(**content)

    def delete(self):
        self._client.delete_signer(self._signature.id, self.id)

    def save(self):
        pass
