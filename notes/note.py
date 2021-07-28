from dataclasses import dataclass

from .exceptions import NoteNotFound

@dataclass()
class Note:
    _id: int
    title: str
    content: str

class Collection:
    def __init__(self):
        """Creates an empty note collection, takes no arguments"""
        self.notes = {}
        self.next_id = 0

    def add(self, title: str, content: str) -> Note:
        """Adds a note to the collection (the C in CRUD)"""
        n = Note(self.next_id, title, content)
        m = {self.next_id: n}
        self.notes.update(m)
        self.next_id += 1
        return n

    def get(self, id: int) -> Note:
        """Gets a note from the collection (the R in CRUD)"""
        try:
            return self.notes[id]
        except KeyError:
            raise NoteNotFound(f"Could not find note with id: {id}")
    
    def update(self, id: int, title: str=None, content: str=None) -> Note:
        """Updates a note from the collection (the U in CRUD)"""
        try:
            n = self.notes[id]
            if title != None:
                n.title = title
            if content != None:
                n.content = content
            return n
        except KeyError:
            raise NoteNotFound(f"Could not find note with id: {id}")

    def delete(self, id: int):
        """Deletes a note from the collection (the D in CRUD)"""
        try:
            del self.notes[id]
        except KeyError:
            raise NoteNotFound(f"Could not find note with id: {id}")            

    def get_by_title(self, title: str) -> Note:
        """Gets note/notes from title."""
        rt = []
        for n in self.notes:
            if n["title"] == title:
                rt.append(n)
        return rt[0] if len(rt) < 1 else rt
