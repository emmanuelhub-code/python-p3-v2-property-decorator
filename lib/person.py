APPROVED_JOBS = [
    "Admin", "Customer Service", "Human Resources", "ITC",
    "Production", "Legal", "Finance", "Sales", "General Management",
    "Research & Development", "Marketing", "Purchasing"
]

class Person:
    def __init__(self, name="Person", job="Admin"):
        self.name = name
        self.job = job

    @property
    def name(self):
        """The name property"""
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # convert to title case
        else:
            raise ValueError("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        """The job property"""
        return self._job

    @job.setter
    def job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            raise ValueError("Job must be in list of approved jobs.")
