from faker.providers import BaseProvider

localized = False

class Provider(BaseProvider):
    """Implement custom Industries provider for Faker."""
    
    INDUSTRIES: [str] = [
            'Global Wireless Telecommunications Carriers',
            'Global Life & Health Insurance Carriers',
            'Global Pension Funds',
            'Global Commercial Real Estate',
            'Global Car & Automobile Sales',
            'Global Car & Automobile Manufacturing',
            'Global Direct General Insurance Carriers',
            'Global Commercial Banks'
        ]

    def industry(self) -> int:
        return self.random_element(self.INDUSTRIES)