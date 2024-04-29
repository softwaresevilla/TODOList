class Todo:

    def __init__(self, id, userId, title, completed):
        self.id = id
        self.userId = userId
        self.title = title
        self.completed = completed
    
    @classmethod
    def from_json(self, json_data):
        return self(
            id=json_data.get('id'),
            userId=json_data.get('userId'),
            title=json_data.get('title'),
            completed=json_data.get('completed')
        )
    
    def to_dict(self) -> dict:
        """
        Convert the Todo object to a dictionary.

        Returns:
            dict: A dictionary representation of the Todo object.
        """
        return {
            'id': self.id,
            'userId': self.userId,
            'title': self.title,
            'completed': self.completed
        }