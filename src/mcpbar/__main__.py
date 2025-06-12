import asyncio
from mcpbar.log import logger
from mcpbar.schema.server_schema import ServerSchema
from mcpbar.schema.ai_schema import AiProviderSchema
import typer
import base64
import json
from typing import Dict, AnyStr, Any
from mcpbar.funcs import execute_server

app = typer.Typer(name="mcpbar")

@app.command()
def run_test():
    logger.info("Run test OK")

@app.command()
def run_server(
        server_meta_b64: str = typer.Option(default=...),
        ai_provider_meta_b64: str = typer.Option(default=...),
        ai_model: str = typer.Option(default=...),
):
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

    try:
        ai_provider_meta_str = base64.b64decode(ai_provider_meta_b64).decode()
    except Exception as e:
        logger.error(f"Error decoding ai provider meta with base64 decode: {e}")
        return

    try :
        ai_provider_meta: Dict[AnyStr, Any] = json.loads(ai_provider_meta_str)
    except Exception as e:
        logger.error(f"Error decoding ai provider meta with json load: {e}")
        return

    asyncio.run(execute_server(ServerSchema(**server_meta), AiProviderSchema(**ai_provider_meta), ai_model))


def main():
    app()
