from mcpbar.schema.ai_schema import AiProvider
from typing import Optional, AnyStr, Any


def try_get_chunk_finish_reason(ai_provider: AiProvider, resp_chunk: Any) -> Optional[AnyStr]:
    if ai_provider == AiProvider.Anthropic:
        raise NotImplemented
    elif ai_provider == AiProvider.OpenAI:
        raise NotImplemented
    elif ai_provider == AiProvider.DeepSeek:
        raise NotImplemented
    elif ai_provider == AiProvider.AliBailianChat:
        return getattr(resp_chunk, "finish_reason", None)
    elif ai_provider == AiProvider.AliBailianTTS:
        return getattr(resp_chunk.output, "finish_reason", None)
    else:
        raise ValueError("Unknown ai_provider")