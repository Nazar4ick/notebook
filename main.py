import datetime


last_id = 0


class Note:
    """
    Represent a note in the notebook. Match against
    a string in searches and sore tags for each note
    """
    def __init__(self, memo, tags=''):
        """
        initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id
        :param memo: str
        :param tags: str
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filt):
        """
        Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and
        tags.
        :param filt: str
        :return: bool
        """
        return filt in self.memo or filt in self.tags


class Notebook:
    """
    Represent a collection of notes that can be tagged,
    modified, and searched
    """
    def __init__(self):
        """
        Initialize a notebook with an empty list
        """
        self.notes = []

    def new_note(self, memo, tags=''):
        """
        Create a new note and add it to the list
        :param memo: str
        :param tags: str
        :return: None
        """
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        """
        Locate the note with the given id.
        :param note_id: int
        :return: object
        """
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def modify_memo(self, note_id, memo):
        """
        Find the note with the given id and change its
        memo to the given value
        :param note_id: int
        :param memo: str
        :return: None
        """
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        """
        Find the note with the given id and change its
        tags to the given value
        :param note_id: int
        :param tags: str
        :return: None
        """
        self._find_note(note_id).tags = tags

    def search(self, filt):
        """
        Find all notes that match the given filter
        string
        :param filt: str
        :return: list
        """
        return [note for note in self.notes if note.match(filt)]
