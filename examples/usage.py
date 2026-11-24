"""Find a specification and its downstream path in the installed manifest."""

from ssot_pack_ga4_google_tagging import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:ga4-measurement-protocol-request-requirements"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2001-ga4-measurement-protocol-request-requirements.yaml"
