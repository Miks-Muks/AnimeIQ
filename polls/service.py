from abc import ABC, abstractmethod, abstractclassmethod, abstractstaticmethod
from typing import List


class BasePercentageCalculator(ABC):

    @abstractmethod
    def prepare_answer(self, answer: List[str]) -> list:
        ...

    def get_percentage_answer(self, data: list) -> int:
        ...


class BaseSchedule(ABC):

    @abstractmethod
    def draw_schedule(self):
        ...
