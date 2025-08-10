from mcpbar.schema.server_schema import (
    ServerSchema, ServerParams
)
from mcpbar.schema.ai_schema import AiProviderSchema, AiProviderParams
import abc
from enum import Enum
from collections import OrderedDict
from mcpbar.schema.ai_schema import AiModelSchema, AiRequestSchema, AiResponseSchema
from typing import Optional, Type, List, Callable, Dict, Any, Tuple, Union
from mcp import ClientSession, StdioServerParameters
from contextlib import AsyncExitStack


"""
Base Runnable class and Base server class
"""

class BaseRunnable:
    def  __init__(self):
        pass

    def run(self):
        pass

McpServerParameters = Union[StdioServerParameters, Dict[str, Any]]


class BaseServer:
    server_type: str
    server_params: Optional[ServerParams] = None
    client_session: Optional[ClientSession] = None


    def __init__(self, server_schema: ServerSchema, server_params_schema:  Type[ServerParams]):
        self.server_params = server_params_schema(**server_schema.server_params_dict)
        self.exit_stack = AsyncExitStack()

    @abc.abstractmethod
    def make_mcp_server_parameters(self) -> StdioServerParameters:
        raise NotImplemented

    @abc.abstractmethod
    def get_runnable(self) -> BaseRunnable:
        raise NotImplemented

    async def close_session(self):
        await self.exit_stack.aclose()

class BaseAiClient:
    def __init__(self):
        self.models: OrderedDict[str, AiModelSchema] = self.get_available_models()
        self.used_model: Optional[AiModelSchema] = None

    def get_available_models(self) -> OrderedDict[str, AiModelSchema]:
        models = OrderedDict()
        models_enum = self.get_ai_models_enum()
        for model_name in models_enum._member_names_:
            m: models_enum = getattr(models_enum, model_name)
            models[m.name] = AiModelSchema(model_id=m.name, model_name=m.value, model_desc="")
        return models

    @abc.abstractmethod
    def get_ai_models_enum(self) -> type[Enum]:
        raise NotImplemented

    def select_model(self, model_id: str):
        self.used_model = self.models[model_id]

    @abc.abstractmethod
    def send_messages(self, request: AiRequestSchema) -> AiResponseSchema:
        raise NotImplemented

    def check_used_model(self):
        if self.used_model is None:
            raise ValueError("Please select a model")

class BaseAiProvider:
    ai_provider: str
    ai_provider_params: AiProviderParams

    def __init__(self, ai_provider_schema: AiProviderSchema,  ai_provider_params_schema: Type[AiProviderParams]):
        self.ai_provider_schema = ai_provider_schema
        if self.ai_provider_schema.ai_provider != self.ai_provider:
            raise ValueError(f"Ai provider {self.ai_provider_schema.ai_provider} not match {self.ai_provider}")
        self.ai_provider_params = ai_provider_params_schema(**self.ai_provider_schema.ai_provider_params_dict)

    @abc.abstractmethod
    def get_client(self) -> BaseAiClient:
        raise NotImplemented
