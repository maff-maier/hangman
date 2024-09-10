class GallowsManager:
    stages = [
        """
            -----
            |   |
                |
                |
                |
                |
            --------\n
        """,
        """
            -----
            |   |
            O   |
                |
                |
                |
            --------\n
        """,
        """
            -----
            |   |
            O   |
            |   |
                |
                |
            --------\n
        """,
        """
            -----
            |   |
            O   |
           /|   |
                |
                |
            --------\n
        """,
        """
            -----
            |   |
            O   |
           /|\\  |
                |
                |
            --------\n
        """,
        """
            -----
            |   |
            O   |
           /|\\  |
           /    |
                |
            --------\n
        """,
        """
            -----
            |   |
            O   |
           /|\\  |
           / \\ |
                |
            --------\n
        """,
    ]

    @classmethod
    def print_gallows_stage(cls, stage: int):
        print(cls.stages[stage])
