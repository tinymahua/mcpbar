from mcpbar.base import BaseServer, BaseAiProvider, BaseAiClient
from mcpbar.server.local_runnable_js_server import LocalRunnableJsServer
from mcpbar.server.local_runnable_py_server import LocalRunnablePyServer
from mcpbar.schema.server_schema import ServerSchema, ServerType
from mcpbar.schema.ai_schema import (
    AiProviderSchema, AiProvider)
from typing import Optional
from mcpbar.provider import anthropic_ai_provider, openai_provider, deepseek_ai_provider
from mcpbar.provider import ali_bailian_chat_provider


class McpBarClient:
    def __init__(self):
        self.server: Optional[BaseServer] = None
        self.ai_provider: Optional[BaseAiProvider] = None
        self.ai_client: Optional[BaseAiClient] = None

    def load_server(self, server_schema: ServerSchema):
        match server_schema.server_type:
            case ServerType.LOCAL_RUNNABLE_JS.name:
                self.server = LocalRunnableJsServer(server_schema)
            case ServerType.LOCAL_RUNNABLE_PY.name:
                self.server = LocalRunnablePyServer(server_schema)
            case _:
                raise ValueError(f"Unknown server type: {server_schema.server_type}")

        print(f"Loaded server: {self.server}")

    def load_ai_provider(self, ai_provider_schema: AiProviderSchema):
        match ai_provider_schema.ai_provider:
            case AiProvider.Anthropic.name:
                self.ai_provider = anthropic_ai_provider.AnthropicAiProvider(ai_provider_schema)
            case AiProvider.OpenAI.name:
                self.ai_provider = openai_provider.OpenAIProvider(ai_provider_schema)
            case AiProvider.DeepSeek.name:
                self.ai_provider = deepseek_ai_provider.DeepSeekAIProvider(ai_provider_schema)
            case AiProvider.AliBailianChat.name:
                self.ai_provider = ali_bailian_chat_provider.AliBailianChatAIProvider(ai_provider_schema)
            case _:
                raise ValueError(f"Unknown ai provider: {ai_provider_schema.ai_provider}")

        self.ai_client = self.ai_provider.get_client()
