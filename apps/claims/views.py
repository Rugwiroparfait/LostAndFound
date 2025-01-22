from rest_framework import viewsets , permissions, status
from rest_framework.response import Response
from .models import Claim
from .serializers import ClaimSerializer
from .task import send_claim_notification

class ClaimViewSet(viewsets.ModelViewSet):
    serializer_class = ClaimSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Claim.objects.all()
        return Claim.objects.filter(claimer=self.request.user)
    
    def perform_create(self,serializer):
        claim = serializer.save(claimer=self.request.user)
        send_claim_notification.delay(claim.id)

    def update(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response(
                {"details:" "Only staff members can update claim status."},
                status=status.HTTP_403_FORBIDDEN
            )
        return super.update(request, *args, **kwargs)
    