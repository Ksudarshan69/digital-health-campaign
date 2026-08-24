from .models import CampaignSettings


def campaign_settings(request):
    """
    Makes CampaignSettings available in every template as {{ campaign }},
    so navbar/footer/hero content is never hard-coded (spec section 25).
    """
    return {"campaign": CampaignSettings.load()}
