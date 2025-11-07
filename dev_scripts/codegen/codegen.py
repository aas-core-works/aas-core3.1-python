"""Generate the SDK based on the aas-core-meta model and the snippets."""

import pathlib
import os
import argparse
import sys


def main() -> int:
    """Execute the main routine."""
    parser = argparse.ArgumentParser(description=__doc__)
    args = parser.parse_args()

    this_dir = pathlib.Path(os.path.realpath(__file__)).parent

    return 0

if __name__ == "__main__":
    sys.exit(main())
