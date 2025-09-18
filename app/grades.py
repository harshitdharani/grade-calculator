import json

class Grades:
    """
    Stores all individual class grades.
    """
    
    def __init__(self, quiz_1=None, quiz_2=None, midterm=None, project=None, final=None) -> None:
        self.quiz_1 = quiz_1
        self.quiz_2 = quiz_2
        self.midterm = midterm
        self.project = project
        self.final = final
        
    def set_all(self, quiz_1=None, quiz_2=None, midterm=None, project=None, final=None):
        self.quiz_1 = quiz_1
        self.quiz_2 = quiz_2
        self.midterm = midterm
        self.project = project
        self.final = final

    @classmethod
    def from_json(cls, filepath: str):
        """
        Loads grades from a JSON file and returns a Grades object.
        Only keys that match class attributes will be set.
        """
        with open(filepath, 'r') as f:
            data = json.load(f)

        return cls(
            quiz_1=data.get("quiz_1"),
            quiz_2=data.get("quiz_2"),
            midterm=data.get("midterm"),
            project=data.get("project"),
            final=data.get("final")
        )
        
    def __str__(self) -> str:
        grades = []
        if self.quiz_1 is not None:
            grades.append(f'Quiz 1: {self.quiz_1}')
        if self.quiz_2 is not None:
            grades.append(f'Quiz 2: {self.quiz_2}')
        if self.midterm is not None:
            grades.append(f'Midterm Exam: {self.midterm}')
        if self.project is not None:
            grades.append(f'Project: {self.project}')
        if self.final is not None:
            grades.append(f'Final Exam: {self.final}')
            
        if len(grades) <= 0:
            return 'No grades submitted yet.'
        else:
            return 'GRADES --- ' + ', '.join(grades)
