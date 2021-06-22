from datetime import date
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import Subscribers, Invites
from rest_framework.response import Response
from rest_framework import status
from .serializers import InvitesSerializer
from django.db.models import FilteredRelation, Q
# Если абонент Б отключил возможность приглашения, то уведомить абонента А
# Если абонент Б уже активировал инвайт, то вернуть соответствующий ответ
# Если абонент Б был ранее приглашен, но не успел активировать инвайт,
# то предыдущий инвайт становится не активным. Каждый новый инвайт заменяет предыдущий
# Абонент А может приглашать абонента Б только раз в сутки

# Status = [ACTIVE, NOT ACTIVE, ACCEPTED]
# Select * from subscribers where phone = numberA
# Select count(*) from invites where sender_subs_id = ?1 and start_date &gt; {полночь}
# Select count(*) from invites where sender_subs_id = ?1 and start_date &gt; {Первое число месяца, полночь}
# Select count(*) from invites where sender_subs_id = ?1 and receiver_subs_id = ?2 and start_date &gt; {полночь}

# Create your views here.

@api_view(['GET'])
def invitation(request, phone_sender, phone_recipient):
    sender_obj, created1 = Subscribers.objects.get_or_create(phone=phone_sender)
    recipient_obj, created2 = Subscribers.objects.get_or_create(phone=phone_recipient)

    if recipient_obj.active:
        if len(Invites.objects.filter(sender_subs_id=sender_obj.id,
                                      start_date__day=date.today().day)) < 5:
            if len(Invites.objects.filter(sender_subs_id=sender_obj.id,
                                          start_date__month=date.today().month)) < 30:
                serializer = InvitesSerializer(invitation, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
    elif recipient_obj.notactive:
        invitation.status = 'Not active'

    else:
        invitation.status = 'Accepted'


