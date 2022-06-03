from datetime import datetime

import app.domain.Ids as Ids


class ExamSubtitle:
    """
    Group of indicators with relation in exam
    attr:
        ExamSubtitleId: serial int
        ExamId: ForeignKey Exam, identifier of exam
        ExamTemplateOrder: PForeignKey ExamTemplate, identifier of template
        CreateUserId: ForeignKey User, identifier of user that creates the register
        CreateDate: timestamp for audit purpose
    """

    ExamSubtitleId: int
    ExamId: Ids.CONSENT_ID
    ExamTemplateId: Ids.EXAMTEMPLATE_ID
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
