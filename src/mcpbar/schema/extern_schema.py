from dataclasses import dataclass
from typing import List, AnyStr, Dict

@dataclass()
class ClineSseServerSchema:
    url: str

@dataclass()
class ClineStdioServerSchema:
    command: str
    args: List[AnyStr]
    env: Dict[str, str]


