from mcpbar.log import logger
from mcpbar.client import McpBarClient
from mcpbar.schema import ServerSchema
import typer
import base64
import json
from typing import Dict, AnyStr, Any


app = typer.Typer(name="mcpbar")

@app.command()
def run_test():
    logger.info("Run test OK")

@app.command()
def run_server(server_meta_b64: str = typer.Option()):
    logger.info("Run server")
    client = McpBarClient()
    try:
        server_meta_str = base64.b64decode(server_meta_b64).decode()
    except Exception as e:
        logger.error(f"Error decoding server meta with base64 decode: {e}")
        return

    try:
        server_meta: Dict[AnyStr, Any] = json.loads(server_meta_str)
    except Exception as e:
        logger.error(f"Error decoding server meta with json load: {e}")
        return

    client.load_server(
        server_schema=ServerSchema(**server_meta)
    )



def main():
    app()
