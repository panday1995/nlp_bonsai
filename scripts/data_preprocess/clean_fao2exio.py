import pandas as pd
from config import ENGINE, RAW_FAO2EXIO
from models import Base, Correspondence, Schema

Base.metadata.create_all(ENGINE)
df_exio2fao: pd.DataFrame = pd.read_excel(
    RAW_FAO2EXIO["path"], sheet_name=RAW_FAO2EXIO["sheet_name"]
)
df_exio2fao_clean: pd.DataFrame = (
    df_exio2fao.drop_duplicates(subset=["Item"], keep="first").reset_index(drop=True)
)[["description", "Item"]].rename(
    columns={
        "description": Schema.DESCRIP_BONSAI.value,
        "Item": Schema.DESCRIP_EXTERNAL.value,
    }
)

df_exio2fao_clean[Schema.SOURCE_EXTERNAL.value] = "Faostat"


df_exio2fao_clean.to_sql(
    Correspondence.__tablename__, ENGINE, if_exists="replace", index=False
)
