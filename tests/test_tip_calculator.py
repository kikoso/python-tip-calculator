# Runs each program with fixed input and checks the output.
# Run from the repository root with:  python3 -m pytest
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(script, user_input):
    result = subprocess.run(
        [sys.executable, str(ROOT / script)],
        input=user_input,
        capture_output=True,
        text=True,
    )
    return result.stdout


def test_basic():
    out = run("tip_calculator.py", "84\n10\n3\n")
    assert "Total: 92.40 EUR, each pays 30.80 EUR" in out


def test_level1_shows_tip():
    out = run("extensions/level1_show_tip.py", "84\n10\n3\n")
    assert "Tip: 8.40 EUR" in out
    assert "Total: 92.40 EUR, each pays 30.80 EUR" in out


def test_level2_accepts_percent_sign():
    out = run("extensions/level2_percent_sign.py", "84\n10%\n3\n")
    assert "Total: 92.40 EUR, each pays 30.80 EUR" in out


def test_level3_rounds_up():
    out = run("extensions/level3_round_up.py", "84\n10\n3\n")
    assert "each pays 31 EUR" in out


def test_level3_exact_amount_not_rounded():
    out = run("extensions/level3_round_up.py", "100\n20\n4\n")
    assert "each pays 30 EUR" in out
