from mcpbar.schema.server_schema import ServerSchema
from mcpbar.schema.ai_schema import AiProviderSchema
import abc
from enum import Enum
from collections import OrderedDict
from mcpbar.schema.ai_schema import AiModelSchema, AiRequestSchema, AiResponseSchema
from typing import Optional

"""
Base Runnable class and Base server class
"""

class BaseRunnable:
    def run(self):
        pass

class BaseServer:
    server_type: str
    def __init__(self, server_schema: ServerSchema):
        self.server_schema = server_schema
        if self.server_schema.server_type != self.server_type:
            raise ValueError(f"Server type {self.server_schema.server_type} not match {self.server_type}")

    @abc.abstractmethod
    def get_runnable(self) -> BaseRunnable:
        raise NotImplemented


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

    def __init__(self, ai_provider_schema: AiProviderSchema):
        self.ai_provider_schema = ai_provider_schema
        if self.ai_provider_schema.ai_provider != self.ai_provider:
            raise ValueError(f"Ai provider {self.ai_provider_schema.ai_provider} not match {self.ai_provider}")

    @abc.abstractmethod
    def get_client(self) -> BaseAiClient:
        raise NotImplemented
