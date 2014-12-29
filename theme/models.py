from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to

# Ideally, I would refactor this code with a "subsection" model, which all of the subsections inherit from
# that contains the homepage and section foreignkey.

class messages(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=140)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    class Meta:
	verbose_name = _("Message")
	verbose_name_plural = _("Messages")

class HomePage(Page, RichText):
    '''
    A page representing the format of the home page
    '''
    heading = models.CharField(max_length=200,
        help_text="The heading under the icon blurbs")
    subheading = models.CharField(max_length=200,
        help_text="The subheading just below the heading")
    featured_works_heading = models.CharField(max_length=200,
        default="Featured Works")
#    featured_portfolio = models.ForeignKey("Portfolio", blank=True, null=True,
#        help_text="If selected items from this portfolio will be featured "
#                  "on the home page.")
    content_heading = models.CharField(max_length=200,
        default="About us!")
    latest_posts_heading = models.CharField(max_length=200,
        default="Latest Posts")

    class Meta:
        verbose_name = _("Home page")
        verbose_name_plural = _("Home pages")


class Section(Orderable):
    '''
    Multiple Sections for a one page site
    '''
    homepage = models.ForeignKey(HomePage, related_name="sections")
    header = models.CharField(max_length=200)
    subheader = models.CharField(max_length=200)
    content = RichTextField()
   
    def edit_subsections(self):
        '''
        Returns a link to this items change form
        '''
        if self.id:
            return '<a onclick="return showAddAnotherPopup(this);" href="%s">Edit documents</a>' % admin_url(self.__class__, "change", self.id)
        return ''

    edit_subsections.allow_tags = True

    def __unicode__(self):
	return self.header
    

class Slide(Orderable):
    '''
    A slide in a slider connected to a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="slides")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.Slide.image", "slider"),
        format="Image", max_length=255, null=True, blank=True)


class IconBlurb(Orderable):
    '''
    An icon box on a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="blurbs")
    section = models.ForeignKey(Section, related_name="blurbs")
#    icon = FileField(verbose_name=_("Image"),
#        upload_to=upload_to("theme.IconBlurb.icon", "icons"),
#        format="Image", max_length=255)
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    content = models.TextField()
    link = models.CharField(max_length=2000, blank=True,
        help_text="Optional, if provided clicking the blurb will go here.")

class TimeLine(Orderable):

    homepage = models.ForeignKey(HomePage, related_name="timeline")
    section = models.ForeignKey(Section, related_name="timeline")
    header = models.CharField(max_length=140)
    subheader = models.CharField(max_length=140)
    content = RichTextField()
    image = FileField(verbose_name=_("Image"),
	upload_to=upload_to("theme.TimeLine.icon", "icons"),
	format="Image", max_length=255)

class Portfolio(Orderable):
    '''
    A collection of individual portfolio items
    '''
    homepage = models.ForeignKey(HomePage, related_name="portfolio")
    section = models.ForeignKey(Section, related_name="portfolio")
    icon = FileField(verbose_name=_("Image"),
	upload_to=upload_to("theme.Portfolio.icon", "icons"),
	format="Image", max_length=255)
    title = models.CharField(max_length=50)
    #ADD CATEGORIES TO DESCRIPTION TO FILTER BY TAG
    description = models.CharField(max_length=140)
    link = models.CharField(max_length=2000, blank=True,
	help_text = "Optional link to project.")

class Team(Orderable):
    '''
    Team photos, name, job description, and social media bar (twitter, facebook, linkedin)
    '''
    homepage = models.ForeignKey(HomePage, related_name="team")
    section = models.ForeignKey(Section, related_name="team")
    profile_picture = FileField(verbose_name=_("Image"),
	upload_to=upload_to("theme.Team.icon", "icons"),
	format="Image", max_length=255)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    twitter_link = models.CharField(max_length=2000, blank=True)
    facebook_link = models.CharField(max_length=2000, blank=True)
    linkedin_link = models.CharField(max_length=2000, blank=True)
# Create your models here.
