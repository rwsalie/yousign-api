from .api import YouSign
from .url import BaseURL
from .data import DeliveryMode
from .signer import Signer
from .document import Document
from typing import List, Union, Self, Union, Optional
from enum import StrEnum
from uuid import uuid4
from dataclasses import dataclass


class Signature:
    class Level(StrEnum):
        ELECTRONIC = 'electronic_signature'
        ADVANCE_ELECTORNIC = 'advanced_electronic_signature'
        QUALIFIED_ELECTRONIC = 'qualified_electronic_signature'

    class AuthenticationMode(StrEnum):
        NONE = 'no_otp'
        OTP_EMAIL = 'otp_email'
        OTP_SMS = 'otp_sms'

    class Status(StrEnum):
        DRAFT = 'draft'
        ONGOING = 'ongoin'
        DONE = 'done'
        DELETED = 'deleted'
        EXPIRED = 'expired'
        CANCEL = 'canceled'
        APPROVAL = 'approval'
        REJECTED = 'rejected'
        DECLINED = 'declined'

    @dataclass
    class Data:
        status: Status
        name: str
        delivery_mode: DeliveryMode
        created_at: str
        ordered_signers: bool
        ordered_approvers: bool
        signers: List[Signer.Data]
        labels: List[str]
        documents: List[Document.Data]
        sender: Optional[str]
        approvers: List[str]
        source: str
        email_custom_note: str
        timezone: str
        reminder_settings: str
        expiration_date: Optional[str]
        external_id: str
        branding_id: str
        custom_experience_id: str
        workspace_id: str
        audit_trail_locale: str
        signers_allowed_to_decline: bool
        bulk_send_batch_id: str
        email_notification: str
        data: Optional[str] = None

    _client: YouSign
    id: uuid4
    data: Data

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
        self.data = self._client.save_signature(self.id, self.data)
