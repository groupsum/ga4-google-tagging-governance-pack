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

- `spc:ga4-measurement-protocol-request-requirements` - GA4 Measurement Protocol Request Requirements
- `spc:ga4-measurement-protocol-event-requirements` - GA4 Measurement Protocol Event Requirements
- `spc:ga4-recommended-event-parameter-requirements` - GA4 Recommended Event Parameter Requirements
- `spc:gtag-config-command-requirements` - Google Tag Config Command Requirements
- `spc:gtag-event-command-requirements` - Google Tag Event Command Requirements
- `spc:gtag-set-get-command-requirements` - Google Tag Set And Get Command Requirements
- `spc:gtag-consent-command-requirements` - Google Tag Consent Command Requirements
- `spc:google-tag-manager-data-layer-requirements` - Google Tag Manager Data Layer Requirements
- `spc:google-tag-manager-container-deployment-requirements` - Google Tag Manager Container Deployment Requirements
- `spc:ga4-bigquery-export-event-schema-requirements` - GA4 BigQuery Export Event Schema Requirements
- `spc:ga4-bigquery-export-user-property-requirements` - GA4 BigQuery Export User Property Requirements
- `spc:google-consent-mode-storage-signal-requirements` - Google Consent Mode Storage Signal Requirements

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
