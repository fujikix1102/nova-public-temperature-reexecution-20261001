# Online execution options

## Recommended: GitHub Actions

Put this directory in a repository together with `master_df.csv` and `master_df_with_splits.csv`, then run **Actions → PurpleAir-HOBO reexecution → Run workflow**. The workflow pins Python 3.12.7, verifies both input hashes, runs the frozen runner, and uploads `reexecution_result.json`.

GitHub documents `setup-python` as the recommended way to make Python versions consistent in Actions.

## Binder

Binder can launch the same repository interactively in a browser. Pin the repository commit in the Binder URL and record the displayed commit, runtime versions, input hashes, and output hash.

## Google Colab

Colab is easiest for a manual run. Upload the two input files and runner, execute the hash checks first, then save the output JSON. Record the notebook revision, runtime Python version, input hashes, and output hash. Colab execution alone is weaker evidence than a pinned GitHub Actions run.
