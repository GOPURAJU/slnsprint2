from rest_framework import viewsets
from rest_framework.response import Response
from .support_serializers import Ticketserializers, DSATicketserializers,FranchiseeTicketserializers
from .models import Ticket, DSATicket,FranchiseeTicket


class Ticketviewsets(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = Ticketserializers

class DSATicketviewsets(viewsets.ModelViewSet):
    queryset = DSATicket.objects.all()
    serializer_class = DSATicketserializers



    
class FranchiseeTicketviewsets(viewsets.ModelViewSet):
    queryset = FranchiseeTicket.objects.all()
    serializer_class = FranchiseeTicketserializers

