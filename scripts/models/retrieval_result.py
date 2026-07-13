from dataclasses import dataclass


@dataclass(frozen=True)
class RetrievalResult:
    """
    Raw provider-neutral retrieval output.

    Retrieval results are not evidence and carry no trust assignments.
    """

    title: str
    url: str
    snippet: str = ""
    provider: str = "UNKNOWN"
