from django.core.exceptions import ValidationError
import os

def validate_file_size(value):
    filesize = value.size
    
    if filesize > 26214400:
        raise ValidationError("File Size Exceeds 25MB!")
    else:
        return value

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.ppt', '.pptx', '.csv']
    
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported File Type!')