from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Response:
    ok: int = 0
    data: list() = []
