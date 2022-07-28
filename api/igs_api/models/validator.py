import re
from rest_framework import serializers

def validate_email(email):
    regex = '^(.*\w)(@igs-software\.com\.br)$'
    if re.search(regex,email):
        return True
    raise serializers.ValidationError("Email must follow the pattern: email@igs-software.com.br")
