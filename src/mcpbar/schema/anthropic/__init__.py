from anthropic.types.tool_union_param import ToolUnionParam
from anthropic.types.message_param import MessageParam
from anthropic.types.message import Message
from anthropic.types.raw_message_stream_event import RawMessageStreamEvent
from typing import Union, List, NewType, Optional, Iterator
from dataclasses import dataclass

AnthropicAiMessagesSchema = NewType('AnthropicAiMessagesSchema', MessageParam)
AnthropicAiToolUnionParam = NewType('AnthropicAiToolUnionParam', ToolUnionParam)


@dataclass()
class AnthropicAiRequestSchema:
    messages: List[AnthropicAiMessagesSchema]
    max_tokens: Optional[int]
    tools: List[AnthropicAiToolUnionParam]
    stream: bool



AnthropicAiMessageSchema =  Message
AnthropicAiRawMessageStreamEvent = RawMessageStreamEvent
AnthropicAiStream = Iterator[str]
AnthropicAiResponseSchema = Union[AnthropicAiMessageSchema, AnthropicAiStream]