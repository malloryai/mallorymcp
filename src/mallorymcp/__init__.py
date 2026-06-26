"""Mallory MCP Server (deprecated).

Replaced by the hosted Mallory Remote MCP service:
https://docs.mallory.ai/use/agent/mcp
"""

try:
    from mallorymcp._version import __version__
except ModuleNotFoundError:
    __version__ = "0.0.0"
