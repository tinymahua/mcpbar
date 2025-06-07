import time

from httpx import stream

from mcpbar.log import logger
from mcpbar.client import McpBarClient
from mcpbar.schema.server_schema import ServerSchema
from mcpbar.schema.ai_schema import AiProviderSchema, AiProvider
import typer
import base64
import json
from typing import Dict, AnyStr, Any

from mcpbar.schema.anthropic import AnthropicAiRequestSchema, AnthropicAiMessagesSchema, AnthropicAiStream, AnthropicAiMessageSchema
from mcpbar.schema.openai import OpenAICompletionsRequestSchema
from anthropic.types.message_param import MessageParam
from mcpbar.schema import deepseek
from mcpbar.schema.ali_bailian import chat as ali_bailian_chat

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

    client.load_server(
        server_schema=ServerSchema(**server_meta)
    )
    client.load_ai_provider(
        ai_provider_schema=AiProviderSchema(**ai_provider_meta)
    )
    ai_client = client.ai_client

    ai_client.select_model(ai_model)

    if client.ai_provider.ai_provider == AiProvider.Anthropic.name:
        req = AnthropicAiRequestSchema(
            messages=[
                AnthropicAiMessagesSchema(
                    MessageParam(
                        role="user",
                        content="Please say a joke about letters."
                    )
                )
            ],
            max_tokens=None,
            tools=[],
            stream=True
        )
    elif client.ai_provider.ai_provider == AiProvider.OpenAI.name:
        # req = OpenAIRequestSchema(
        #     input="Please say a joke about letters.",
        #     max_output_tokens=None,
        #     tools=[],
        #     stream=True
        # )
        req = OpenAICompletionsRequestSchema(
            messages=[
                {"role": "assistant", "content": "Talk like a school teacher."},
                {
                    "role": "assistant",
                    "content": "How can I write a article about sky?",
                },
            ],
            max_tokens=None,
            tools=[],
            stream=True
        )
    elif client.ai_provider.ai_provider == AiProvider.DeepSeek.name:
        # req = deepseek.DeepSeekAIRequestSchema(
        #     input="Please say a joke about letters.",
        #     max_output_tokens=None,
        #     tools=[],
        #     stream=True
        # )
        req = deepseek.DeepSeekAICompletionsRequestSchema(
            messages=[
                {"role": "assistant", "content": "Talk like a school teacher."},
                {
                    "role": "assistant",
                    "content": "How can I write a article about sky?",
                },
            ],
            max_tokens=None,
            tools=[],
            stream=True
        )
    elif client.ai_provider.ai_provider == AiProvider.AliBailianChat.name:
        req = ali_bailian_chat.AliBailianChatAICompletionsRequestSchema(
            messages=[
                {"role": "assistant", "content": "Talk like a school teacher."},
                {
                    "role": "assistant",
                    "content": "How can I write a article about sky?",
                },
            ],
            max_tokens=None,
            tools=[],
            stream=True
        )
    else:
        logger.error(f"Unsupported ai provider: {client.ai_provider.ai_provider}")
        return

    resp = ai_client.send_messages(request=req)
    if resp is AnthropicAiMessageSchema:
        logger.info(f'Resp: {resp}')
    else:
        for chunk in resp:
            logger.info(f'Stream Chunk: {chunk}')

def main():
    app()
