from faker.providers import BaseProvider
from typing import Any

localized = False

class Provider(BaseProvider):
    """Implement custom collater provider for Faker."""

    COLLATERALS: list[dict[str:Any]] = [
            {'name': 'Security', 'id': 100 },
            {'name': 'Cash', 'id': 200 },
            {'name': 'Cash Like', 'id': 300 },
            {'name': 'Bank Gaurantee', 'id': 500 },
            {'name': 'Fixed Deposit', 'id': 400 }
        ]

    def collateral(self) -> dict[str:Any]:
        return self.random_element(self.COLLATERALS)
    
