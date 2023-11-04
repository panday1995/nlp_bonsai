import pandas as pd

from scripts.configs import ENGINE, RAW_FAO2EXIO
from scripts.models import Base, Correspondence, Schema


def clean_fao2exio():
    df_exio2fao: pd.DataFrame = pd.read_excel(
        RAW_FAO2EXIO["path"], sheet_name=RAW_FAO2EXIO["sheet_name"]
    )
    df_exio2fao_clean: pd.DataFrame = (
        df_exio2fao.drop_duplicates(subset=["Item"], keep="first").reset_index(
            drop=True
        )
    )[["description", "Item"]].rename(
        columns={
            "description": Schema.DESCRIP_BONSAI.value,
            "Item": Schema.DESCRIP_EXTERNAL.value,
        }
    )

    df_exio2fao_clean[
        Schema.SOURCE_EXTERNAL.value
    ] = "Food and Agriculture Organization Corporate Statistical Database"
    return df_exio2fao_clean


if __name__ == "__main__":
    Base.metadata.create_all(ENGINE)
    df_exio2fao_clean = clean_fao2exio()
    df_exio2fao_clean.to_sql(
        Correspondence.__tablename__, ENGINE, if_exists="replace", index=False
    )
