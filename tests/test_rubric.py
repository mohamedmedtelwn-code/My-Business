"""Tests for tools/rubric.py - scoring arithmetic."""
import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))

import rubric  # noqa: E402
import studio  # noqa: E402

CFG = dict(studio.DEFAULT_CONFIG)


class Scoring(unittest.TestCase):
    def test_weights_sum_to_twenty_and_max_is_100(self):
        self.assertEqual(sum(CFG["rubric_weights"]), 20)
        r = rubric.score([5] * 8, CFG)
        self.assertEqual(r["total"], 100)

    def test_total_is_weighted_sum(self):
        r = rubric.score([4, 5, 2, 4, 4, 3, 2, 3], CFG)
        expected = sum(s * w for s, w in zip([4, 5, 2, 4, 4, 3, 2, 3], CFG["rubric_weights"]))
        self.assertEqual(r["total"], expected)
        self.assertEqual(r["approved"], expected >= CFG["rubric_threshold"])

    def test_edge_bonus_adds_one_to_durability_and_ceiling_capped_at_five(self):
        base = rubric.score([3, 3, 3, 3, 3, 3, 3, 3], CFG)
        edge = rubric.score([3, 3, 3, 3, 3, 3, 3, 3], CFG, edge=True)
        w = CFG["rubric_weights"]
        self.assertEqual(edge["total"] - base["total"], w[5] + w[6])
        capped = rubric.score([5] * 8, CFG, edge=True)
        self.assertEqual(capped["total"], 100)

    def test_rejects_bad_input(self):
        with self.assertRaises(rubric.RubricError):
            rubric.score([4, 4, 4], CFG)
        with self.assertRaises(rubric.RubricError):
            rubric.score([0, 4, 4, 4, 4, 4, 4, 4], CFG)
        with self.assertRaises(rubric.RubricError):
            rubric.score([6, 4, 4, 4, 4, 4, 4, 4], CFG)

    def test_markdown_block_has_total_line_the_checker_reads(self):
        r = rubric.score([4, 5, 2, 4, 4, 3, 2, 3], CFG, edge=True, notes=["two primary sources"] + [""] * 7)
        md = rubric.render(r)
        self.assertIn("## Score", md)
        self.assertRegex(md, r"\*\*Total:\*\* \d+/100")
        self.assertIn("two primary sources", md)
        self.assertIn("edge", md.lower())

    def test_cli_exit_code_reflects_verdict(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = rubric.main(["score", "--scores", "5,5,5,5,5,5,5,5"])
        self.assertEqual(code, 0)
        self.assertIn("APPROVED", buf.getvalue())
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = rubric.main(["score", "--scores", "1,1,1,1,1,1,1,1"])
        self.assertEqual(code, 1)
        self.assertIn("REJECTED", buf.getvalue())


if __name__ == "__main__":
    unittest.main()
