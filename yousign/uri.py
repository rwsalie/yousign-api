from typing import Optional
from enum import StrEnum


class BaseURL:
    base = 'https://api-sandbox.yousign.app/v3/signature_requests'

    def get_signatures(
            signature_id: Optional[str],
            **kwargs
    ) -> str:
        url = f"{BaseURL.base}/{signature_id}"

        if signature_id is None:
            return url

        query = kwargs.get('query', None)
        if query is not None and query in ['activate', 'cancel', 'reactivate']:
            return f"{url}/{str(query)}"

        permanent_delete = kwargs.get('permanent_delete', False)
        if permanent_delete:
            return f"{url}/?permanent_delete={permanent_delete}"

    def get_documents(
            signature_id: str,
            document_id: Optional[str],
            **kwargs
    ) -> str:
        url = f"{BaseURL.base}/{signature_id}/documents/{document_id}"

        if document_id is None:
            return url

        query = kwargs.get('query', None)
        if query is not None and query in ['replace', 'download']:
            url = f"{url}/{query}"

            # Some params
            if query == BaseURL.DocumentQuery.DOWNLOAD:
                # To do
                _ = kwargs.get('version', None)
                _ = kwargs.get('archive', None)

        return url

    def get_signers(
            signature_id: str,
            signer_id: Optional[str],
            **kwargs
    ) -> str:
        url = f"{BaseURL.base}/signers/{signature_id}"

        if signer_id is None:
            return url

        query = kwargs.get('query', None)

        allowed_queries = ['send_reminder', 'send_otp', 'identity_verification',
                           'sign', 'unblock_identification']

        if query is not None and query in allowed_queries:
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
