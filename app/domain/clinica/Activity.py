import app.domain.clinica.Constants as Constants
import app.domain.Ids as Ids

from dataclasses import dataclass
from datetime import date, datetime

# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     # This is necessary to prevent circular imports
#     from app.adapters.ActivityRepository import ActivityRepository


@dataclass
class Activity:
    """
    Conjunto de examenes que le pertenecen a una persona
    """

    ActivityId: Ids.ACTIVITY_ID
    MeetDate: date.strptime("%d-%m-%Y")
    AttentionDate: datetime.strptime("%d-%m-%Y") = None
    EndDate: datetime.strptime("%d-%m-%Y") = None
    isActive: bool = False
    TypeServiceConstant: str(1)
    AptitudeConstant: str(1)
    PersonId: Ids.PERSON_ID
    ScheduleActivityId: Ids.SCHEDULEACTIVITY_ID
    CompanyProfileId: Ids.COMPANYPROFILE_ID
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()

    def get_TypeServiceConstant(self, TypeServiceConstant: str):
        return Constants.ConstantService_TypeService.get(TypeServiceConstant)

    def get_AptitudeConstant(self, AptitudeConstant: str):
        return Constants.ConstantActivity_Aptitude.get(AptitudeConstant)

    def get_by_id(self, ActivityId: str):
        return ActivityRepository.get_by_id(ActivityId)
