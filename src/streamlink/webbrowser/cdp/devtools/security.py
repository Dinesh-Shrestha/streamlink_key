# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all modules.
#
# CDP version: v0.0.1359167
# CDP domain: Security

from __future__ import annotations

import enum
from collections.abc import Generator
from dataclasses import dataclass
from typing import Any

import streamlink.webbrowser.cdp.devtools.network as network
from streamlink.webbrowser.cdp.devtools.util import T_JSON_DICT, event_class


class CertificateId(int):
    """
    An internal certificate ID value.
    """
    def to_json(self) -> int:
        return self

    @classmethod
    def from_json(cls, json: int) -> CertificateId:
        return cls(json)

    def __repr__(self):
        return f"CertificateId({super().__repr__()})"


class MixedContentType(enum.Enum):
    """
    A description of mixed content (HTTP resources on HTTPS pages), as defined by
    https://www.w3.org/TR/mixed-content/#categories
    """
    BLOCKABLE = "blockable"
    OPTIONALLY_BLOCKABLE = "optionally-blockable"
    NONE = "none"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> MixedContentType:
        return cls(json)


class SecurityState(enum.Enum):
    """
    The security level of a page or resource.
    """
    UNKNOWN = "unknown"
    NEUTRAL = "neutral"
    INSECURE = "insecure"
    SECURE = "secure"
    INFO = "info"
    INSECURE_BROKEN = "insecure-broken"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> SecurityState:
        return cls(json)


@dataclass
class CertificateSecurityState:
    """
    Details about the security state of the page certificate.
    """
    #: Protocol name (e.g. "TLS 1.2" or "QUIC").
    protocol: str

    #: Key Exchange used by the connection, or the empty string if not applicable.
    key_exchange: str

    #: Cipher name.
    cipher: str

    #: Page certificate.
    certificate: list[str]

    #: Certificate subject name.
    subject_name: str

    #: Name of the issuing CA.
    issuer: str

    #: Certificate valid from date.
    valid_from: network.TimeSinceEpoch

    #: Certificate valid to (expiration) date
    valid_to: network.TimeSinceEpoch

    #: True if the certificate uses a weak signature algorithm.
    certificate_has_weak_signature: bool

    #: True if the certificate has a SHA1 signature in the chain.
    certificate_has_sha1_signature: bool

    #: True if modern SSL
    modern_ssl: bool

    #: True if the connection is using an obsolete SSL protocol.
    obsolete_ssl_protocol: bool

    #: True if the connection is using an obsolete SSL key exchange.
    obsolete_ssl_key_exchange: bool

    #: True if the connection is using an obsolete SSL cipher.
    obsolete_ssl_cipher: bool

    #: True if the connection is using an obsolete SSL signature.
    obsolete_ssl_signature: bool

    #: (EC)DH group used by the connection, if applicable.
    key_exchange_group: str | None = None

    #: TLS MAC. Note that AEAD ciphers do not have separate MACs.
    mac: str | None = None

    #: The highest priority network error code, if the certificate has an error.
    certificate_network_error: str | None = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = {}
        json["protocol"] = self.protocol
        json["keyExchange"] = self.key_exchange
        json["cipher"] = self.cipher
        json["certificate"] = list(self.certificate)
        json["subjectName"] = self.subject_name
        json["issuer"] = self.issuer
        json["validFrom"] = self.valid_from.to_json()
        json["validTo"] = self.valid_to.to_json()
        json["certificateHasWeakSignature"] = self.certificate_has_weak_signature
        json["certificateHasSha1Signature"] = self.certificate_has_sha1_signature
        json["modernSSL"] = self.modern_ssl
        json["obsoleteSslProtocol"] = self.obsolete_ssl_protocol
        json["obsoleteSslKeyExchange"] = self.obsolete_ssl_key_exchange
        json["obsoleteSslCipher"] = self.obsolete_ssl_cipher
        json["obsoleteSslSignature"] = self.obsolete_ssl_signature
        if self.key_exchange_group is not None:
            json["keyExchangeGroup"] = self.key_exchange_group
        if self.mac is not None:
            json["mac"] = self.mac
        if self.certificate_network_error is not None:
            json["certificateNetworkError"] = self.certificate_network_error
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> CertificateSecurityState:
        return cls(
            protocol=str(json["protocol"]),
            key_exchange=str(json["keyExchange"]),
            cipher=str(json["cipher"]),
            certificate=[str(i) for i in json["certificate"]],
            subject_name=str(json["subjectName"]),
            issuer=str(json["issuer"]),
            valid_from=network.TimeSinceEpoch.from_json(json["validFrom"]),
            valid_to=network.TimeSinceEpoch.from_json(json["validTo"]),
            certificate_has_weak_signature=bool(json["certificateHasWeakSignature"]),
            certificate_has_sha1_signature=bool(json["certificateHasSha1Signature"]),
            modern_ssl=bool(json["modernSSL"]),
            obsolete_ssl_protocol=bool(json["obsoleteSslProtocol"]),
            obsolete_ssl_key_exchange=bool(json["obsoleteSslKeyExchange"]),
            obsolete_ssl_cipher=bool(json["obsoleteSslCipher"]),
            obsolete_ssl_signature=bool(json["obsoleteSslSignature"]),
            key_exchange_group=str(json["keyExchangeGroup"]) if "keyExchangeGroup" in json else None,
            mac=str(json["mac"]) if "mac" in json else None,
            certificate_network_error=str(json["certificateNetworkError"]) if "certificateNetworkError" in json else None,
        )


class SafetyTipStatus(enum.Enum):
    BAD_REPUTATION = "badReputation"
    LOOKALIKE = "lookalike"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> SafetyTipStatus:
        return cls(json)


@dataclass
class SafetyTipInfo:
    #: Describes whether the page triggers any safety tips or reputation warnings. Default is unknown.
    safety_tip_status: SafetyTipStatus

    #: The URL the safety tip suggested ("Did you mean?"). Only filled in for lookalike matches.
    safe_url: str | None = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = {}
        json["safetyTipStatus"] = self.safety_tip_status.to_json()
        if self.safe_url is not None:
            json["safeUrl"] = self.safe_url
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> SafetyTipInfo:
        return cls(
            safety_tip_status=SafetyTipStatus.from_json(json["safetyTipStatus"]),
            safe_url=str(json["safeUrl"]) if "safeUrl" in json else None,
        )


@dataclass
class VisibleSecurityState:
    """
    Security state information about the page.
    """
    #: The security level of the page.
    security_state: SecurityState

    #: Array of security state issues ids.
    security_state_issue_ids: list[str]

    #: Security state details about the page certificate.
    certificate_security_state: CertificateSecurityState | None = None

    #: The type of Safety Tip triggered on the page. Note that this field will be set even if the Safety Tip UI was not actually shown.
    safety_tip_info: SafetyTipInfo | None = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = {}
        json["securityState"] = self.security_state.to_json()
        json["securityStateIssueIds"] = list(self.security_state_issue_ids)
        if self.certificate_security_state is not None:
            json["certificateSecurityState"] = self.certificate_security_state.to_json()
        if self.safety_tip_info is not None:
            json["safetyTipInfo"] = self.safety_tip_info.to_json()
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> VisibleSecurityState:
        return cls(
            security_state=SecurityState.from_json(json["securityState"]),
            security_state_issue_ids=[str(i) for i in json["securityStateIssueIds"]],
            certificate_security_state=CertificateSecurityState.from_json(json["certificateSecurityState"]) if "certificateSecurityState" in json else None,
            safety_tip_info=SafetyTipInfo.from_json(json["safetyTipInfo"]) if "safetyTipInfo" in json else None,
        )


@dataclass
class SecurityStateExplanation:
    """
    An explanation of an factor contributing to the security state.
    """
    #: Security state representing the severity of the factor being explained.
    security_state: SecurityState

    #: Title describing the type of factor.
    title: str

    #: Short phrase describing the type of factor.
    summary: str

    #: Full text explanation of the factor.
    description: str

    #: The type of mixed content described by the explanation.
    mixed_content_type: MixedContentType

    #: Page certificate.
    certificate: list[str]

    #: Recommendations to fix any issues.
    recommendations: list[str] | None = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = {}
        json["securityState"] = self.security_state.to_json()
        json["title"] = self.title
        json["summary"] = self.summary
        json["description"] = self.description
        json["mixedContentType"] = self.mixed_content_type.to_json()
        json["certificate"] = list(self.certificate)
        if self.recommendations is not None:
            json["recommendations"] = list(self.recommendations)
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> SecurityStateExplanation:
        return cls(
            security_state=SecurityState.from_json(json["securityState"]),
            title=str(json["title"]),
            summary=str(json["summary"]),
            description=str(json["description"]),
            mixed_content_type=MixedContentType.from_json(json["mixedContentType"]),
            certificate=[str(i) for i in json["certificate"]],
            recommendations=[str(i) for i in json["recommendations"]] if "recommendations" in json else None,
        )


@dataclass
class InsecureContentStatus:
    """
    Information about insecure content on the page.
    """
    #: Always false.
    ran_mixed_content: bool

    #: Always false.
    displayed_mixed_content: bool

    #: Always false.
    contained_mixed_form: bool

    #: Always false.
    ran_content_with_cert_errors: bool

    #: Always false.
    displayed_content_with_cert_errors: bool

    #: Always set to unknown.
    ran_insecure_content_style: SecurityState

    #: Always set to unknown.
    displayed_insecure_content_style: SecurityState

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = {}
        json["ranMixedContent"] = self.ran_mixed_content
        json["displayedMixedContent"] = self.displayed_mixed_content
        json["containedMixedForm"] = self.contained_mixed_form
        json["ranContentWithCertErrors"] = self.ran_content_with_cert_errors
        json["displayedContentWithCertErrors"] = self.displayed_content_with_cert_errors
        json["ranInsecureContentStyle"] = self.ran_insecure_content_style.to_json()
        json["displayedInsecureContentStyle"] = self.displayed_insecure_content_style.to_json()
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> InsecureContentStatus:
        return cls(
            ran_mixed_content=bool(json["ranMixedContent"]),
            displayed_mixed_content=bool(json["displayedMixedContent"]),
            contained_mixed_form=bool(json["containedMixedForm"]),
            ran_content_with_cert_errors=bool(json["ranContentWithCertErrors"]),
            displayed_content_with_cert_errors=bool(json["displayedContentWithCertErrors"]),
            ran_insecure_content_style=SecurityState.from_json(json["ranInsecureContentStyle"]),
            displayed_insecure_content_style=SecurityState.from_json(json["displayedInsecureContentStyle"]),
        )


class CertificateErrorAction(enum.Enum):
    """
    The action to take when a certificate error occurs. continue will continue processing the
    request and cancel will cancel the request.
    """
    CONTINUE = "continue"
    CANCEL = "cancel"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> CertificateErrorAction:
        return cls(json)


def disable() -> Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Disables tracking security state changes.
    """
    cmd_dict: T_JSON_DICT = {
        "method": "Security.disable",
    }
    yield cmd_dict


def enable() -> Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Enables tracking security state changes.
    """
    cmd_dict: T_JSON_DICT = {
        "method": "Security.enable",
    }
    yield cmd_dict


def set_ignore_certificate_errors(
    ignore: bool,
) -> Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Enable/disable whether all certificate errors should be ignored.

    :param ignore: If true, all certificate errors will be ignored.
    """
    params: T_JSON_DICT = {}
    params["ignore"] = ignore
    cmd_dict: T_JSON_DICT = {
        "method": "Security.setIgnoreCertificateErrors",
        "params": params,
    }
    yield cmd_dict


def handle_certificate_error(
    event_id: int,
    action: CertificateErrorAction,
) -> Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Handles a certificate error that fired a certificateError event.

    :param event_id: The ID of the event.
    :param action: The action to take on the certificate error.
    """
    params: T_JSON_DICT = {}
    params["eventId"] = event_id
    params["action"] = action.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "Security.handleCertificateError",
        "params": params,
    }
    yield cmd_dict


def set_override_certificate_errors(
    override: bool,
) -> Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Enable/disable overriding certificate errors. If enabled, all certificate error events need to
    be handled by the DevTools client and should be answered with ``handleCertificateError`` commands.

    :param override: If true, certificate errors will be overridden.
    """
    params: T_JSON_DICT = {}
    params["override"] = override
    cmd_dict: T_JSON_DICT = {
        "method": "Security.setOverrideCertificateErrors",
        "params": params,
    }
    yield cmd_dict


@event_class("Security.certificateError")
@dataclass
class CertificateError:
    """
    There is a certificate error. If overriding certificate errors is enabled, then it should be
    handled with the ``handleCertificateError`` command. Note: this event does not fire if the
    certificate error has been allowed internally. Only one client per target should override
    certificate errors at the same time.
    """
    #: The ID of the event.
    event_id: int
    #: The type of the error.
    error_type: str
    #: The url that was requested.
    request_url: str

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> CertificateError:
        return cls(
            event_id=int(json["eventId"]),
            error_type=str(json["errorType"]),
            request_url=str(json["requestURL"]),
        )


@event_class("Security.visibleSecurityStateChanged")
@dataclass
class VisibleSecurityStateChanged:
    """
    **EXPERIMENTAL**

    The security state of the page changed.
    """
    #: Security state information about the page.
    visible_security_state: VisibleSecurityState

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> VisibleSecurityStateChanged:
        return cls(
            visible_security_state=VisibleSecurityState.from_json(json["visibleSecurityState"]),
        )


@event_class("Security.securityStateChanged")
@dataclass
class SecurityStateChanged:
    """
    The security state of the page changed. No longer being sent.
    """
    #: Security state.
    security_state: SecurityState
    #: True if the page was loaded over cryptographic transport such as HTTPS.
    scheme_is_cryptographic: bool
    #: Previously a list of explanations for the security state. Now always
    #: empty.
    explanations: list[SecurityStateExplanation]
    #: Information about insecure content on the page.
    insecure_content_status: InsecureContentStatus
    #: Overrides user-visible description of the state. Always omitted.
    summary: str | None

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> SecurityStateChanged:
        return cls(
            security_state=SecurityState.from_json(json["securityState"]),
            scheme_is_cryptographic=bool(json["schemeIsCryptographic"]),
            explanations=[SecurityStateExplanation.from_json(i) for i in json["explanations"]],
            insecure_content_status=InsecureContentStatus.from_json(json["insecureContentStatus"]),
            summary=str(json["summary"]) if "summary" in json else None,
        )
