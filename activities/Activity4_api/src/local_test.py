from locale import currency
from platform import platform
from services.services_nomics import NomicsServices

nomic_v1 = NomicsServices(api_key="781f6cd2fe5b5e2ba5c09eee8f88a387f24885fa")

print(nomic_v1.get_currency_ticker(ids="BTC", interval="30d", convert="EUR"))