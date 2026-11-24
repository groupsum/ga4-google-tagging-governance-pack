"""Inspect the installed pack identity."""

from ssot_pack_ga4_google_tagging import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:ga4-google-tagging"
print(metadata["origin"]["id"])
