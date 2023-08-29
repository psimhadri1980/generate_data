from faker.providers import BaseProvider

localized = False

class Provider(BaseProvider):
    """Implement custom Products provider for Faker."""
    
    PRODUCTS: [str] = [
            'Lombard',
            'Structured Lombard',
            'Mortgage',
            'Corporate Loan'
        ]

    def product(self) -> int:
        return self.random_element(self.PRODUCTS)