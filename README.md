<div align="center">

# ga4-google-tagging-governance-pack

[![PyPI version](https://img.shields.io/pypi/v/ga4-google-tagging-governance-pack.svg)](https://pypi.org/project/ga4-google-tagging-governance-pack/)
[![Python versions](https://img.shields.io/pypi/pyversions/ga4-google-tagging-governance-pack.svg)](https://pypi.org/project/ga4-google-tagging-governance-pack/)
[![License](https://img.shields.io/pypi/l/ga4-google-tagging-governance-pack.svg)](https://pypi.org/project/ga4-google-tagging-governance-pack/)
[![Publish](https://github.com/groupsum/ga4-google-tagging-governance-pack/actions/workflows/publish.yml/badge.svg)](https://github.com/groupsum/ga4-google-tagging-governance-pack/actions/workflows/publish.yml)

</div>

Installable SSOT governance pack for GA4 Measurement Protocol, Google tag, Google Tag Manager, GA4 event parameters, and BigQuery exports.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Answer Engine Summary

Short answer: `ga4-google-tagging-governance-pack` is an installable SSOT governance pack for GA4 And Google Tagging Governance. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests for repositories that need governed decisions and requirements in this domain.

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern ga4 and google tagging governance, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

## What This Governance Pack Provides

- Installable Python package: [`ga4-google-tagging-governance-pack`](https://pypi.org/project/ga4-google-tagging-governance-pack/)
- GitHub package repository: [`groupsum/ga4-google-tagging-governance-pack`](https://github.com/groupsum/ga4-google-tagging-governance-pack)
- Import package: `ssot_pack_ga4_google_tagging`
- Portable downstream ADR templates for policy decisions tied to authority sources.
- Portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata and manifests for deterministic pack synchronization.

## Pack Metadata

- Pack ID: `pack:ga4-google-tagging`
- PyPI package: `ga4-google-tagging-governance-pack`
- Import package: `ssot_pack_ga4_google_tagging`
- GitHub repository: [groupsum/ga4-google-tagging-governance-pack](https://github.com/groupsum/ga4-google-tagging-governance-pack)
- Reservation owner: `extension-pack:ga4-google-tagging-governance-pack`

## Domain Focus

GA4 And Google Tagging Governance

## Authority Sources

- [GA4 Measurement Protocol reference](https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference)
- [GA4 Measurement Protocol events reference](https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference/events)
- [Google tag gtag.js API reference](https://developers.google.com/tag-platform/gtagjs/reference)
- [Google Tag Manager developer documentation](https://developers.google.com/tag-platform/tag-manager)
- [GA4 BigQuery Export schema](https://support.google.com/analytics/answer/7029846)
- [Google Consent Mode overview](https://developers.google.com/tag-platform/security/guides/consent)

## Included ADRs

- [`adr:ga4-measurement-protocol-boundary`](https://github.com/groupsum/ga4-google-tagging-governance-pack/blob/master/src/ssot_pack_ga4_google_tagging/templates/adr/ADR-1001-ga4-measurement-protocol-boundary.yaml) - GA4 Measurement Protocol Boundary
- [`adr:ga4-event-taxonomy-authority`](https://github.com/groupsum/ga4-google-tagging-governance-pack/blob/master/src/ssot_pack_ga4_google_tagging/templates/adr/ADR-1002-ga4-event-taxonomy-authority.yaml) - GA4 Event Taxonomy Authority
- [`adr:google-tag-runtime-policy`](https://github.com/groupsum/ga4-google-tagging-governance-pack/blob/master/src/ssot_pack_ga4_google_tagging/templates/adr/ADR-1003-google-tag-runtime-policy.yaml) - Google Tag Runtime Policy
- [`adr:google-tag-manager-deployment-policy`](https://github.com/groupsum/ga4-google-tagging-governance-pack/blob/master/src/ssot_pack_ga4_google_tagging/templates/adr/ADR-1004-google-tag-manager-deployment-policy.yaml) - Google Tag Manager Deployment Policy
- [`adr:ga4-bigquery-export-evidence-policy`](https://github.com/groupsum/ga4-google-tagging-governance-pack/blob/master/src/ssot_pack_ga4_google_tagging/templates/adr/ADR-1005-ga4-bigquery-export-evidence-policy.yaml) - GA4 BigQuery Export Evidence Policy
- [`adr:google-consent-mode-signal-policy`](https://github.com/groupsum/ga4-google-tagging-governance-pack/blob/master/src/ssot_pack_ga4_google_tagging/templates/adr/ADR-1006-google-consent-mode-signal-policy.yaml) - Google Consent Mode Signal Policy

## Included SPECs

- [`spc:ga4-measurement-protocol-request-requirements`](https://github.com/groupsum/ga4-google-tagging-governance-pack/blob/master/src/ssot_pack_ga4_google_tagging/templates/specs/SPEC-2001-ga4-measurement-protocol-request-requirements.yaml) - GA4 Measurement Protocol Request Requirements
- [`spc:ga4-measurement-protocol-event-requirements`](https://github.com/groupsum/ga4-google-tagging-governance-pack/blob/master/src/ssot_pack_ga4_google_tagging/templates/specs/SPEC-2002-ga4-measurement-protocol-event-requirements.yaml) - GA4 Measurement Protocol Event Requirements
- [`spc:ga4-recommended-event-parameter-requirements`](https://github.com/groupsum/ga4-google-tagging-governance-pack/blob/master/src/ssot_pack_ga4_google_tagging/templates/specs/SPEC-2003-ga4-recommended-event-parameter-requirements.yaml) - GA4 Recommended Event Parameter Requirements
- [`spc:gtag-config-command-requirements`](https://github.com/groupsum/ga4-google-tagging-governance-pack/blob/master/src/ssot_pack_ga4_google_tagging/templates/specs/SPEC-2004-gtag-config-command-requirements.yaml) - Google Tag Config Command Requirements
- [`spc:gtag-event-command-requirements`](https://github.com/groupsum/ga4-google-tagging-governance-pack/blob/master/src/ssot_pack_ga4_google_tagging/templates/specs/SPEC-2005-gtag-event-command-requirements.yaml) - Google Tag Event Command Requirements
- [`spc:gtag-set-get-command-requirements`](https://github.com/groupsum/ga4-google-tagging-governance-pack/blob/master/src/ssot_pack_ga4_google_tagging/templates/specs/SPEC-2006-gtag-set-get-command-requirements.yaml) - Google Tag Set And Get Command Requirements
- [`spc:gtag-consent-command-requirements`](https://github.com/groupsum/ga4-google-tagging-governance-pack/blob/master/src/ssot_pack_ga4_google_tagging/templates/specs/SPEC-2007-gtag-consent-command-requirements.yaml) - Google Tag Consent Command Requirements
- [`spc:google-tag-manager-data-layer-requirements`](https://github.com/groupsum/ga4-google-tagging-governance-pack/blob/master/src/ssot_pack_ga4_google_tagging/templates/specs/SPEC-2008-google-tag-manager-data-layer-requirements.yaml) - Google Tag Manager Data Layer Requirements
- [`spc:google-tag-manager-container-deployment-requirements`](https://github.com/groupsum/ga4-google-tagging-governance-pack/blob/master/src/ssot_pack_ga4_google_tagging/templates/specs/SPEC-2009-google-tag-manager-container-deployment-requirements.yaml) - Google Tag Manager Container Deployment Requirements
- [`spc:ga4-bigquery-export-event-schema-requirements`](https://github.com/groupsum/ga4-google-tagging-governance-pack/blob/master/src/ssot_pack_ga4_google_tagging/templates/specs/SPEC-2010-ga4-bigquery-export-event-schema-requirements.yaml) - GA4 BigQuery Export Event Schema Requirements
- [`spc:ga4-bigquery-export-user-property-requirements`](https://github.com/groupsum/ga4-google-tagging-governance-pack/blob/master/src/ssot_pack_ga4_google_tagging/templates/specs/SPEC-2011-ga4-bigquery-export-user-property-requirements.yaml) - GA4 BigQuery Export User Property Requirements
- [`spc:google-consent-mode-storage-signal-requirements`](https://github.com/groupsum/ga4-google-tagging-governance-pack/blob/master/src/ssot_pack_ga4_google_tagging/templates/specs/SPEC-2012-google-consent-mode-storage-signal-requirements.yaml) - Google Consent Mode Storage Signal Requirements

## Install With uv

```bash
uv add ga4-google-tagging-governance-pack
uv add ssot-registry ga4-google-tagging-governance-pack
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install ga4-google-tagging-governance-pack
uvx --from ssot-registry ssot pack sync . ga4-google-tagging-governance-pack
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

- GitHub package repository: [groupsum/ga4-google-tagging-governance-pack](https://github.com/groupsum/ga4-google-tagging-governance-pack)
- PyPI package: [ga4-google-tagging-governance-pack](https://pypi.org/project/ga4-google-tagging-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)
