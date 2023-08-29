from faker.providers import BaseProvider

localized = False

class Provider(BaseProvider):
    """Implement custom amount provider for Faker."""

    def amount(self) -> int:
        return self.random_number()
    
    def amountMillions(self) -> int:
        return self.random_number(9, False)

