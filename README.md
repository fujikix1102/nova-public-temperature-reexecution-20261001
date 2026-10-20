# NOVA Public Temperature Re-execution

This repository contains a reproducible PurpleAir–HOBO temperature evaluation bundle for the NOVA validation framework. It is an exploratory numerical re-execution, not a sensor calibration or safety certification.

## Scope

- Fixed public input bundle and predefined evaluation splits
- Conformal interval and coverage diagnostics
- Input provenance and reproducibility checks
- formal_pass=false unless independent external reproduction and calibration evidence are established

## Reproduction

Install the pinned dependencies from requirements.txt and follow REEXECUTION.md. Record the operating system, Python and dependency versions, input SHA-256, runner revision, output SHA-256, result counts, and failure reasons.

## Interpretation

Reported coverage and interval widths are valid only for the stated data, split, and assumptions. They do not establish general sensor accuracy, physical calibration, or performance outside the supplied dataset. Automated workflow execution is not human third-party reproduction.

## Evidence status

This bundle is benchmark/exploratory evidence. External calibration, independent data, and human third-party execution remain separate requirements.
