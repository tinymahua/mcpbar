from enum import EnumMeta
from typing import Any, Union
from typing import AsyncGenerator, Generator, List, Union
import dataclasses

from dashscope.api_entities.dashscope_response import \
    MultiModalConversationResponse

class AlibailianTtsVoiceEnum(EnumMeta):
    Cherry = 'Cherry'

class AlibailianTtsLanguageTypeEnum:
    Chinese = 'Chinese'

@dataclasses.dataclass()
class AliBailianTtsRequestSchema:
    text: str
    voice: str
    language_type: str
    stream: bool


# class AliBailianTtsAudio:
#     data: str
#     url: str
#     id: str
#     expires_at: int
#
#
# class AliBailianTtsOutput:
#     text: str
#     finish_reason: str
#     choices: Any
#     audio: AliBailianTtsAudio
#
#
# class AliBailianTtsInputTokenDetails:
#     text_tokens: int
#
# class AliBailianTtsOutputTokenDetails:
#     text_tokens: int
#     audio_tokens: int
#
# class AliBailianTtsUsage:
#     input_tokens_details: AliBailianTtsInputTokenDetails
#     total_tokens: int
#     output_tokens: int
#     input_tokens: int
#     output_tokens_details: AliBailianTtsOutputTokenDetails
#     characters: int
#
# class AliBailianTtsResponseSchema:
#     status_code: int
#     request_id: str
#     code: str
#     message: str
#     output: AliBailianTtsOutput
#     usage: AliBailianTtsUsage


AliBailianTtsResponseSchema =  Union[MultiModalConversationResponse, Generator[
            MultiModalConversationResponse, None, None]]