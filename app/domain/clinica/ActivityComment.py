from dataclasses import dataclass
from datetime import datetime

import app.domain.clinica.Constants as Constants
import app.domain.Ids as Ids


@dataclass
class ActivityComment:
    """
    Opcional: Puente entre actividad y comentarios sobre examenes
    """

    ActivityCommentId: int
    ActivityId: Ids.ACTIVITY_ID
    Description: str(10000)
    TypeCommentConstant: str(1)
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()

    def get_TypeCommentConstant(self, TypeComentConstant: str):
        return Constants.ConstantService_TypeService.get(TypeComentConstant)
