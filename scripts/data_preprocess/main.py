import pandas as pd
from clean_concito2exio import clean_concito2exio
from clean_fao2exio import clean_fao2exio
from clean_iea2exio import clean_iea2exio
from config import ENGINE
from models import Base, Correspondence


def main():
    Base.metadata.create_all(ENGINE)
    df_fao2exio_clean = clean_fao2exio()
    df_concito2exio_clean = clean_concito2exio()
    df_iea2exio_clean = clean_iea2exio()
    df_corr = pd.concat([df_fao2exio_clean, df_concito2exio_clean, df_iea2exio_clean])
    breakpoint()
    df_corr = df_corr.applymap(lambda x: x.lower())
    breakpoint()
    df_corr.to_sql(
        Correspondence.__tablename__, ENGINE, if_exists="replace", index=False
    )


if __name__ == "__main__":
    main()
