from .models import Category
from app_settings.models import SiteSettings


def load_menu(request):
    try:
        settings = SiteSettings.load()
        sub_categories = settings.root_category.get_descendants(include_self=False)
        base_categories = Category.objects.filter(parent_id=settings.root_category.id).only('name', 'slug')
    except AttributeError as exc:
        sub_categories = {}
        base_categories = {}
    return {'main_menu': sub_categories, 'base_menu': base_categories}
