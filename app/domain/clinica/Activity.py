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
    Set of exams that person pass
    attr:
        ActivityId: serial str with format define in Ids.py
        MeetDate: date that patient must have to come to fill the form
        AttentionDate: timestamp when patient is attended
        EndDate: timestamp when the doctor gives the end of the form
        isActive: value to indicate state
        TypeServiceConstant: ForeignKey Constants (optional), services that hospital provides
        AptitudeConstant: ForeignKey Constants (optional), aptitude that doctor give base on form and other exams
        PersonId: ForeignKey Person, identifier of person
        ScheduleActivityId: ForeignKey ScheduleActivity, identifier of schedule
        CompanyProfileId: ForeignKey CompanyProfile, identifier of profile (set of exams)
        CreateUserId: ForeignKey User, identifier of user that creates the register
        CreateDate: timestamp for audit purpose
        WriteUserId: ForeignKey User, identifier of user that modify the register
        WriteDate: timestamp for audit purpose
    """

    ActivityId: Ids.ACTIVITY_ID
    MeetDate: date.strptime("%d-%m-%Y")
    AttentionDate: datetime.strptime("%d-%m-%Y") = None
    EndDate: datetime.strptime("%d-%m-%Y") = None
    isActive: bool = True
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
        return Constants.Service_TypeService.get(TypeServiceConstant)

    def get_AptitudeConstant(self, AptitudeConstant: str):
        return Constants.Activity_Aptitude.get(AptitudeConstant)

    def get_by_id(self, ActivityId: str):
        return ActivityRepository.get_by_id(ActivityId)
