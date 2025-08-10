from mcpbar.log import logger
from mcpbar.client import McpBarClient
from mcpbar.schema.server_schema import ServerSchema
from mcpbar.schema.ai_schema import AiProviderSchema, AiProvider
from mcpbar.schema.ai_schema import anthropic_schema
from mcpbar.schema.ai_schema import openai_schema
from mcpbar.schema.ai_schema import ali_bailian_chat_schema
from mcpbar.schema.ai_schema import deepseek_schema


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




    if client.ai_provider.ai_provider == AiProvider.Anthropic.name:
        req = anthropic_schema.AnthropicAiRequestSchema(
            messages=[
                anthropic_schema.AnthropicAiMessagesSchema(
                    anthropic_schema.MessageParam(
                        role="user",
                        content="Please say a joke about letters."
                    )
                )
            ],
            max_tokens=None,
            tools=[],
            stream=True
        )
    elif client.ai_provider.ai_provider == AiProvider.OpenAI.name:
        # req = OpenAIRequestSchema(
        #     input="Please say a joke about letters.",
        #     max_output_tokens=None,
        #     tools=[],
        #     stream=True
        # )
        req = openai_schema.OpenAICompletionsRequestSchema(
            messages=[
                {"role": "assistant", "content": "Talk like a school teacher."},
                {
                    "role": "assistant",
                    "content": "How can I write a article about sky?",
                },
            ],
            max_tokens=None,
            tools=[],
            stream=True
        )
    elif client.ai_provider.ai_provider == AiProvider.DeepSeek.name:
        # req = deepseek.DeepSeekAIRequestSchema(
        #     input="Please say a joke about letters.",
        #     max_output_tokens=None,
        #     tools=[],
        #     stream=True
        # )
        req = deepseek_schema.DeepSeekAICompletionsRequestSchema(
            messages=[
                {"role": "assistant", "content": "Talk like a school teacher."},
                {
                    "role": "assistant",
                    "content": "How can I write a article about sky?",
                },
            ],
            max_tokens=None,
            tools=[],
            stream=True
        )
    elif client.ai_provider.ai_provider == AiProvider.AliBailianChat.name:
        req = ali_bailian_chat_schema.AliBailianChatAICompletionsRequestSchema(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": "编写一个Rust枚举OrderStatus，包含常用订单状态项，并附加可打印宏，不要输出非代码内容。",
                },
            ],
            max_tokens=None,
            tools=[],
            stream=True
        )
    else:
        logger.error(f"Unsupported ai provider: {client.ai_provider.ai_provider}")
        return

    resp = ai_client.send_messages(request=req)
    if resp is anthropic_schema.AnthropicAiMessageSchema:
        logger.info(f'Resp: {resp}')
    else:
        for chunk in resp:
            logger.info(f'Stream Chunk: {chunk}')
            finish_reason = getattr(chunk, "finish_reason", None)
            print(f'FINISH_REASON: {finish_reason}')
            if finish_reason is not None and finish_reason == "stop":
                print('DONE')
                break

    await client.server.close_session()