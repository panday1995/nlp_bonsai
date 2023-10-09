import pandas as pd
from config import ENGINE, EXIO_CLASSIF, RAW_CONCITO2EXIO
from models import Base, Correspondence, Schema


def clean_concito2exio() -> pd.DataFrame:
    df_concito2exio: pd.DataFrame = pd.read_excel(
        RAW_CONCITO2EXIO["path"], sheet_name=RAW_CONCITO2EXIO["sheet_name"]
    )
    df_exio_prod: pd.DataFrame = pd.read_excel(
        EXIO_CLASSIF["path"], sheet_name=EXIO_CLASSIF["sheet_name"]
    )
    df_concito2exio_clean = df_concito2exio.merge(
        df_exio_prod, left_on="exio4_id", right_on="Exio prod code", how="left"
    )[["concito500_name", "description"]].rename(
        columns={
            "concito500_name": Schema.DESCRIP_EXTERNAL.value,
            "description": Schema.DESCRIP_BONSAI.value,
        }
    )

    df_concito2exio_clean[Schema.SOURCE_EXTERNAL.value] = "Concito"
    return df_concito2exio_clean


if __name__ == "__main__":
    Base.metadata.create_all(ENGINE)
    df_concito2exio_clean = clean_concito2exio()
    df_concito2exio_clean.to_sql(
        Correspondence.__tablename__, ENGINE, if_exists="replace", index=False
    )
