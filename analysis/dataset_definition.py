###################################################
# This script defines a function that 
#   creates statin prescribing variables,
#   and whether someone has a qrisk score
#   for use in downstream code
#
# Author: Colm Andrews 
#   Bennett Institute for Applied Data Science
#   University of Oxford, 2024
#####################################################################

from ehrql import Dataset, years
from ehrql.tables.tpp import (
    medications, 
    practice_registrations,
    clinical_events)

import codelists

# Function to define dataset #
def make_dataset_statin(index_date, end_date):
    
    dataset = Dataset()

    ## Define relevant variables

    dataset.atorvastatin = medications.where(medications.dmd_code.is_in(statin_code)
            ).where(
                medications.date.is_on_or_between(index_date, end_date)
            ).exists_for_patient()

    dataset.noteligible = clinical_events.where(
        clinical_events.snomedct_code.is_in(codelists.intolerence)
    ).where(
        clinical_events.snomedct_code.is_in(codelists.adverse_reaction)
    ).where(
        clinical_events.snomedct_code.is_in(codelists.contraindication)
    ).where(
        clinical_events.snomedct_code.is_in(codelists.declined)
    ).where(
        clinical_events.snomedct_code.is_in(codelists.intolerence)
    ).exists_for_patient

    dataset.qrisk = clinical_events.where(
        clinical_events.snomedct_code.is_in(codelists.qrisk)
        ).exists_for_patient()
    


    return dataset