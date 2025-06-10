from mcpbar.base import BaseAiProvider, BaseAiClient
from mcpbar.schema.ai_schema import AiProvider, AiModelSchema, AiRequestSchema, AiResponseSchema
from openai import OpenAI
from enum import Enum
from collections import OrderedDict

class OpenAIModelsEnum(Enum):
    gpt_4_1 = "gpt-4.1"
    #
    o1_pro = "o1-pro"
    o1_pro_2025_03_19 = "o1-pro-2025-03-19"
    computer_use_preview = "computer-use-preview"
    computer_use_preview_2025_03_11 = "computer-use-preview-2025-03-11"


class OpenAIClient(BaseAiClient):
    def __init__(self, base_url: str, api_key: str, max_tokens: int, **kwargs):
        self.base_url = base_url
        self.api_key = api_key
        self.max_tokens = max_tokens
        super().__init__()
        self.api = OpenAI(api_key=self.api_key, base_url=self.base_url, **kwargs)

    def get_ai_models_enum(self) -> type[Enum]:
        return OpenAIModelsEnum

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


class OpenAIProvider(BaseAiProvider):
    ai_provider = AiProvider.OpenAI.name

    def get_client(self) -> OpenAIClient:
        return OpenAIClient(
            base_url=self.ai_provider_params.base_url,
            api_key=self.ai_provider_params.api_key,
            max_tokens=self.ai_provider_schema.max_tokens,
        )