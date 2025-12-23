from uuid import UUID

from faker import Faker


class Fake:
    """
    Класс для генерации случайных тестовых данных с использованием библиотеки Faker
    """

    def __init__(self, faker: Faker):
        """
        Инициализация

        Args:
            faker (Faker): экземляр класса Faker
        """
        self._faker = faker

    def text(self) -> str:
        """

        Returns:
            str: случайный текст
        """
        return self._faker.text()

    def uuid4(self) -> UUID:
        """
        Returns:
            UUID: случайный UUID версии 4
        """
        return self._faker.uuid4(cast_to=None)

    def uuid4_str(self) -> str:
        """
        Returns:
            UUID: случайный UUID версии 4 как строка
        """
        return self._faker.uuid4()

    def email(self, domain: str | None = None) -> str:
        """
        Args:
            domain (str | None): домен электронной почты, если указан.

        Returns:
            str: случайный email
        """
        return self._faker.email(domain=domain)

    def sentence(self) -> str:
        """
        Returns:
            str: случайное предложение
        """
        return self._faker.sentence()

    def password(self) -> str:
        """
        Returns:
            str: случайный пароль
        """
        return self._faker.password()

    def last_name(self) -> str:
        """
        Returns:
            str: случайная фамилия
        """
        return self._faker.last_name()

    def first_name(self) -> str:
        """
        Returns:
            str: случайное имя
        """
        return self._faker.first_name()

    def middle_name(self) -> str:
        """
        Returns:
            str: случайное отчество/среднее имя
        """
        return self._faker.first_name()

    def integer(self, min: int = 1, max: int = 100) -> int:
        """
        Args:
            min (int): минимальное значение (включительно)
            max (int): максимальное значение (включительно)

        Returns:
            int: случайно целое [min, max]
        """
        return self._faker.random_int(min, max)

    def estimated_time(self) -> str:
        """
        Returns:
            str: строка с предполагаемым количеством месяцев ('2 months')
        """
        return f"{self.integer(1, 12)} months"

    def max_score(self) -> int:
        """
        Returns:
            int: случайный максимальный балл [50,100]
        """
        return self.integer(50, 100)

    def min_score(self) -> int:
        """
        Returns:
            int: случайный минимальный балл [1,30]
        """
        return self.integer(1, 30)


fake = Fake(Faker())
