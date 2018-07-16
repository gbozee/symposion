from symposion.proposals.models import ProposalSection
from django.contrib.auth.models import Permission

def reviews(request):
    sections = []
        
    for section in ProposalSection.objects.all():
        # if request.user.has_perm("reviews.can_review_%s" % section.section.slug):
        if request.user.has_perm('symposion_reviews.add_review'):
            sections.append(section)
    return {
        "review_sections": sections,
    }
