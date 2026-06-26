"""Deprecation stub for the mallorymcp CLI.

The local mallorymcp stdio server is deprecated in favor of the hosted
Mallory Remote MCP service. See https://docs.mallory.ai/use/agent/mcp
"""

import sys

DOCS_URL = "https://docs.mallory.ai/use/agent/mcp"

MESSAGE = f"""\
mallorymcp is deprecated and no longer maintained.

The local MCP server has been replaced by Mallory's hosted Remote MCP
service, which requires no local install and is always up to date.

Migrate your AI client to the Remote MCP service:

    {DOCS_URL}

You can then remove mallorymcp from your MCP client config and uninstall
this package:

    pip uninstall mallorymcp
"""


def main() -> None:
    """Entry point: print the deprecation notice and exit non-zero."""
    print(MESSAGE, file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
