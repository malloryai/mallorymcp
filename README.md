# Mallory MCP Server (deprecated)

[![PyPI](https://img.shields.io/pypi/v/mallorymcp.svg)](https://pypi.org/project/mallorymcp/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

> **⚠️ This package is deprecated and no longer maintained.**
>
> The local `mallorymcp` stdio server has been replaced by Mallory's hosted
> **Remote MCP** service. The remote service is fully managed, always
> up to date, and requires no local install.
>
> **➡️ Migrate to the Remote MCP service: https://docs.mallory.ai/use/agent/mcp**

## What changed

`mallorymcp` was a local MCP server you ran via `uvx`/`pip` that proxied the
Mallory API to your AI client over stdio. It is no longer published with new
features and will receive no further updates.

All functionality now lives in the **Mallory Remote MCP service**, a hosted
endpoint you connect your AI client to directly. It exposes the same threat
intelligence capabilities (vulnerabilities, threat actors, malware, exploits,
organizations, attack patterns, breaches, products, advisories, stories,
mentions, search, and sources) without any local package to install or keep
up to date.

## How to migrate

Follow the setup guide for your AI client (Cursor, Claude Desktop, Claude Code,
and others) here:

**https://docs.mallory.ai/use/agent/mcp**

Once you've connected the Remote MCP service, you can remove the local server
from your MCP client config and uninstall this package:

```bash
pip uninstall mallorymcp
```

## License

Apache 2.0.
