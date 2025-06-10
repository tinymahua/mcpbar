from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Union, NewType

from mcpbar.schema import anthropic as anthropic_schema
from mcpbar.schema import openai as openai_schema
from mcpbar.schema import deepseek as deepseek_schema
from mcpbar.schema.ali_bailian import chat as ali_bailian_chat_schema

ToolUnionParamSchema = NewType('ToolUnionParamSchema', anthropic_schema.AnthropicAiToolUnionParam)



AiRequestSchema = Union[
    anthropic_schema.AnthropicAiRequestSchema,
    openai_schema.OpenAIRequestSchema,
    openai_schema.OpenAICompletionsRequestSchema,
    deepseek_schema.DeepSeekAIRequestSchema,
    deepseek_schema.DeepSeekAICompletionsRequestSchema,
    ali_bailian_chat_schema.AliBailianChatAIRequestSchema,
    ali_bailian_chat_schema.AliBailianChatAICompletionsRequestSchema,
]
AiResponseSchema = Union[
    anthropic_schema.AnthropicAiResponseSchema,
    openai_schema.OpenAIResponseSchema,
    openai_schema.OpenAIChatResponseSchema,
    deepseek_schema.DeepSeekAIResponseSchema,
    deepseek_schema.DeepSeekAIChatResponseSchema,
    ali_bailian_chat_schema.AliBailianChatAIResponseSchema,
    ali_bailian_chat_schema.AliBailianChatAIChatResponseSchema,
]


@dataclass()
class AiModelSchema:
    model_id: str
    model_name: str
    model_desc: str


class AiProvider(Enum):
    Anthropic = 'Anthropic'
    OpenAI = 'OpenAI'
    DeepSeek = 'DeepSeek'
    AliBailianChat = 'AliBailianChat'


@dataclass()
class AnthropicAiProviderParams:
    api_key: str
    base_url: str


@dataclass()
class OpenAIAiProviderParams:
    api_key: str
    base_url: str


@dataclass()
class DeepSeekAiProviderParams:
    api_key: str
    base_url: str

@dataclass()
class AliBailianChatProviderParams:
    api_key: str
    base_url: str

AiProviderParams = Union[
    AnthropicAiProviderParams,
    OpenAIAiProviderParams,
    DeepSeekAiProviderParams,
    AliBailianChatProviderParams,
]


@dataclass()
class AiProviderSchema:
    max_tokens: int
    ai_provider: str
    ai_provider_params_dict: Dict
    # ai_provider_params: AiProviderParams = field(init=False)


    def __post_init__(self):
        if not getattr(AiProvider, self.ai_provider, None):
            raise ValueError(f"Invalid ai provider: {self.ai_provider}")
