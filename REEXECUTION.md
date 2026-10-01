# PurpleAir–HOBO Third-Party Re-execution

1. Obtain `master_df.csv` and `master_df_with_splits.csv`.
2. Verify the SHA-256 values in the manifest.
3. Run:

```text
python run_purpleair_m2_conformal.py \
  --csv master_df.csv \
  --splits master_df_with_splits.csv \
  --out reexecution_result.json
```

The runner fits M2 on calibration locations only, preserves chronological order, and evaluates the joint unseen-location/future-period set once. It records a 30-day rolling conformal interval with nominal target 97.5%.

Expected exploratory result: joint coverage approximately 95.57%, mean interval width approximately 23.18 C, and `formal_pass: false`. Small floating-point or dependency differences must be recorded rather than silently corrected.
