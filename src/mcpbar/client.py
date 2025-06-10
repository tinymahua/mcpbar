from mcpbar.base import BaseServer, BaseAiProvider, BaseAiClient
from mcpbar.schema.server_schema import ServerSchema, ServerType
from mcpbar.schema.ai_schema import (
    AiProviderSchema)
from typing import Optional
from mcpbar.loader import ServersLoader, AIProviderLoader


class McpBarClient:
    def __init__(self):
        self.server: Optional[BaseServer] = None
        self.ai_provider: Optional[BaseAiProvider] = None
        self.ai_client: Optional[BaseAiClient] = None
        self.server_loader = ServersLoader()
        self.ai_provider_loader = AIProviderLoader()

    def load_server(self, tag: str, server_schema: ServerSchema):
        self.server = self.server_loader.load_server(tag, server_schema)

    def load_ai_provider(self, ai_provider_schema: AiProviderSchema):
        ai_provider_obj = self.ai_provider_loader.load_ai_provider(ai_provider_schema)
        self.ai_provider = ai_provider_obj
        self.ai_client = ai_provider_obj.get_client()