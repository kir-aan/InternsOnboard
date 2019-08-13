from rest_framework.serializers import ModelSerializer
from InternsOnboardMain.models import internshipPost

class internshipSerializer(ModelSerializer):
    class Meta:
        model = internshipPost
        fields = [
            'id',
            'owner',
            'company_name',
            'description',
            'created_at',
        ]