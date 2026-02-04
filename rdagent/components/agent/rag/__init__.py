from pydantic_ai.mcp import MCPServerStreamableHTTP

from rdagent.components.agent.base import PAIAgent
from rdagent.components.agent.rag.conf import SETTINGS
from rdagent.utils.agent.tpl import T


class Agent(PAIAgent):
    """
    A specific agent for RAG
    """

    def __init__(self, system_prompt: str | None = None):
        toolsets = [MCPServerStreamableHTTP(SETTINGS.url, timeout=SETTINGS.timeout)]
        if system_prompt is None:
            system_prompt = "你是一个检索增强生成（RAG，Retrieval-Augmented Generation）agent。请使用检索到的文档准确、简洁地回答用户的问题。"
        super().__init__(system_prompt=system_prompt, toolsets=toolsets)
