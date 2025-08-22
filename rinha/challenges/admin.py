from django.contrib import admin
from .models import Challenge, ChallengeSubmission

class ChallengeSubmissionInline(admin.TabularInline):
    model = ChallengeSubmission
    extra = 0
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ['title', 'judge_user', 'tags']
    search_fields = ['title', 'statement', 'tags']
    inlines = [ChallengeSubmissionInline]

@admin.register(ChallengeSubmission)
class ChallengeSubmissionAdmin(admin.ModelAdmin):
    list_display = ['challenge', 'competitor', 'created_at', 'updated_at']
    list_filter = ['challenge', 'competitor', 'created_at']
    search_fields = ['challenge__title', 'competitor__username', 'code', 'observations']
    readonly_fields = ['created_at', 'updated_at']
