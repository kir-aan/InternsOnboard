from rest_framework.serializers import ModelSerializer
from InternsOnboardMain.models import internshipPost

class internshipSerializer(ModelSerializer):
    class Meta:
        model = internshipPost
        fields = [
            'id',
            'company_name',
            'discription',
            'created_at'
        ]