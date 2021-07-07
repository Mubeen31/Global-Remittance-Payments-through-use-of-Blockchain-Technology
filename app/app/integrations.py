from typing import List
from django.db.models import QuerySet
from polaris.models import Asset, Transaction
from polaris.integrations import RailsIntegration

class MyRailsIntegrations(RailsIntegration):
    def poll_pending_deposits(self, pending_deposits: QuerySet) -> List[Transaction]:
        return list(pending_deposits)

def toml():
    asset = Asset.objects.first()
    return {
        "DOCUMENTATION": {
        "ORG_NAME":"Stellar Development Foundation",
        "ORG_URL": "https://stellar.org"
    },
    "PRINCIPALS": [
        {
            "name": "Stellar"
        }
    ],
        "CURRENCIES": [
            {
                "code": asset.code,
                "issuer": asset.issuer,
                "status": "test",
                "display_decimals": 2,
                "name": "Stellar Reference Token",
                "desc": "A fake asset."
            }
        ]
   }