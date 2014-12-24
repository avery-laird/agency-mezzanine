from django.contrib import admin
from mezzanine.conf import settings
from mezzanine.core.admin import DisplayableAdmin, DisplayableAdminForm, TabularDynamicInlineAdmin
from mezzanine.pages.models import Page, RichTextPage, Link
from mezzanine.pages.admin import PageAdmin
from mezzanine.utils.urls import admin_url
from theme.models import IconBlurb, HomePage, Section, Portfolio, TimeLine, Team

class IconBlurbInline(TabularDynamicInlineAdmin):
    model = IconBlurb

class SectionInline(TabularDynamicInlineAdmin):
    model = Section

class PortfolioInline(TabularDynamicInlineAdmin):
    model = Portfolio

class TimeLineInline(TabularDynamicInlineAdmin):
    model = TimeLine

class TeamInline(TabularDynamicInlineAdmin):
    model = Team
#class SlideInline(TabularDynamicInlineAdmin):
#    model = Slide

class HomePageAdmin(PageAdmin):
    inlines = (SectionInline, IconBlurbInline, PortfolioInline, TimeLineInline, TeamInline)

admin.site.register(HomePage, HomePageAdmin)

# Register your models here.
