from flask_cors import cross_origin
#from flask import request, jsonify
from middleware.auth import login_required, admin_required
from models.notifications import Notifications
#from services import notifications_service

# User actions
@cross_origin()
@login_required
def get_my_list(user_id: int) -> dict:
    """Fetch my notifications"""
    # TODO: get all notifications for my user_id
    # list with pagination and some filters, default filter is ack=0
    return {'status': 'OK', 'user': user_id}, 200

@cross_origin()
@login_required
def get_my_notif_details(user_id: int, notification_id: int) -> dict:
    """Get notification information"""
    # TODO: get notifications data
    return {'status': 'OK', 'user': user_id, 'ntf_id': notification_id}, 200

@cross_origin()
@login_required
def ack(user_id: int, notification_id: int) -> dict:
    """Acknowledge notification"""
    Notifications.update(
        conditions={'id': notification_id, 'target_user_id': user_id},
        new_values={'ack': 1}
    )
    return {'status': 'OK'}, 201

# Admin actions
@cross_origin()
@admin_required
def get_all(_, notification_id: int) -> dict:
    """Fetch all notifications"""
    # TODO: Fetch all notifiations on the system
    # allow quer string params for pagination and filters
    return {'status': 'OK', 'notification_id': notification_id}, 200

@cross_origin()
@admin_required
def get_notif_details(_, notification_id: int) -> dict:
    """Get notification information"""
    # TODO: get notifications data
    return {'status': 'OK', 'id': notification_id}, 200

@cross_origin()
@admin_required
def add_notification(_) -> dict:
    """Add new notification"""
    # TODO: get data provided via json in the request body and
    # add new notification
    return {'status': 'OK'}, 201

@cross_origin()
@admin_required
def update_notification(_, notification_id: int) -> dict:
    """Update notification info"""
    # TODO: Get data provided via body json and update the data of
    # provided notification_id
    return {'status': 'OK', 'id': notification_id}, 200

@cross_origin()
@admin_required
def del_notification(_, notification_id: int) -> dict:
    """Delete Notification"""
    Notifications.delete(conditions={'id': notification_id})
    return {'status': 'OK'}, 200
