import json
from queue import Queue

import person


class BeveragesTracker:

    READER_BARCODE = 1
    READER_NFC = 2

    def __init__(self, barcode_reader=True, nfc_reader=False):
        self.running = True
        self.entries = self.load_data()
        self.persons = self.load_persons()
        self.read_queue = Queue()
        self.readers = []
        if barcode_reader:
            from barcode_reader import BarcodeReader
            self.barcode_reader = BarcodeReader(self)
            self.readers.append(self.barcode_reader)
        if nfc_reader:
            from nfc_reader import NfcReader
            self.nfc_reader = NfcReader(self)
            self.readers.append(self.nfc_reader)
        for reader in self.readers:
            reader.start()

    def enqueue_read(self, data):
        (kind, id) = data
        if kind is self.READER_NFC:
            person = self.get_person_by_card_uid(id)
            if person is None:
                print('Person not registered yet!')
                return
            id = person.id
        self.read_queue.put(id)

    def start_loop(self):
        try:
            while self.running:
                id = self.read_queue.get()
                self.update_amount_for_id(str(id))
                print('Updated: ' + str(self.entries))
                self.save_data()
        except KeyboardInterrupt:
            for reader in self.readers:
                reader.shutdown()
        finally:
            self.save_data()

    def update_amount_for_id(self, id):
        if id not in self.entries:
            self.entries[id] = 0
        self.entries[id] += 1

    def get_person_by_card_uid(self, id):
        for p in self.persons:
            if p.has_nfc_id(id):
                return p
        return None

    def save_data(self):
        with open('entries.json', 'w') as save_file:
            save_file.write(json.dumps(self.entries))

    def load_data(self):
        try:
            with open('entries.json') as entries:
                return json.loads(entries.read())
        except:
            return json.loads('{}')

    def load_persons(self):
        try:
            with open('persons.json') as persons_file:
                js = json.loads(persons_file.readline())
                persons = person.from_json(js)
                return persons
        except:
            return json.loads('[]')

    def save_persons(self):
        try:
            with open('persons.json', 'w') as persons_file:
                persons_file.writelines(json.dumps(self.persons))
        except:
            print('Failed to write persons to file!')
