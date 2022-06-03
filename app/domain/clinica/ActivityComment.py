from dataclasses import dataclass
from datetime import datetime

import app.domain.clinica.Constants as Constants
import app.domain.Ids as Ids


@dataclass
class ActivityComment:
    """
    Complement to Activity that gives comments about the form
    attr:
        ActivityCommentId: serial int
        ActivityId: ForeignKey Activity, identifier of activity
        Description: comment of activity form
        TypeCommentConstant: ForeignKey Constants (optional), types of comment in activity
        CreateUserId: ForeignKey User, identifier of user that creates the register
        CreateDate: timestamp for audit purpose
    """

    ActivityCommentId: int
    ActivityId: Ids.ACTIVITY_ID
    Description: str(10000)
    TypeCommentConstant: str(1)
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()

    def get_TypeCommentConstant(self, TypeComentConstant: str):
        return Constants.Service_TypeService.get(TypeComentConstant)
