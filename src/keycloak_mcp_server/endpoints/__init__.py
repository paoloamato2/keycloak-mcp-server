from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Param:
    name: str
    description: str
    required: bool = True
    param_type: str = "string"
    default: Any = None
    enum: list[str] | None = None


@dataclass
class EndpointDef:
    name: str
    description: str
    method: str
    path: str
    path_params: list[Param] = field(default_factory=list)
    query_params: list[Param] = field(default_factory=list)
    body_param: Param | None = None

    def input_schema(self) -> dict[str, Any]:
        properties: dict[str, Any] = {}
        required: list[str] = []

        for p in self.path_params:
            prop: dict[str, Any] = {"type": p.param_type, "description": p.description}
            if p.enum:
                prop["enum"] = p.enum
            properties[p.name] = prop
            if p.required:
                required.append(p.name)

        for p in self.query_params:
            prop = {"type": p.param_type, "description": p.description}
            if p.default is not None:
                prop["default"] = p.default
            if p.enum:
                prop["enum"] = p.enum
            properties[p.name] = prop
            if p.required:
                required.append(p.name)

        if self.body_param:
            properties[self.body_param.name] = {
                "type": "object",
                "description": self.body_param.description,
            }
            if self.body_param.required:
                required.append(self.body_param.name)

        schema: dict[str, Any] = {"type": "object", "properties": properties}
        if required:
            schema["required"] = required
        return schema

    def extract_args(
        self, arguments: dict[str, Any]
    ) -> tuple[dict[str, str], dict[str, Any], Any]:
        path_vals = {
            p.name: str(arguments[p.name])
            for p in self.path_params
            if p.name in arguments
        }
        query_vals = {
            p.name: arguments[p.name] for p in self.query_params if p.name in arguments
        }
        body_val = arguments.get(self.body_param.name) if self.body_param else None
        return path_vals, query_vals, body_val


def _realm_param(description: str = "Realm name") -> Param:
    return Param("realm", description)


# Common params used across many endpoints
REALM = _realm_param()
