from uuid import uuid4
from .data import FieldData
from typing import Optional, List
from dataclasses import dataclass, field
from enum import StrEnum
from abc import ABC


class Field(ABC):
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

    type: Type
    signer_id: uuid4
    page: int
    x: int
    y: int


@dataclass
class SignatureField(Field):
    type: str = str(FieldData.Type.SIGNATURE)
    height: int = 37
    width: int = 150
    reason: Optional[str] = None


@dataclass
class MentionField(Field):
    type: str = str(FieldData.Type.MENTION)
    mention: str = ''
    font: Optional[FieldData.Font] = None
    name: Optional[str] = None


@dataclass
class TextField(Field):
    type: str = str(FieldData.Type.TEXT)
    max_length: int = 1
    question: str = 255
    instruction: Optional[str] = None
    font: Optional[FieldData.Font] = None
    name: Optional[str] = None
    default_value: Optional[str] = None
    read_only: bool = False


@dataclass
class ReadOnlyTextField(Field):
    type: str = FieldData.Type.READ_ONLY
    text: str = ""
    font: Optional[FieldData.Font] = None


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
