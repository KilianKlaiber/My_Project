class Me:
    def __init__(self, help) -> None:
        self.help = help
        
class You(Me):
    def __init__(self, help) -> None:
        super().__init__(help)
        