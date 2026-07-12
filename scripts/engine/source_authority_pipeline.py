from scripts.engine.evidence_weight_engine import EvidenceWeightEngine
from scripts.engine.provenance_engine import ProvenanceEngine
from scripts.engine.source_authority_engine import SourceAuthorityEngine
from scripts.engine.source_classifier import SourceClassifier
from scripts.models.evidence import Evidence
from scripts.models.provenance import Provenance
from scripts.models.source import Source


class SourceAuthorityPipeline:
    """
    BotAtlas Layer 5 source authority orchestration boundary.

    Classifies and scores a source, records provenance,
    and converts source trust into evidence confidence.

    This pipeline does not resolve claims.
    """

    def __init__(self):
        self.classifier = SourceClassifier()
        self.authority = SourceAuthorityEngine()
        self.provenance = ProvenanceEngine()
        self.weight_engine = EvidenceWeightEngine()

    def process(
        self,
        source: Source,
        evidence: Evidence,
        discovery_method: str = "UNKNOWN",
        content_type: str = "UNKNOWN",
        content_reference: str | None = None,
    ) -> tuple[Source, Provenance, Evidence]:
        source = self.classifier.classify(source)
        source = self.authority.score(source)

        provenance = self.provenance.create(
            source=source,
            discovery_method=discovery_method,
            content_type=content_type,
            content_reference=content_reference,
        )

        evidence = self.weight_engine.weight(
            evidence=evidence,
            source=source,
        )

        return source, provenance, evidence
