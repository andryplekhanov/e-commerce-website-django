from app_settings.models import SiteSettings


def get_delivery_price(total, type_delivery):
    settings = SiteSettings.load()
    common_delivery_price = settings.common_delivery_price
    edge_for_free_delivery = settings.edge_for_free_delivery
    express_delivery_price = settings.express_delivery_price
    if type_delivery == '2':
        return express_delivery_price
    if total < edge_for_free_delivery:
        return common_delivery_price
    else:
        return 0
