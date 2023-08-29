import logging as logger
import random

from src.models.AccountInfo import AccountInfo
from src.models.AddressInfo import AddressInfo
from src.models.PersonalInfo import PersonalInfo
from faker import Faker

fake = Faker()


def get_random_personal_info(firstname=None, lastname=None, company=None, mobile_number=None):
    logger.debug("Generating personal information")
    personal_info = PersonalInfo(
        firstname=firstname if firstname else fake.first_name(),
        lastname=lastname if lastname else fake.last_name(),
        company=company if company else fake.company(),
        mobile_number=mobile_number if mobile_number else fake.phone_number()
    )
    logger.debug(f"Generated the following personal information: {personal_info}")
    return personal_info


def get_random_account_info(personal_info=None, email=None, password=None, dob=None):
    logger.debug("Generating account information")
    dob = dob if dob else fake.date_of_birth(minimum_age=18, maximum_age=80)
    account_info = AccountInfo(
        title=random.choice(["Mr.", "Mrs."]),
        name=personal_info.first_name + " " + personal_info.last_name if personal_info else fake.name(),
        email=email if email else fake.email(),
        password=password if password else fake.password(),
        birth_date=dob.day,
        birth_month=dob.month,
        birth_year=dob.year,
    )
    logger.debug(f"Generated the following account information: {account_info}")
    return account_info


def get_random_address_info(address_line_1=None, address_line_2=None, country=None, state=None, city=None,
                            zip_code=None):
    logger.debug("Generating address information")
    address_info = AddressInfo(
        address1=address_line_1 if address_line_1 else fake.street_address(),
        address2=address_line_2 if address_line_2 else fake.secondary_address(),
        country=country if country else random.choice(["United States", "Canada", "Australia", "New Zealand"]),
        state=state if state else fake.state(),
        city=city if city else fake.city(),
        zipcode=zip_code if zip_code else fake.zipcode(),
    )
    logger.debug(f"Generated the following personal information: {address_info}")
    return address_info
