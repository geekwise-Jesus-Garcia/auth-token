from rest_framework import serializers
from leads.models import Lead

# lead serializers

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fiedss = "__all__"