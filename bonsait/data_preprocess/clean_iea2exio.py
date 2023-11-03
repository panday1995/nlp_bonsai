import pandas as pd

from bonsait.configs import ENGINE, EXIO_CLASSIF, RAW_IEA2EXIO
from bonsait.models import Base, Correspondence, Schema


def clean_iea2exio() -> pd.DataFrame:
    df_iea2exio: pd.DataFrame = pd.read_excel(
        RAW_IEA2EXIO["path"], sheet_name=RAW_IEA2EXIO["sheet_name"]
    )
    df_exio_prod = pd.read_excel(
        EXIO_CLASSIF["path"], sheet_name=EXIO_CLASSIF["sheet_name"]
    )
    df_iea2exio_clean = (
        df_iea2exio.dropna()
        .merge(
            df_exio_prod,
            left_on="Exiobase product code",
            right_on="Exio prod code",
            how="left",
        )[["PRODUCT.1", "description"]]
        .rename(
            columns={
                "PRODUCT.1": Schema.DESCRIP_EXTERNAL.value,
                "description": Schema.DESCRIP_BONSAI.value,
            }
        )
    )
    df_iea2exio_clean[Schema.SOURCE_EXTERNAL.value] = "International Energy Agency"
    return df_iea2exio_clean.dropna()


if __name__ == "__main__":
    Base.metadata.create_all(ENGINE)
    df_iea2exio_clean = clean_iea2exio()
    df_iea2exio_clean.to_sql(
        Correspondence.__tablename__, ENGINE, if_exists="replace", index=False
    )
