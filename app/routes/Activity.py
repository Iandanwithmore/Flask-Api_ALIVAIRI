import json

import requests
from flask import Blueprint, current_app, jsonify, request

from app.adapters.ActivityPDF import ActivityPDF
from app.adapters.ActivityRepository import ActivityRepository
from app.decorators import user_required
from app.fn_base import FnBase

loActivityRepo = ActivityRepository()
loActivityPdf = ActivityPDF()

Activity = Blueprint("actividad", __name__, url_prefix="/actividad")


@Actividad.get("/<string:ActivityID>")
@user_required
def get_activity_by_id(ActivityID):
    R1 = ActivityRepository.get_by_id(ActivityID)
    return jsonify(R1), FnBase.get_status_code(R1.ok)
