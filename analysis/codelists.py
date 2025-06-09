####################################################################
# This script fetches all of the codelists identified in 
# codelists.txt from OpenCodelists.
#
# Author: Colm Andrews 
#   Bennett Institute for Applied Data Science
#   University of Oxford, 2025
#####################################################################

# --- IMPORT STATEMENTS ---

## Import code building blocks from cohort extractor package
from ehrql import codelist_from_csv

 
# --- CODELISTS ---

# statin intolerance
intolerence = codelist_from_csv("codelists/nhsd-primary-care-domain-refsets-codes-for-intolerance-to-statins.csv",
column = "code",
)

# adverse reaction atorvastatin
adverse_reaction = codelist_from_csv("codelists/nhsd-primary-care-domain-refsets-codes-indicating-adverse-reaction-to-atorvastatin.csv",
column = "code",
)

# contraindication any statin
contraindication = codelist_from_csv("codelists/nhsd-primary-care-domain-refsets-codes-indicating-contraindication-to-any-statin.csv",
column = "code",
)

# declined statin
declined = codelist_from_csv("codelists/nhsd-primary-care-domain-refsets-statindec_cod.csv",
column = "code",
)

# any statin
statin_code = codelist_from_csv("codelists/openprescribing-all-statins.csv",
column = "code",
)


# qrisk
qrisk = codelist_from_csv(
"codelists/nhsd-primary-care-domain-refsets-qriskscore_cod.csv",
column = "code",
)

# cvd risk
cvd_risk = codelist_from_csv(
"codelists/opensafely-cvd-risk-assessment-score-qof.csv",
column = "code",
)

## Ethnicity
ethnicity5 = codelist_from_csv(
  "codelists/opensafely-ethnicity-snomed-0removed.csv",
  column="code",
  category_column="Label_6", # it's 6 because there is an additional "6 - Not stated" category, but this is not represented in SNOMED, instead corresponding to no ethnicity code
)

ethnicity16 = codelist_from_csv(
  "codelists/opensafely-ethnicity-snomed-0removed.csv",
  column="code",
  category_column="Label_16",
)