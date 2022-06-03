from dataclasses import dataclass
from datetime import datetime

import app.domain.clinica.Constants as Constants
import app.domain.Ids as Ids


@dataclass
class Person:
    """
    Person data
    attr:
        PersonId: str with format define in Ids.py
        TypeDocumentConstant: ForeignKey Constants (optional), type of document
        NumberDocument: document id
        Name: name
        GenderConstant: ForeignKey Constants (optional), gender of person
        BirthDay: date of birth
        TypeHealthConstant: ForeignKey Constants (optional), have sure heatlh
        MailAddress: mail
        PhoneNumber: number of person
        AddressId: ForeignKey CityDistrict, identifier of district
        Address: Full address name
        Password: hash of password
        isActive: value to indicate state
        CreateUserId: ForeignKey User, identifier of user that creates the register
        CreateDate: timestamp for audit purpose
        WriteUserId: ForeignKey User, identifier of user that modify the register
        WriteDate: timestamp for audit purpose
    """

    PersonId: Ids.PERSON_ID
    TypeDocumentConstant: str(1)
    NumberDocument: str(15)
    Name: str(200)
    GenderConstant: str(1)
    BirthDay: datetime.now()
    TypeHealthConstant: str(1)
    mailaddress: str(300)
    phonenumber: str(24)
    AddressId: Ids.CITYDISTRICT_ID
    Address: str(300)
    Password: str(128)
    isActivate: bool = True
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()

    def get_TypeDocumentConstant(self, TypeDocumentConstant: str):
        return Constants.Person_TypeDocument.get(TypeDocumentConstant)

    def get_TypeHealthConstant(self, TypeHealthConstant: str):
        return Constants.Person_Gender.get(TypeHealthConstant)

    def get_GenderConstant(self, GenderConstant: str):
        return Constants.Person_TypeHealth.get(GenderConstant)
