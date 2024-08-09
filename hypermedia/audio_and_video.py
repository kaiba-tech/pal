from typing import Unpack

from hypermedia.models import Element, VoidElement
from hypermedia.models.types import AnyChildren
from hypermedia.types.attributes import (
    AudioAttrs,
    SourceAttrs,
    TrackAttrs,
    VideoAttrs,
)


class Audio(Element[AnyChildren, AudioAttrs]):
    """Defines sound content."""

    tag: str = "audio"

    def __init__(self, **attributes: Unpack[AudioAttrs]) -> None:
        super().__init__(**attributes)


class Source(VoidElement[SourceAttrs]):
    """
    Defines multiple media resources for media elements.

    `video`, `audio` and `picture`.
    """

    tag: str = "source"

    def __init__(self, **attributes: Unpack[SourceAttrs]) -> None:
        super().__init__(**attributes)


class Track(VoidElement[TrackAttrs]):
    """Defines text tracks for media elements (`video` and `audio`)."""

    tag: str = "track"

    def __init__(self, **attributes: Unpack[TrackAttrs]) -> None:
        super().__init__(**attributes)


class Video(Element[AnyChildren, VideoAttrs]):
    """Defines a video or movie."""

    tag: str = "video"

    def __init__(self, **attributes: Unpack[VideoAttrs]) -> None:
        super().__init__(**attributes)
