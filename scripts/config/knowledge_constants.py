"""
BotAtlas Knowledge Domain Constants

Canonical constants used by the Knowledge Processing Layer.

These values should never be hard-coded throughout the engine layer.
"""

# ==========================================================
# Content Types
# ==========================================================

CONTENT_TYPE_TEXT = "TEXT"
CONTENT_TYPE_HTML = "HTML"
CONTENT_TYPE_MARKDOWN = "MARKDOWN"
CONTENT_TYPE_PDF = "PDF"
CONTENT_TYPE_JSON = "JSON"
CONTENT_TYPE_IMAGE = "IMAGE"
CONTENT_TYPE_VIDEO = "VIDEO"

# ==========================================================
# Acquisition Methods
# ==========================================================

ACQUISITION_METHOD_RETRIEVER = "RETRIEVER"
ACQUISITION_METHOD_API = "API"
ACQUISITION_METHOD_CRAWLER = "CRAWLER"
ACQUISITION_METHOD_MANUAL = "MANUAL"

# ==========================================================
# Discovery Methods
# ==========================================================

DISCOVERY_METHOD_SEARCH = "SEARCH"
DISCOVERY_METHOD_API = "API"
DISCOVERY_METHOD_MANUAL = "MANUAL"

# ==========================================================
# Candidate Types
# ==========================================================

CANDIDATE_TYPE_UNKNOWN = "UNKNOWN"
CANDIDATE_TYPE_PRODUCT = "PRODUCT"
CANDIDATE_TYPE_MANUFACTURER = "MANUFACTURER"
CANDIDATE_TYPE_DOCUMENT = "DOCUMENT"
CANDIDATE_TYPE_VIDEO = "VIDEO"
CANDIDATE_TYPE_ARTICLE = "ARTICLE"