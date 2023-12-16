from collections import UserDict

class Note:
    def __init__(self, name, note):
        self.name = name
        self.note = note
        self.teg = []

    def add_teg(self, teg):
        self.teg.append(teg)
    
    def __str__(self):
        return f"Note name: {self.name}, tegs: {'; '.join(p for p in self.teg)}, note: {self.note}"
    
class Notebook(UserDict):
    def add_note(self, note):
        if isinstance(note, Note):
            self.data[note.name] = note

notebook = Notebook()
cleans = Note('прибрати кімнату', 'віник,  вода і інше')
cleans.add_teg('необовязкове')
cleans.add_teg('щоденне')

notebook.add_note(cleans)

print('-----', cleans)

cleeps = Note('лягти спати', 'поставити будильник на 22 год і одразу лягти спати')
cleeps.add_teg('обовязкове')
cleeps.add_teg('щоденне')

notebook.add_note(cleeps)

print('_____', cleeps)


for x, y in notebook.data.items():
    print(x, '_-_', y)