from typing import Optional

from phorcys.decoders.base import Layer, split_string
from phorcys.plugins.decoder import DecoderPlugin


class Text(DecoderPlugin):
    def __call__(self, parent: Layer, **metadata) -> Optional[Layer]:
        # if len(parent.name) > 0:
        #     raise ValueError("[Phorcys] Failed to parse input. Not text")

        data = parent.raw_data
        try:
            self.layer = parent
            content = data
            if type(data) is bytes:
                content = data.decode('utf-8')
            if type(content) is not str:
                raise ValueError("[Phorcys] Failed to parse input. Not text")
            self.layer.lines = split_string(content, 64)
            self.layer.raw_data = content
            self.layer.human_readable = True
            self.layer.name = "text"
            self.layer.add_header({'length': len(content)})
            return self.layer
        except Exception as e:
            raise ValueError(f"[Phorcys] Failed to parse input. Not text ({e})")
