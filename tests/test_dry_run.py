"""The dry run must finish with the checker passing."""
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import dry_run  # noqa: E402


class DryRun(unittest.TestCase):
    def test_dry_run_passes(self):
        with tempfile.TemporaryDirectory() as d:
            code = dry_run.main(["--root", str(Path(d) / "studio"), "--quiet", "--keep"])
            self.assertEqual(code, 0)
            self.assertTrue((Path(d) / "studio" / "businesses" / "gulf-fidic-claim-pack" / "ledger.md").exists())


if __name__ == "__main__":
    unittest.main()
