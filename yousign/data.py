from enum import StrEnum
from dataclasses import dataclass
from typing import List, Optional
from uuid import uuid4


@dataclass
class Info:
    first_name: str
    last_name: str
    email: str
    locale: str


class FieldData:
    class Type(StrEnum):
        SIGNATURE = 'signature'
        MENTION = 'mention'
        TEXT = 'text'
        CHECKBOX = 'checkbox'
        RADIO_GROUP = 'radio_group'
        READ_ONLY = 'read_only_text'

    @dataclass
    class Font:
        class Variant:
            italic: bool = False
            bold: bool = False

        family: str
        color: str
        size: int
        variant: Variant


class DocumentNature(StrEnum):
    ATTACHMENT = 'attachment'
    SIGNABLE = 'signable_document'


class SignerStatus(StrEnum):
    INITIATED = 'initiated'
    DECLINED = 'declined'
    NOTIFIED = 'notified'
    VERIFIED = 'verified'
    PROCESSING = 'processing'
    CONSENT_GIVEN = 'consent_given'
    SIGNED = 'signed'
    ABORTED = 'aborted'
    ERROR = 'error'


class DeliveryMode(StrEnum):
    NONE = 'none',
    EMAIL = 'email'


class Signer:
    @dataclass
    class Data:
        id: uuid4
        info: Info
        status: SignerStatus
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


class Document:
    @dataclass
    class Data:
        pass


class Signature:
    class Level(StrEnum):
        ELECTRONIC = 'electronic_signature'
        ADVANCE_ELECTORNIC = 'advanced_electronic_signature'
        QUALIFIED_ELECTRONIC = 'qualified_electronic_signature'

    class AuthenticationMode(StrEnum):
        NONE = 'no_otp'
        OTP_EMAIL = 'otp_email'
        OTP_SMS = 'otp_sms'

    class RequestStatus(StrEnum):
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
        status: RequestStatus
        name: str
        delivery_mode: DeliveryMode
        created_at: str
        ordered_signers: bool
        ordered_approvers: bool
        signers: List[Signer]
        labels: List[str]
        documents: List[Document]
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
