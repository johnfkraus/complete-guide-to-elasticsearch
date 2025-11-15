# pip install phonenumbers then

import pandas as pd
# import dataprep
import phonenumbers

num = phonenumbers.format_number(phonenumbers.parse("8006397663", 'US'), phonenumbers.PhoneNumberFormat.NATIONAL)

print(num)

# Source - https://stackoverflow.com/a/66233556
# Posted by victoria55
# Retrieved 2025-11-13, License - CC BY-SA 4.0

# from dataprep.clean import clean_phone
# df = pd.DataFrame({'phone': ['5555555', '5555555555', '18005555555']})
# clean_phone(df, 'phone')
# Phone Number Cleaning Report:
#     3 values cleaned (100.0%)
# Result contains 3 (100.0%) values in the correct format and 0 null values (0.0%)
#          phone     phone_clean
# 0      5555555        555-5555
# 1   5555555555    555-555-5555
# 2  18005555555  1-800-555-5555

# Source - https://stackoverflow.com/a/71793229
# Posted by Aizen Murtaza, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-13, License - CC BY-SA 4.0

from phonenumbers import country_code_for_region, format_number, PhoneMetadata, PhoneNumberFormat, parse as parse_phone
import re

def get_country_phone_pattern(country_code: str):
    mobile_number_example = PhoneMetadata.metadata_for_region(country_code).mobile.example_number
    formatted_phone = format_number(parse_phone(mobile_number_example, country_code), PhoneNumberFormat.INTERNATIONAL)
    without_country_code = " ".join(formatted_phone.split()[1:])
    return re.sub("\d", "*", without_country_code)

print(get_country_phone_pattern("KG"))  # *** *** ***
