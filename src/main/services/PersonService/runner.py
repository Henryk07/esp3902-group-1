from services.PersonService.model import PersonModel

class PersonRunner:
    def __init__(self) -> None:
        self.model = PersonModel()

    def run(self, frame: str) -> None:
        return self.model.infer(frame)