from mcpbar.log import logger
from mcpbar.client import McpBarClient
from mcpbar.schema.server_schema import ServerSchema
from mcpbar.schema.ai_schema import AiProviderSchema, AiProvider


async def execute_server(server_schema: ServerSchema, ai_provider_schema: AiProviderSchema, ai_model: str):
    logger.info("Run server")
    client = McpBarClient()

    await client.load_server("default", server_schema)

    client.load_ai_provider(
        ai_provider_schema=ai_provider_schema
    )
    ai_client = client.ai_client

    ai_client.select_model(ai_model)

    response = await client.server.client_session.list_tools()
    tools = response.tools
    for t in tools:
        logger.info(t.name, t.description)

    # if client.ai_provider.ai_provider == AiProvider.Anthropic.name:
    #     req = AnthropicAiRequestSchema(
    #         messages=[
    #             AnthropicAiMessagesSchema(
    #                 MessageParam(
    #                     role="user",
    #                     content="Please say a joke about letters."
    #                 )
    #             )
    #         ],
    #         max_tokens=None,
    #         tools=[],
    #         stream=True
    #     )
    # elif client.ai_provider.ai_provider == AiProvider.OpenAI.name:
    #     # req = OpenAIRequestSchema(
    #     #     input="Please say a joke about letters.",
    #     #     max_output_tokens=None,
    #     #     tools=[],
    #     #     stream=True
    #     # )
    #     req = OpenAICompletionsRequestSchema(
    #         messages=[
    #             {"role": "assistant", "content": "Talk like a school teacher."},
    #             {
    #                 "role": "assistant",
    #                 "content": "How can I write a article about sky?",
    #             },
    #         ],
    #         max_tokens=None,
    #         tools=[],
    #         stream=True
    #     )
    # elif client.ai_provider.ai_provider == AiProvider.DeepSeek.name:
    #     # req = deepseek.DeepSeekAIRequestSchema(
    #     #     input="Please say a joke about letters.",
    #     #     max_output_tokens=None,
    #     #     tools=[],
    #     #     stream=True
    #     # )
    #     req = deepseek.DeepSeekAICompletionsRequestSchema(
    #         messages=[
    #             {"role": "assistant", "content": "Talk like a school teacher."},
    #             {
    #                 "role": "assistant",
    #                 "content": "How can I write a article about sky?",
    #             },
    #         ],
    #         max_tokens=None,
    #         tools=[],
    #         stream=True
    #     )
    # elif client.ai_provider.ai_provider == AiProvider.AliBailianChat.name:
    #     req = ali_bailian_chat.AliBailianChatAICompletionsRequestSchema(
    #         messages=[
    #             {"role": "assistant", "content": "Talk like a school teacher."},
    #             {
    #                 "role": "assistant",
    #                 "content": "How can I write a article about sky?",
    #             },
    #         ],
    #         max_tokens=None,
    #         tools=[],
    #         stream=True
    #     )
    # else:
    #     logger.error(f"Unsupported ai provider: {client.ai_provider.ai_provider}")
    #     return
    #
    # resp = ai_client.send_messages(request=req)
    # if resp is AnthropicAiMessageSchema:
    #     logger.info(f'Resp: {resp}')
    # else:
    #     for chunk in resp:
    #         logger.info(f'Stream Chunk: {chunk}')