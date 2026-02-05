"""Generate the SDK based on the aas-core-meta model and the snippets."""

import argparse
import os
import pathlib
import subprocess
import sys


def _generate_sdk(
    meta_model_path: pathlib.Path,
    snippet_path: pathlib.Path,
    sdk_path: pathlib.Path,
) -> None:
    subprocess.run(
        [
            "aas-core-codegen",
            "--model_path",
            str(meta_model_path),
            "--snippets_dir",
            str(snippet_path),
            "--output_dir",
            str(sdk_path),
            "--target",
            "python",
        ],
        check=True,
    )


def main() -> int:
    """Execute the main routine."""
    this_dir = pathlib.Path(os.path.realpath(__file__)).parent
    repo_root = this_dir.parent.parent.parent

    default_meta_model_path = os.path.relpath(
        str(this_dir / "meta_model.py"), os.getcwd()
    )
    default_target_dir = os.path.relpath(str(repo_root / "aas_core3_1"), os.getcwd())

    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--meta_model", help="Path to the meta-model", default=default_meta_model_path
    )
    parser.add_argument(
        "--target",
        help="Path to the directory where the generated files are to be output",
        default=default_target_dir,
    )
    args = parser.parse_args()

    this_dir = pathlib.Path(os.path.realpath(__file__)).parent
    snippet_dir = this_dir / "snippets"

    meta_model_path = pathlib.Path(args.meta_model)
    target_dir = pathlib.Path(args.target)

    _generate_sdk(
        meta_model_path=meta_model_path, snippet_path=snippet_dir, sdk_path=target_dir
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
