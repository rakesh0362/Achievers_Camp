from django.contrib import admin
from achievers.models import CurrentAffairs, Vocabulary, ExamNotification, ExamAnalysis

# Register your models here.
admin.site.register(CurrentAffairs)
admin.site.register(Vocabulary)
admin.site.register(ExamNotification)
admin.site.register(ExamAnalysis)
