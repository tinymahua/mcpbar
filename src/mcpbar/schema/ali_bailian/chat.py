from .. import openai
from typing import Iterable, Union, Optional




AliBailianChatAIMessageInputParam = openai.ResponseInputParam
AliBailianChatAIInputParam = Union[str, AliBailianChatAIMessageInputParam]

AliBailianChatAIToolParam = openai.ToolParam
AliBailianChatAIToolsParam = Iterable[AliBailianChatAIToolParam]

AliBailianChatAIRequestSchema = openai.OpenAIRequestSchema


AliBailianChatAIResponse = openai.Response
AliBailianChatAIStream = openai.Stream
AliBailianChatAIResponseSchema = Union[AliBailianChatAIResponse, AliBailianChatAIStream]


AliBailianChatAIChatCompletionMessageParam = openai.ChatCompletionMessageParam
AliBailianChatAICompletionMessageParam = Iterable[AliBailianChatAIChatCompletionMessageParam]

AliBailianChatAIChatCompletionToolParam = openai.ChatCompletionToolParam
AliBailianChatAICompletionToolsParam = Iterable[AliBailianChatAIChatCompletionToolParam]

AliBailianChatAICompletionsRequestSchema = openai.OpenAICompletionsRequestSchema

AliBailianChatAIChatCompletion = openai.ChatCompletion
AliBailianChatAiChatCompletionChunk = openai.ChatCompletionChunk
AliBailianChatAIChatStream = openai.Stream
AliBailianChatAIChatResponseSchema = Union[AliBailianChatAIChatCompletion, AliBailianChatAIChatStream]

