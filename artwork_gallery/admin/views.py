from django.shortcuts import render

@login_required()
@permission_required("artworks.can_vote")
def admin():
    return 'rtn'
