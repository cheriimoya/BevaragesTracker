from threading import Thread


class Reader(Thread):
    def __init__(self, parent, reader_id):
        super().__init__()
        self.running = True
        self.parent = parent
        self.reader_id = reader_id

    def run(self):
        while self.running:
            try:
                id = self.get_id()
            except:
                continue
            self.parent.enqueue_read((self.reader_id, id))

    def get_id(self):
        # Implement me
        raise NotImplementedError()

    def shutdown(self):
        self.running = False
