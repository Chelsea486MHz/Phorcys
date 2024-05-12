import subprocess
import tempfile
from typing import Optional

from phorcys.decoders.base import Layer
from phorcys.plugins.decoder import DecoderPlugin


class Protobuf(DecoderPlugin):
    def __call__(self, parent: Layer, **metadata) -> Optional[Layer]:
        data = parent.raw_data
        self.layer = parent
        try:
            self._decode(data)
        except Exception as e:
            raise ValueError(f"[Phorcys] Failed to parse input. Not protobuf ({e})")
        self.layer.name = 'protobuf'
        self.layer.is_structured = True
        self.layer.human_readable = True
        return self.layer

    def _decode(self, data, **metadata):
        with tempfile.NamedTemporaryFile(delete=True) as tf:
            tf.write(data)
            tf.seek(0)
            content = subprocess.check_output("cat %s | protoc --decode_raw" % tf.name, shell=True,
                                              universal_newlines=True)
            self.layer.raw_data = content
            self.layer.lines = content.splitlines()
            self._decode_data()

    def _decode_data(self):
        prev = []
        for ll in self.layer.lines:
            line = ll.strip()
            if '{' in line:
                name = line[:line.find('{')]
                prev.append(name.strip())
            elif ':' in line:
                name = line[:line.find(':')]
                prefix = ';'.join(prev)
                value = line[line.find(':') + 1:]
                child = Layer(True)
                child.parent = self.layer
                child.raw_data = '%s;%s=%s' % (prefix.strip(), name.strip(), value.strip())
                child.lines = [child.raw_data]
                self.layer.add_extracted_layer(child)
            elif '}' in line:
                prev.pop()
