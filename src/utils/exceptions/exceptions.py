from builtins import Exception


class TTrackerException(Exception):
    notify_user = "Error"

    def __init__(self, *args, **kwargs):
        self.message: str = f"{self.notify_user}."
        super(TTrackerException, self).__init__(self.message)

    def __str__(self) -> str:
        return self.message

    def __repr__(self) -> str:
        return f"Exception: {self.__class__}. Message: {self.message}"


class AlchemyError(TTrackerException):
    notify_user = "Unknown error, please, try again later"


class StatusNotFoundError(TTrackerException):
    notify_user = "Status not found"


class TaskNotFoundError(TTrackerException):
    notify_user = "Task not found"


class UserNotFoundError(TTrackerException):
    notify_user = "User not found"


class UserEmailNotUnique(TTrackerException):
    notify_user = "User with current email is already exist"
