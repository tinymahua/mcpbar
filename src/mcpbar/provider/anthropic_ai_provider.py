from collections import OrderedDict
from mcpbar.base import BaseAiProvider, BaseAiClient
from mcpbar.schema.ai_schema import AiProvider, AiModelSchema
from mcpbar.schema.anthropic import (
    AnthropicAiResponseSchema,
    AnthropicAiRequestSchema,
)
from enum import Enum
from anthropic import Anthropic


class AnthropicAiModelsEnum(Enum):
    claude_3_7_sonnet_latest = "claude-3-7-sonnet-latest"
    claude_3_7_sonnet_20250219 =  "claude-3-7-sonnet-20250219"
    claude_3_5_haiku_latest =  "claude-3-5-haiku-latest"
    claude_3_5_haiku_20241022 =  "claude-3-5-haiku-20241022"
    claude_3_5_sonnet_latest =  "claude-3-5-sonnet-latest"
    claude_3_5_sonnet_20241022 =  "claude-3-5-sonnet-20241022"
    claude_3_5_sonnet_20240620 =  "claude-3-5-sonnet-20240620"
    claude_3_opus_latest =  "claude-3-opus-latest"
    claude_3_opus_20240229 =  "claude-3-opus-20240229"
    claude_3_sonnet_20240229 =  "claude-3-sonnet-20240229"
    claude_3_haiku_20240307 =  "claude-3-haiku-20240307"
    claude_2_1 = "claude-2.1"
    claude_2_0 =  "claude-2.0"



class AnthropicAiClient(BaseAiClient):
    def __init__(self, base_url: str, api_key: str, max_tokens: int, **kwargs):
        self.base_url = base_url
        self.api_key = api_key
        self.max_tokens = max_tokens
        super().__init__()
        self.api = Anthropic(api_key=self.api_key, base_url=self.base_url, **kwargs)

    def get_ai_models_enum(self) -> type[Enum]:
        return AnthropicAiModelsEnum

    def send_messages(self, request: AnthropicAiRequestSchema) -> AnthropicAiResponseSchema:
        self.check_used_model()

        resp = self.api.messages.create(
            model=self.used_model.model_name,
            max_tokens=request.max_tokens if request.max_tokens is not None else self.max_tokens,
            messages=request.messages,
            tools=request.tools,
            stream=request.stream,
        )
        if request.stream:
            return resp.response.iter_lines()
            # for line in resp.response.iter_lines():
            #     line = line.lstrip("data: ").strip()
            #     if line:
            #         data = json.loads(line)
            #         if data['type'] == 'content_block_start':
            #             yield AnthropicAiRawContentBlockStartEvent.construct(**data)
            #         elif data['type'] == 'content_block_delta':
            #             yield AnthropicAiRawContentBlockDeltaEvent.construct(**data)
            #         elif data['type'] == 'content_block_stop':
            #             yield AnthropicAiRawContentBlockStopEvent.construct(**data)
            #         elif data['type'] == 'message_start':
            #             yield AnthropicAiRawMessageStartEvent.construct(**data)
            #         elif data['type'] == 'message_delta':
            #             yield AnthropicAiRawMessageDeltaEvent.construct(**data)
            #         else:
            #             yield AnthropicAiRawMessageStopEvent.construct(**data)
        else:
            return resp


class AnthropicAiProvider(BaseAiProvider):
    ai_provider = AiProvider.Anthropic.name

    def get_client(self) -> AnthropicAiClient:
        return AnthropicAiClient(
            self.ai_provider_schema.ai_provider_params.base_url,
            self.ai_provider_schema.ai_provider_params.api_key,
            max_tokens=self.ai_provider_schema.max_tokens,
        )