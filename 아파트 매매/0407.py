import PublicDataReader as pdr
print(pdr.__version__)
# from PublicDataReader import TransactionPrice

service_key = "ybAi2TTNPIIxR5M%2B2OGc7OJpn94cuXnpfafc7j%2FMy1fYi74ia%2FbOHUDCgq04nJLFB%2Fa5RJ8tCBDHUXfVSOfHTA%3D%3D"
api = pdr.TransactionPrice(service_key)


# 단일 월 조회
df = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11650",
    year_month="202212",
)

# 기간 내 조회
# df = api.get_data(
#     property_type="아파트",
#     trade_type="매매",
#     sigungu_code="11650",
#     start_year_month="202201",
#     end_year_month="202212",
# )

df.tail()

print(df.head())
