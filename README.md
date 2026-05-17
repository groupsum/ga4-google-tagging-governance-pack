# ssot-pack-ga4-google-tagging

Installable SSOT governance pack for GA4 Measurement Protocol, Google tag, Google Tag Manager, GA4 event parameters, and BigQuery exports.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:ga4-google-tagging`
- Priority: `P1.1`
- PyPI package: `ssot-pack-ga4-google-tagging`
- Import package: `ssot_pack_ga4_google_tagging`
- GitHub repository: `groupsum/ga4-google-tagging-governance-pack`
- Reservation owner: `extension-pack:ssot-pack-ga4-google-tagging`

## Domain Focus

GA4 And Google Tagging Governance

## Authority Sources

- GA4 Measurement Protocol reference
- GA4 Measurement Protocol events reference
- Google tag gtag.js API reference
- Google Tag Manager developer documentation
- GA4 BigQuery Export schema
- Google Consent Mode overview

## Included ADRs

- `adr:ga4-measurement-protocol-boundary` - GA4 Measurement Protocol Boundary
- `adr:ga4-event-taxonomy-authority` - GA4 Event Taxonomy Authority
- `adr:google-tag-runtime-policy` - Google Tag Runtime Policy
- `adr:google-tag-manager-deployment-policy` - Google Tag Manager Deployment Policy
- `adr:ga4-bigquery-export-evidence-policy` - GA4 BigQuery Export Evidence Policy
- `adr:google-consent-mode-signal-policy` - Google Consent Mode Signal Policy

## Included SPECs

- `spc:ga4-measurement-protocol-contract` - GA4 Measurement Protocol Contract
- `spc:gtag-api-contract` - Google Tag API Contract
- `spc:ga4-event-parameter-contract` - GA4 Event Parameter Contract
- `spc:ga4-bigquery-export-contract` - GA4 BigQuery Export Contract

## Install With uv

```bash
uv add ssot-pack-ga4-google-tagging
uv add ssot-registry ssot-pack-ga4-google-tagging
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install ssot-pack-ga4-google-tagging
uvx --from ssot-registry ssot pack sync . ssot-pack-ga4-google-tagging
uv run ssot adr list .
uv run ssot spec list .
```

## Programmatic Usage

```python
from ssot_pack_ga4_google_tagging import load_document_manifest

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
```

## Resources

- GitHub repository: https://github.com/groupsum/ga4-google-tagging-governance-pack
- PyPI package: https://pypi.org/project/ssot-pack-ga4-google-tagging/
- SSOT Registry: https://pypi.org/project/ssot-registry/
