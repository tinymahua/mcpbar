from .. import openai
from typing import Iterable, Union, Optional

DeepSeekAIMessageInputParam = openai.ResponseInputParam
DeepSeekAIInputParam = Union[str, DeepSeekAIMessageInputParam]

DeepSeekAIToolParam = openai.ToolParam
DeepSeekAIToolsParam = Iterable[DeepSeekAIToolParam]

DeepSeekAIRequestSchema = openai.OpenAIRequestSchema


DeepSeekAIResponse = openai.Response
DeepSeekAIStream = openai.Stream
DeepSeekAIResponseSchema = Union[DeepSeekAIResponse, DeepSeekAIStream]


DeepSeekAIChatCompletionMessageParam = openai.ChatCompletionMessageParam
DeepSeekAICompletionMessageParam = Iterable[DeepSeekAIChatCompletionMessageParam]

DeepSeekAIChatCompletionToolParam = openai.ChatCompletionToolParam
DeepSeekAICompletionToolsParam = Iterable[DeepSeekAIChatCompletionToolParam]

DeepSeekAICompletionsRequestSchema = openai.OpenAICompletionsRequestSchema

DeepSeekAIChatCompletion = openai.ChatCompletion
DeepSeekAiChatCompletionChunk = openai.ChatCompletionChunk
DeepSeekAIChatStream = openai.Stream
DeepSeekAIChatResponseSchema = Union[DeepSeekAIChatCompletion, DeepSeekAIChatStream]