from dataclasses import fields
from pathlib import Path

from scripts.engine.acquisition_engine import AcquisitionEngine
from scripts.engine.candidate_deduplicator import CandidateDeduplicator
from scripts.engine.discovery_engine import DiscoveryEngine
from scripts.engine.discovery_pipeline import DiscoveryPipeline
from scripts.models.acquired_material import AcquiredMaterial
from scripts.models.discovery_candidate import DiscoveryCandidate


FORBIDDEN_TRUST_FIELDS = {
    "verified",
    "verification_status",
    "confidence_score",
    "quality_score",
    "authority_score",
    "reputation_score",
    "selected",
}

LAYER_6_FILES = [
    Path("scripts/models/discovery_candidate.py"),
    Path("scripts/models/acquired_material.py"),
    Path("scripts/engine/discovery_engine.py"),
    Path("scripts/engine/discovery_pipeline.py"),
    Path("scripts/engine/acquisition_engine.py"),
    Path("scripts/engine/candidate_deduplicator.py"),
]


def audit_file_inventory():
    print("\n=== FILE INVENTORY ===")

    for path in LAYER_6_FILES:
        print(path)
        assert path.exists(), f"Missing Layer 6 file: {path}"

    print("PASS: Layer 6 file inventory")


def audit_contracts():
    print("\n=== CONTRACT AUDIT ===")

    contracts = [
        DiscoveryCandidate,
        AcquiredMaterial,
    ]

    for contract in contracts:
        contract_fields = {
            field.name
            for field in fields(contract)
        }

        leaked = FORBIDDEN_TRUST_FIELDS.intersection(
            contract_fields
        )

        print(
            contract.__name__,
            sorted(contract_fields),
        )

        assert not leaked, (
            f"{contract.__name__} contains trust fields: "
            f"{sorted(leaked)}"
        )

    print("PASS: Layer 6 contracts contain no trust fields")


def audit_behavior():
    print("\n=== BEHAVIOR AUDIT ===")

    discovery = DiscoveryEngine()
    deduplicator = CandidateDeduplicator()
    acquisition = AcquisitionEngine()

    candidates = [
        discovery.discover(
            "Figure 02",
            "https://www.figure.ai/robot/",
            "SEED",
            "ROBOT",
        ),
        discovery.discover(
            "Figure duplicate",
            "figure.ai/robot",
            "SEARCH",
            "ROBOT",
        ),
        discovery.discover(
            "Atlas",
            "https://bostondynamics.com/atlas/",
            "SEED",
            "ROBOT",
        ),
    ]

    unique = deduplicator.deduplicate(candidates)

    materials = [
        acquisition.acquire(
            candidate=candidate,
            content=(
                f"AUDIT MATERIAL FOR "
                f"{candidate.candidate_name}"
            ),
            acquisition_method="AUDIT_FIXTURE",
            content_type="TEXT",
        )
        for candidate in unique
    ]

    print("DISCOVERED:", len(candidates))
    print("DEDUPLICATED:", len(unique))
    print("ACQUIRED:", len(materials))

    assert len(candidates) == 3
    assert len(unique) == 2
    assert len(materials) == 2

    for obj in [*unique, *materials]:
        for forbidden in FORBIDDEN_TRUST_FIELDS:
            assert not hasattr(obj, forbidden), (
                f"Trust leakage detected: "
                f"{type(obj).__name__}.{forbidden}"
            )

    print(
        "PASS: Layer 6 behavior preserves trust boundary"
    )



def audit_discovery_pipeline():
    print("\n=== DISCOVERY PIPELINE AUDIT ===")

    pipeline = DiscoveryPipeline()

    materials = pipeline.discover_and_process(
        candidate_name="Figure 02",
        candidate_url="https://www.figure.ai/",
        discovery_method="AUDIT",
        candidate_type="ROBOT",
        content="Figure 02 product reference material",
    )

    assert len(materials) == 1, (
        f"Expected 1 acquired material, found {len(materials)}"
    )

    material = materials[0]
    material_fields = {
        field.name for field in fields(material)
    }

    leaked_fields = material_fields.intersection(
        FORBIDDEN_TRUST_FIELDS
    )

    assert not leaked_fields, (
        "DiscoveryPipeline leaked trust fields: "
        + ", ".join(sorted(leaked_fields))
    )

    print(f"PIPELINE OUTPUTS: {len(materials)}")
    print("PASS: DiscoveryPipeline preserves Layer 6 trust boundary")



def audit_runtime_trust_injection():
    print("\n=== RUNTIME TRUST INJECTION AUDIT ===")

    candidate = DiscoveryCandidate(
        candidate_name="Figure 02",
        candidate_url="https://www.figure.ai/",
        discovery_method="ADVERSARIAL",
        candidate_type="ROBOT",
    )

    pipeline = DiscoveryPipeline()

    materials = pipeline.discover_and_process(
        candidate_name="Figure 02",
        candidate_url="https://www.figure.ai/",
        discovery_method="ADVERSARIAL",
        candidate_type="ROBOT",
        content="Figure 02 product reference material",
    )

    assert len(materials) == 1

    targets = [
        ("DiscoveryCandidate", candidate),
        ("AcquiredMaterial", materials[0]),
    ]

    violations = []

    for label, obj in targets:
        for field_name in FORBIDDEN_TRUST_FIELDS:
            try:
                setattr(obj, field_name, True)
            except (AttributeError, TypeError):
                continue

            if hasattr(obj, field_name):
                violations.append(
                    f"{label}.{field_name}"
                )

    assert not violations, (
        "Runtime trust injection possible:\n"
        + "\n".join(sorted(violations))
    )

    print(
        "PASS: Layer 6 runtime trust injection blocked"
    )


def audit_static_trust_assignments():
    print("\n=== STATIC TRUST ASSIGNMENT AUDIT ===")

    assignment_patterns = [
        f"{field_name} ="
        for field_name in FORBIDDEN_TRUST_FIELDS
    ]

    violations = []

    for path in LAYER_6_FILES:
        text = path.read_text()

        for pattern in assignment_patterns:
            if pattern in text:
                violations.append(
                    f"{path}: {pattern}"
                )

    assert not violations, (
        "Layer 6 trust assignments detected:\n"
        + "\n".join(violations)
    )

    print("PASS: no Layer 6 trust assignments detected")


def main():
    print("\n=== BOTATLAS LAYER 6 EVIDENCE GATE ===")

    audit_file_inventory()
    audit_contracts()
    audit_behavior()
    audit_discovery_pipeline()
    audit_runtime_trust_injection()
    audit_static_trust_assignments()

    print("\n=== ARCHITECTURE RESULT ===")
    print("Layer 6: PASS")
    print("Trust boundary: PASS")
    print(
        "PASS: BOTATLAS LAYER 6 EVIDENCE GATE"
    )


if __name__ == "__main__":
    main()
