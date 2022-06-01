from dataclasses import dataclass
from datetime import datetime

import app.domain.clinica.Constants as Constants
import app.domain.Ids as Ids


@dataclass
class Person:
    """
    Examen que tiene asociado indicadores
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
        return Constants.ConstantPerson_TypeDocument.get(TypeDocumentConstant)

    def get_TypeHealthConstant(self, TypeHealthConstant: str):
        return Constants.ConstantPerson_Gender.get(TypeHealthConstant)

    def get_GenderConstant(self, GenderConstant: str):
        return Constants.ConstantPerson_TypeHealth.get(GenderConstant)
