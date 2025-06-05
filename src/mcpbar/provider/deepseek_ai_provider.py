from . import openai_provider
from enum import Enum
from mcpbar.base import BaseAiClient, BaseAiProvider
from openai import OpenAI
from mcpbar.schema.ai_schema import AiRequestSchema, AiResponseSchema, AiProvider


class DeepSeekAIModelsEnum(Enum):
    deepseek_chat = "deepseek-chat"
    deepseek_reasoner = "deepseek-reasoner"

class DeepSeekAIClient(BaseAiClient):
    def __init__(self, base_url: str, api_key: str, max_tokens: int, **kwargs):
        self.base_url = base_url
        self.api_key = api_key
        self.max_tokens = max_tokens
        super().__init__()
        self.api = OpenAI(api_key=self.api_key, base_url=self.base_url, **kwargs)

    def get_ai_models_enum(self) -> type[Enum]:
        return DeepSeekAIModelsEnum

    def send_messages(self, request: AiRequestSchema) -> AiResponseSchema:
        self.check_used_model()
        # resp = self.api.responses.create(
        #     model=self.used_model.model_name,
        #     input=request.input,
        #     max_output_tokens=request.max_output_tokens,
        #     tools=request.tools,
        #     stream=request.stream,
        # )
        resp = self.api.chat.completions.create(
            model=self.used_model.model_name,
            messages=request.messages,
            max_tokens=request.max_tokens,
            stream=request.stream,
        )
        return resp

class DeepSeekAIProvider(BaseAiProvider):
    ai_provider = AiProvider.DeepSeek.name

    def get_client(self) -> DeepSeekAIClient:
        return DeepSeekAIClient(
            base_url=self.ai_provider_schema.ai_provider_params.base_url,
            api_key=self.ai_provider_schema.ai_provider_params.api_key,
            max_tokens=self.ai_provider_schema.max_tokens,
        )