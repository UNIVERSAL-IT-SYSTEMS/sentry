from __future__ import absolute_import

from sentry.models import Activity

from .mail import ActivityMailDebugView


class DebugAssignedEmailView(ActivityMailDebugView):
    def get_activity(self, request, event):
        return {
            'type': Activity.ASSIGNED,
            'user': request.user,
            'data': {
                'assignee': '10000000',
                'assigneeEmail': 'foo@example.com',
            }
        }


class DebugSelfAssignedEmailView(ActivityMailDebugView):
    def get_activity(self, request, event):
        return {
            'type': Activity.ASSIGNED,
            'user': request.user,
            'data': {
                'assignee': str(request.user.id),
                'assigneeEmail': request.user.email,
            }
        }
