# mcpbar

> A mcp client call mcpbar.

## Quick Start

* Ali Bailian Chat Example

```python
from mcpbar.log import logger
from mcpbar.provider.ali_bailian_chat_provider import AliBailianChatAIProvider, AliBailianChatAIModelsEnum
from mcpbar.schema.ai_schema import ali_bailian_chat_schema
from mcpbar.schema.ai_schema import AiProviderSchema, AiProvider, AliBailianChatProviderParams
from mcpbar.utils.states import try_get_chunk_finish_reason
from dataclasses import asdict


def ali_bailian_chat_test():
    ai_provider = AliBailianChatAIProvider(
        ai_provider_schema=AiProviderSchema(
            max_tokens = 1024,
            ai_provider = AiProvider.AliBailianChat.name,
            ai_provider_params_dict = asdict(AliBailianChatProviderParams(api_key="YOUR-ALI-BAILIAN-API-KEY", base_url="ALI-BAILIAN-CHAT-BASE-URL")),
        ),
        ai_provider_params_schema=AliBailianChatProviderParams,
    )
    ai_client = ai_provider.get_client()
    ai_client.select_model(AliBailianChatAIModelsEnum.qwen_vl_plus.name)
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
    resp = ai_client.send_messages(request=req)
    if req.stream:
        for chunk in resp:
            logger.info(f'Stream Chunk: {chunk}')
            finish_reason = try_get_chunk_finish_reason(ai_provider=AiProvider.AliBailianChat, resp_chunk=chunk)
            if finish_reason is not None and finish_reason == "stop":
                break
    else:
        logger.info("StatusCode: {}".format(resp.status_code))
        logger.info("Content: {}".format(resp.content))
```