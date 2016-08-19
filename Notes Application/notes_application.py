class NotesApplication(object):
    """class for a note taking application """
    def __init__(self, author):
        #initialising the author and the notes list
        self.author = author
        self.notes = []

    def create(self, note_content):
        #method to add the note_content to the notes list
        note = {}
        note[self.author] = note_content
        self.notes.append(note)
        return note_content

    def list(self):
        #method to list out the notes in the notes list and their authors
        for note in self.notes:
            note_id = self.notes.index(note)
            note_content = note[self.author]
            note_author = note.keys()
            print('Note ID: '+str(note_id)+'\n'+str(note_content)+'\n\nBy Author '+str(note_author)+'\n\n')

    def get(self, note_id):
        #method to return contents of a note in notes list based on note id
        note = self.notes[note_id]
        return "The content of Note ID: "+str(note_id)+"\n"+str(note[self.author])+"\n\n"

    def search(self, search_text):
        #method to return notes that have the search text within them
        print("Showing results for search: "+str(search_text))
        for note in self.notes:
            for note_content in note.values():
                if search_text in note_content:
                    print("\n Note ID: "+str(self.notes.index(note))+"\n"+str(note_content)+"\n\n\nBy Author "+str(self.author)+"\n\n")
            return note_content

    def delete(self, note_id):
        #method to delete note at index note_id in the notes list
        for note in self.notes:
            if note.index() == note_id:
                self.notes.pop(note)

    def edit(self, note_id, new_content):
        #method to replace content at index note_id with new content
        for note in self.notes:
            if note.index() == note_id:
                for note_content in note.values():
                    note_content = new_content
        return "Note ID: "+str(note_id)+" edited\n\n"

note1 = NotesApplication('Isaac')

note1.create('This is the start of something beautiful')
note1.create('Done this is already')

print(note1.get(0))
print(note1.list())
print(note1.search('is'))

