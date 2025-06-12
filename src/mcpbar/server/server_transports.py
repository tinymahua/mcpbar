from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.client.sse import sse_client
from contextlib import AsyncExitStack
from typing import Callable, Dict, Any, Tuple


class StdioTransportServerMixin:
    async def make_transport(
            self,
            exit_stack: AsyncExitStack,
            mcp_server_parameters_maker: Callable[[], StdioServerParameters]
    ) -> Tuple[Any, Any]:
        print(f'estack: {id(exit_stack)}')
        mcp_server_parameters = mcp_server_parameters_maker()
        stdio_transport = await exit_stack.enter_async_context(stdio_client(mcp_server_parameters))
        return stdio_transport


class SseTransportServerMixin:
    async def make_transport(
            self,
            exit_stack: AsyncExitStack,
            mcp_server_parameters_maker: Callable[[], Dict[str, Any]]
    ) -> Tuple[Any, Any]:
        mcp_server_parameters = mcp_server_parameters_maker()
        sse_transport = await exit_stack.enter_async_context(sse_client(**mcp_server_parameters))
        return sse_transport