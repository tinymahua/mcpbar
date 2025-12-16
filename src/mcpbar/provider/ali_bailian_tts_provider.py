from enum import Enum

import dashscope

from mcpbar.base import BaseAiClient, BaseAiProvider
from openai import OpenAI
from mcpbar.schema.ai_schema import AiRequestSchema, AiResponseSchema, AiProvider


class AliBailianTtsAIModelsEnum(Enum):
    qwen3_tts_flash = "qwen3-tts-flash"

class AliBailianTtsAIClient(BaseAiClient):
    def __init__(self, base_url: str, api_key: str, max_tokens: int, **kwargs):
        self.base_url = base_url
        self.api_key = api_key
        self.max_tokens = max_tokens
        super().__init__()
        # self.api = OpenAI(api_key=self.api_key, base_url=self.base_url, **kwargs)
        self.api = dashscope.MultiModalConversation

    def get_ai_models_enum(self) -> type[Enum]:
        return AliBailianTtsAIModelsEnum

    def send_messages(self, request: AiRequestSchema) -> AiResponseSchema:
        self.check_used_model()
        # resp = self.api.chat.completions.create(
        #     model=self.used_model.model_name,
        #     messages=request.messages,
        #     max_tokens=request.max_tokens,
        #     stream=request.stream,
        # )
        resp = self.api.call(
            model=self.used_model.model_name,
            api_key=self.api_key,
            text=request.text,
            voice=request.voice,
            language_type=request.language_type,
            stream=request.stream,
        )

        return resp

class AliBailianTtsAIProvider(BaseAiProvider):
    ai_provider = AiProvider.AliBailianTTS.name

    def get_client(self) -> AliBailianTtsAIClient:
        return AliBailianTtsAIClient(
            base_url=self.ai_provider_params.base_url,
            api_key=self.ai_provider_params.api_key,
            max_tokens=self.ai_provider_schema.max_tokens,
        )