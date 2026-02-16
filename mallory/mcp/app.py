from mallory.mcp.server.server import initialize_server

# Initialize the server at module level so tools can register
mcp = initialize_server()


def main() -> None:
    """Entry point for the mallory-mcp-server CLI."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
