"""NBoost base exceptions"""


class RequestException(Exception):
    """Exception when receiving client request"""


class ResponseException(Exception):
    """Upstream response contains error message"""


class UpstreamConnectionError(Exception):
    """Raised when the upstream host refuses connection"""


class FrontendRequest(RequestException):
    """Client sent frontend request"""


class UnknownRequest(RequestException):
    """Unrecognized url path in request"""


class MissingQuery(RequestException):
    """Could not parse query in request"""
