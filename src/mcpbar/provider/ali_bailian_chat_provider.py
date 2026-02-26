from enum import Enum
from mcpbar.base import BaseAiClient, BaseAiProvider
from openai import OpenAI
from mcpbar.schema.ai_schema import AiRequestSchema, AiResponseSchema, AiProvider


class AliBailianChatAIModelsEnum(Enum):
    qwen_vl_plus = "qwen-vl-plus"
    qwen_plus = "qwen-plus"
    qwen3_coder_plus = 'qwen3-coder-plus'
    deepseek_r1 = "deepseek-r1"
    deepseek_r1_distill_qwen_1_5b = "deepseek-r1-distill-qwen-1.5b"
    qwen3_5_flash = "qwen3.5-flash"

class AliBailianChatAIClient(BaseAiClient):
    def __init__(self, base_url: str, api_key: str, max_tokens: int, **kwargs):
        self.base_url = base_url
        self.api_key = api_key
        self.max_tokens = max_tokens
        super().__init__()
        self.api = OpenAI(api_key=self.api_key, base_url=self.base_url, **kwargs)

    def get_ai_models_enum(self) -> type[Enum]:
        return AliBailianChatAIModelsEnum

    def send_messages(self, request: AiRequestSchema) -> AiResponseSchema:
        self.check_used_model()
        resp = self.api.chat.completions.create(
            model=self.used_model.model_name,
            messages=request.messages,
            max_tokens=request.max_tokens,
            stream=request.stream,
        )
        return resp

class AliBailianChatAIProvider(BaseAiProvider):
    ai_provider = AiProvider.AliBailianChat.name

    def get_client(self) -> AliBailianChatAIClient:
        return AliBailianChatAIClient(
            base_url=self.ai_provider_params.base_url,
            api_key=self.ai_provider_params.api_key,
            max_tokens=self.ai_provider_schema.max_tokens,
        )