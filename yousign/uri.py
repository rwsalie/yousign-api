from typing import Optional
from enum import StrEnum


class BaseURL:
    base = 'https://api-sandbox.yousign.app/v3/signature_requests'

    class SignatureQuery(StrEnum):
        ACTIVATE = 'activate'
        CANCEL = 'cancel'
        REACTIVATE = 'reactivate'

    def get_signatures(
            signature_id: Optional[str],
            permanent_delete: Optional[bool],
            query: Optional[SignatureQuery] = None) -> str:
        url = f"{BaseURL.base}/{signature_id}"

        if signature_id is None:
            return url

        if query is not None:
            return f"{url}/{str(query)}"

        if permanent_delete is not None:
            return f"{url}/?permanent_delete={permanent_delete}"

    class DocumentQuery(StrEnum):
        DOWNLOAD = 'download'
        REPLACE = 'replace'

    def get_documents(
            signature_id: str,
            document_id: Optional[str],
            query: Optional[DocumentQuery] = None
    ) -> str:
        url = f"{BaseURL.base}/{signature_id}/documents/{document_id}"

        if document_id is None:
            return url

        if query is not None:
            return f"{url}/{str(query)}"

        return url

    class SignersQuery(StrEnum):
        SEND_REMINDER = 'send_reminder'
        SEND_OTP = 'send_otp'
        IDENTITY_VERIFICATION = 'identity_verification'
        SIGN = 'sign'
        UNBLOCK_IDENTIFICATION = 'unblock_identification'

    def get_signers(
            signature_id: str,
            signer_id: Optional[str],
            query: Optional[SignersQuery] = None
    ) -> str:
        url = f"{BaseURL.base}/signers/{signature_id}"

        if signer_id is None:
            return url

        if query is not None:
            return f"{url}/{query}"

        return url

    def get_approvers(
            signature_id: str,
            approver_id: Optional[str],
            send_reminder: bool = False
    ) -> str:
        url = f"{BaseURL.get_signatures(id)}/approvers/{approver_id}"

        if approver_id is None:
            return url

        if send_reminder:
            return f"{url}/send_reminder"

        return url

    def get_fields(
            signature_id: str,
            document_id: str,
            field_id: Optional[str],
            answer: bool = False
    ) -> str:
        url = f"{BaseURL.get_documents(signature_id)}/documents/{document_id}/fields/{field_id}"

        if field_id is None:
            return url

        if answer:
            url += "/answer"

        return url

    def get_followers(signature_id: str) -> str:
        return f"{BaseURL.get_signatures(signature_id)}/followe"
