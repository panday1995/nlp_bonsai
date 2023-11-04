from pathlib import Path

from sqlalchemy import create_engine

####################
# raw correspondence definition
####################

DIR_HOME = Path(__file__).parent

RAW_FAO2EXIO = {
    "path": DIR_HOME / "data/raw/Exio4_vs_FCL.xlsx",
    "sheet_name": "Exio4_vs_FAO",
}

RAW_CONCITO2EXIO = {
    "path": DIR_HOME / "data/raw/concito500_exio4.xlsx",
    "sheet_name": "concito500_exio4_list",
}

RAW_IEA2EXIO = {
    "path": DIR_HOME / "data/raw/IEAvsExiobase_products.xlsx",
    "sheet_name": "prod_corres",
}
EXIO_CLASSIF = {
    "path": DIR_HOME / "data/raw/Master_classif_exio4.xlsx",
    "sheet_name": "unit_products",
}

####################
# sql connection definition
####################
DB = f"sqlite:///{Path(DIR_HOME / 'data/clean/correspondence.db')}"
ENGINE = create_engine(DB, echo=True)
