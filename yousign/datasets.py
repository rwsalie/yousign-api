from yousign.constants import Field as FieldData, Document, Signature
from abc import ABC
from typing import Optional, List

import yousign.constants as ys_const
from uuid import uuid4
from dataclasses import dataclass, field


@dataclass(init=False)
class Info:
    first_name: str
    last_name: str
    email: str
    phone: Optional[str]
    locale: str

    def __init__(self, first_name: str, last_name: str, email: str, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        if phone := kwargs.get('phone', None) is not None:
            self.phone = phone
        self.locale = kwargs.pop('locale', 'en')


@dataclass(init=False)
class DocumentData:
    id: Optional[uuid4]
    name: str
    nature: Document.Nature

    def __init__(self, nature, name: Optional[str] = None, **kwargs):
        self.nature = nature
        self.name = name
        self.id = kwargs.pop('id', None)


@dataclass(init=False)
class SignerData:
    id: uuid4
    info: Info
    status: ys_const.Signer.Status
    signature_link: str
    signature_link_expiration_date: str
    signature_image_preview: str
    redirect_urls: str
    custom_text: str
    delivery_mode: ys_const.DeliveryMode
    fields: List[str]
    signature_level: ys_const.Signature.Level
    signature_authentication_mode: ys_const.Signature.AuthenticationMode
    identification_attestation_id:  str
    sms_notification: str
    email_notification: str
    pre_identity_verification_required: str

    def __init__(self, **kwargs):
        self.info = kwargs.pop('info')
        self.signature_level = kwargs.pop(
            'signature_level', Signature.Level.ELECTRONIC)
        self.signature_authentication_mode = kwargs.pop(
            'signature_authentication_mode', Signature.AuthenticationMode.NONE
        )
        self.fields = kwargs.pop('fields', [])


@dataclass(init=False)
class SignatureData:
    id: Optional[uuid4]
    status: Optional[ys_const.Signature.Status]
    name: str = field(init=True)
    delivery_mode: ys_const.DeliveryMode = field(init=True)
    created_at: Optional[str]
    ordered_signers: Optional[bool]
    ordered_approvers: Optional[bool]
    source: Optional[str]
    email_custom_note: Optional[str]
    timezone: Optional[str]
    reminder_settings: Optional[str]
    expiration_date: Optional[str]
    external_id: Optional[str]
    branding_id: Optional[str]
    custom_experience_id: Optional[str]
    workspace_id: Optional[str]
    audit_trail_locale: Optional[str]
    signers_allowed_to_decline: Optional[bool]
    bulk_send_batch_id: Optional[str]
    email_notification: Optional[str]
    data: Optional[str]

    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', 'Unnamed')
        self.delivery_mode = kwargs.pop(
            'delivery_mode', ys_const.DeliveryMode.NONE)
        for key, value in kwargs.items():
            setattr(self, key, value)


class Field(ABC):
    @dataclass
    class Font:
        class Variant:
            italic: bool = False
            bold: bool = False

        family: str
        color: str
        size: int
        variant: Variant

    type: FieldData.Type
    signer_id: Optional[uuid4]
    document_id: Optional[uuid4]
    page: int
    x: int
    y: int


@dataclass(init=False)
class SignatureField(Field):
    signer_id: Optional[uuid4] = None
    document_id: Optional[uuid4] = None
    x: int = 30
    y: int = 120
    page: int = 1
    type: str = str(FieldData.Type.SIGNATURE)
    height: int = 37
    width: int = 150
    reason: Optional[str] = None


@dataclass
class MentionField(Field):
    type: str = str(FieldData.Type.MENTION)
    mention: str = ''
    font: Optional[Field.Font] = None
    name: Optional[str] = None


@dataclass
class TextField(Field):
    type: str = str(FieldData.Type.TEXT)
    max_length: int = 1
    question: str = 255
    instruction: Optional[str] = None
    font: Optional[Field.Font] = None
    name: Optional[str] = None
    default_value: Optional[str] = None
    read_only: bool = False


@dataclass
class ReadOnlyTextField(Field):
    type: str = FieldData.Type.READ_ONLY
    text: str = ""
    font: Optional[Field.Font] = None


@dataclass
class CheckboxField(Field):
    type: str = FieldData.Type.CHECKBOX
    size: int = 24
    optional: bool = False
    name: Optional[str] = None
    checked: bool = False
    read_only: bool = False


@dataclass
class RadioGroupField(Field):
    @dataclass
    class RadioField(Field):
        size: int = 24
        default_checked: bool = False

    type = FieldData.Type.RADIO_GROUP
    optional: bool = False
    name: Optional[str] = None
    read_only: bool = False
    radios: List[RadioField] = field(default_factory=list)
    radios: List[RadioField] = field(default_factory=list)
