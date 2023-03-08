from datetime import datetime


class Comment:
    def __init__(self, author_id: int, text: str):
        self.author_id = author_id
        self.text = text
        self.create_data = datetime.now()
        self.update_data = self.create_data
        self.like_count = 0

    def edit_comment(self, new_text: str):
        self.text = new_text
        self.update_data = datetime.now()

    def like(self):
        self.like_count += 1

    def dislike(self):
        self.like_count -= 1

    def __repr__(self):
        return "Comment<author={}, text={}, created={}, updated={}, likes={}>".format(self.author_id, self.text, self.create_data, self.update_data, self.like_count)

