"""Basic smoke tests for the deprecated mallorymcp package."""

import subprocess
import sys


def test_import():
    """Package can be imported."""
    import mallorymcp

    assert mallorymcp.__version__


def test_entry_point():
    """Entry point function exists."""
    from mallorymcp.app import main

    assert callable(main)


def test_deprecation_notice_points_to_docs():
    """The deprecation message points users to the Remote MCP docs."""
    from mallorymcp.app import DOCS_URL, MESSAGE

    assert DOCS_URL == "https://docs.mallory.ai/use/agent/mcp"
    assert DOCS_URL in MESSAGE
    assert "deprecated" in MESSAGE


def test_cli_prints_deprecation_and_exits_nonzero():
    """Running the CLI prints the notice and exits non-zero."""
    result = subprocess.run(
        [sys.executable, "-m", "mallorymcp.app"],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "https://docs.mallory.ai/use/agent/mcp" in result.stderr
