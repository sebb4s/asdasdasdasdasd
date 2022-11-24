class FoodShift:
    def __init__(self, title:str, image:str, description:str) -> None:
        self.title = title
        self.image = image
        self.description = description

    def serialize(self) -> dict:
        return {
            "title" : self.title,
            "image" : self.image,
            "description" : self.description
}
