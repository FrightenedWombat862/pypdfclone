"""
All errors/exceptions pypdf raises and all of the warnings it uses.

Please note that broken PDF files might cause other Exceptions.
"""


class DeprecationError(Exception):
    """Raised when a deprecated feature is used."""

    pass


class DependencyError(Exception):
    """Raised when a required dependency (a library or module that PyPDF depends on) is not available or cannot be imported."""

    pass


class PyPdfError(Exception):
    """Base class for all exceptions raised by PyPDF."""

    pass


class PdfReadError(PyPdfError):
    """Raised when there is an issue reading a PDF file."""

    pass


class PageSizeNotDefinedError(PyPdfError):
    """Raised when the page size of a PDF document is not defined."""

    pass


class PdfReadWarning(UserWarning):
    """Issued when there is a potential issue reading a PDF file, but it can still be read."""

    pass


class PdfStreamError(PdfReadError):
    """Raised when there is an issue reading the stream of data in a PDF file."""

    pass


class ParseError(Exception):
    """Raised when there is an issue parsing (analyzing and understanding the structure and meaning of) a PDF file."""

    pass


class FileNotDecryptedError(PdfReadError):
    """Raised when a PDF file that has been encrypted (meaning it requires a password to be accessed) has not been successfully decrypted."""

    pass


class WrongPasswordError(FileNotDecryptedError):
    """Raised when the wrong password is used to try to decrypt an encrypted PDF file."""

    pass


class EmptyFileError(PdfReadError):
    """Raised when a PDF file is empty or has no content."""

    pass


STREAM_TRUNCATED_PREMATURELY = "Stream has ended unexpectedly"