from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class Company:
    """
    Company that have relation with hospital
    attr:
        CompanyId: str with specific format
        Description: name
        AddressId: ForeignKey CityDistrict, identifier of district
        Address: Full address name
        Password: hash of password
        isActive: value to indicate state
        CreateUserId: ForeignKey User, identifier of user that creates the register
        CreateDate: timestamp for audit purpose
        WriteUserId: ForeignKey User, identifier of user that modify the register
        WriteDate: timestamp for audit purpose
    """

    CompanyId: Ids.COMPANY_ID
    Description: str(100)
    AddressId: Ids.CITYDISTRICT_ID
    Address: str(300)
    Password: str(128)
    isActivate: bool = True
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
