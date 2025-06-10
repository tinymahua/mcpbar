from mcpbar.schema.server_schema import ServerSchema, ServerType
from mcpbar.schema import ai_schema
from mcpbar.server.local_runnable_py_server import LocalRunnablePyServer
from mcpbar.server.local_runnable_js_server import LocalRunnableJsServer
from mcpbar.schema.server_schema import LocalRunnablePyParams, LocalRunnableJsParams
from typing import Dict
from mcpbar.base import BaseServer, BaseAiProvider
from mcpbar.provider import deepseek_ai_provider, ali_bailian_chat_provider, openai_provider, anthropic_ai_provider

class ServersLoader:
    servers: Dict[str, BaseServer] = {}

    def __init__(self):
        pass

    def load_server(self, tag: str, server_schema: ServerSchema):
        if tag in self.servers:
            raise ValueError(f"Server with tag {tag} already exists")

        if server_schema.server_type == ServerType.LOCAL_RUNNABLE_PY.name:
            server = LocalRunnablePyServer(server_schema, LocalRunnablePyParams)
        elif server_schema.server_type == ServerType.LOCAL_RUNNABLE_JS.name:
            server = LocalRunnableJsServer(server_schema, LocalRunnableJsParams)
        else:
            raise ValueError(f"Invalid server type: {server_schema.server_type}")

        self.servers[tag] = server
        return server


class AIProviderLoader:
    ai_providers: Dict[str, BaseAiProvider] = {}

    def load_ai_provider(self, ai_provider_schema: ai_schema.AiProviderSchema):
        _ai_provider_name = ai_provider_schema.ai_provider

        if _ai_provider_name in self.ai_providers:
            raise ValueError(f"AI provider with name {_ai_provider_name} already exists")

        if _ai_provider_name == ai_schema.AiProvider.Anthropic.name:
            ai_provider_obj = anthropic_ai_provider.AnthropicAiProvider(ai_provider_schema, ai_schema.AnthropicAiProviderParams)
        elif _ai_provider_name == ai_schema.AiProvider.OpenAI.name:
            ai_provider_obj = openai_provider.OpenAIProvider(ai_provider_schema, ai_schema.OpenAIAiProviderParams)
        elif _ai_provider_name == ai_schema.AiProvider.DeepSeek.name:
            ai_provider_obj = deepseek_ai_provider.DeepSeekAIProvider(ai_provider_schema, ai_schema.DeepSeekAiProviderParams)
        elif _ai_provider_name  == ai_schema.AiProvider.AliBailianChat.name:
            ai_provider_obj = ali_bailian_chat_provider.AliBailianChatAIProvider(ai_provider_schema, ai_schema.AliBailianChatProviderParams)
        else:
            raise ValueError(f"Invalid ai provider: {ai_provider_schema.ai_provider}")

        self.ai_providers[_ai_provider_name] = ai_provider_obj
        return ai_provider_obj
