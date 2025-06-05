from dataclasses import dataclass
from typing import Optional, Union, Iterable
from openai.types.responses.response_input_param import ResponseInputParam
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam
from openai.types.chat.chat_completion_tool_param import ChatCompletionToolParam
from openai.types.chat.chat_completion import ChatCompletion
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk
from openai.types.responses.tool_param import ToolParam
from openai.types.responses.response import Response
from openai._streaming import Stream

OpenAIMessageInputParam = ResponseInputParam
OpenAIInputParam = Union[str, OpenAIMessageInputParam]

OpenAIToolParam = ToolParam
OpenAIToolsParam = Iterable[OpenAIToolParam]


@dataclass()
class OpenAIRequestSchema:
    input: OpenAIInputParam
    max_output_tokens: Optional[int]
    stream: bool
    tools: OpenAIToolsParam


OpenAIResponse = Response
OpenAIStream = Stream
OpenAIResponseSchema = Union[OpenAIResponse, OpenAIStream]

"""
Chat Completion API Schema Defines
"""

OpenAIChatCompletionMessageParam = ChatCompletionMessageParam
OpenAICompletionMessageParam = Iterable[OpenAIChatCompletionMessageParam]

OpenAIChatCompletionToolParam = ChatCompletionToolParam
OpenAICompletionToolsParam = Iterable[OpenAIChatCompletionToolParam]

@dataclass()
class OpenAICompletionsRequestSchema:
    messages: OpenAICompletionMessageParam
    max_tokens: Optional[int]
    tools: OpenAICompletionToolsParam
    stream: bool

OpenAIChatCompletion = ChatCompletion
OpenAiChatCompletionChunk = ChatCompletionChunk
OpenAIChatStream = Stream
OpenAIChatResponseSchema = Union[OpenAIChatCompletion, OpenAIChatStream]


