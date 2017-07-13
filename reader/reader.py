import os
from reader.compressed import gzipped

extension_map = {
    '.gz': gzipped.opener
}


class Reader:
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        opener = extension_map.get(extension, open)
        # self.filename = filename
        self.f = opener(filename, 'rt')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()
