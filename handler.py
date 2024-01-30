import dataclasses
import datetime
import json
import pprint
import uuid

from note import Note


class Handler:

    def __init__(self, filename: str):
        self.filename = filename
        self.notes = dict()

    def get(self):
        try:
            with open(self.filename, 'r') as f:
                self.notes = json.load(f)
        except:
            self.notes = dict()

    def save(self):
        with open(self.filename, 'w', encoding ='utf-8') as f:
            f.write(json.dumps(self.notes, indent=4, ensure_ascii=False))

    def add(self, note: Note):
        self.notes[str(uuid.uuid4())] = dataclasses.asdict(note)
        print("Заметка добавлена")
