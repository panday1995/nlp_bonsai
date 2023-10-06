from pathlib import Path

from sqlalchemy import create_engine

####################
# raw data definition
####################

DIR_HOME = Path("../../")

RAW_FAO2EXIO = {
    "path": DIR_HOME / "data/raw/Exio4_vs_FCL.xlsx",
    "sheet_name": "Exio4_vs_FAO",
}


####################
# sql connection definition
####################
DB = f"sqlite:///{Path(DIR_HOME / 'data/clean/correspondence.db')}"
ENGINE = create_engine(DB, echo=True)
