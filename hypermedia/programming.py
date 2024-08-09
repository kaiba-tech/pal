from typing import Unpack

from hypermedia.models import Element, VoidElement
from hypermedia.models.types import AnyChildren, PrimitiveChildren
from hypermedia.types.attributes import (
    EmbedAttrs,
    GlobalAttrs,
    ObjectAttrs,
    ScriptAttrs,
)


class Script(Element[PrimitiveChildren, ScriptAttrs]):
    """Defines a client-side script."""

    tag: str = "script"

    def __init__(
        self, *children: PrimitiveChildren, **attributes: Unpack[ScriptAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class NoScript(Element[AnyChildren, GlobalAttrs]):
    """Defines alternate content when client-side scripts aren't supported."""

    tag: str = "noscript"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Embed(VoidElement[EmbedAttrs]):
    """Defines a container for an external (non-HTML) application."""

    tag: str = "embed"

    def __init__(self, **attributes: Unpack[EmbedAttrs]) -> None:
        super().__init__(**attributes)


class Object(Element[AnyChildren, ObjectAttrs]):
    """Defines an embedded object."""

    tag: str = "object"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[ObjectAttrs]
    ) -> None:
        super().__init__(*children, **attributes)
