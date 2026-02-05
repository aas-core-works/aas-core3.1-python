"""Update to the latest meta-model and the latest test data."""

import argparse
import os
import pathlib
import subprocess
import sys


def main() -> int:
    """Execute the main routine."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.parse_args()

    repo_root = pathlib.Path(os.path.realpath(__file__)).parent.parent.parent

    print("Downloading the latest meta-model...")
    subprocess.check_call(
        [
            sys.executable,
            str(repo_root / "dev" / "dev_scripts" / "download_aas_core_meta_model.py"),
        ],
        cwd=str(repo_root),
    )

    print("Generating the code...")
    subprocess.check_call(
        [
            sys.executable,
            str(repo_root / "dev" / "dev_scripts" / "regenerate_code.py"),
        ],
        cwd=str(repo_root),
    )

    print("Re-formatting the code...")
    subprocess.check_call(
        [sys.executable, "-m", "black", "aas_core3_1", "dev/tests"], cwd=str(repo_root)
    )

    print("Downloading the latest test data...")
    subprocess.check_call(
        [
            sys.executable,
            str(repo_root / "dev" / "dev_scripts" / "download_latest_test_data.py"),
        ],
        cwd=str(repo_root),
    )

    print("Re-recording the test data...")
    subprocess.check_call(
        [sys.executable, str(repo_root / "dev" / "dev_scripts" / "rerecord_tests.py")],
        cwd=str(repo_root),
    )

    print("Running the pre-commit to check that everything worked...")
    subprocess.check_call(
        [
            sys.executable,
            str(repo_root / "dev" / "continuous_integration" / "precommit.py"),
            "--overwrite",
        ],
        cwd=str(repo_root),
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
