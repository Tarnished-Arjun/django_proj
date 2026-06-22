from rest_framework import serializers

from .models import CandidateProfile


class CandidateProfileSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = CandidateProfile

        fields = '__all__'

        read_only_fields = ['user']