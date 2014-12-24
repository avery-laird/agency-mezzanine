# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Portfolio.page_ptr'
        db.delete_column(u'theme_portfolio', u'page_ptr_id')

        # Adding field 'Portfolio.id'
        db.add_column(u'theme_portfolio', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=4, primary_key=True),
                      keep_default=False)

        # Adding field 'Portfolio._order'
        db.add_column(u'theme_portfolio', '_order',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Portfolio.homepage'
        db.add_column(u'theme_portfolio', 'homepage',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=4, related_name='portfolio', to=orm['theme.HomePage']),
                      keep_default=False)

        # Adding field 'Portfolio.section'
        db.add_column(u'theme_portfolio', 'section',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=4, related_name='portfolio', to=orm['theme.Section']),
                      keep_default=False)

        # Adding field 'Portfolio.icon'
        db.add_column(u'theme_portfolio', 'icon',
                      self.gf('mezzanine.core.fields.FileField')(default=4, max_length=255),
                      keep_default=False)

        # Adding field 'Portfolio.title'
        db.add_column(u'theme_portfolio', 'title',
                      self.gf('django.db.models.fields.CharField')(default=4, max_length=50),
                      keep_default=False)

        # Adding field 'Portfolio.description'
        db.add_column(u'theme_portfolio', 'description',
                      self.gf('django.db.models.fields.CharField')(default=4, max_length=140),
                      keep_default=False)

        # Adding field 'Portfolio.link'
        db.add_column(u'theme_portfolio', 'link',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=2000, blank=True),
                      keep_default=False)

        # Deleting field 'HomePage.featured_portfolio'
        db.delete_column(u'theme_homepage', 'featured_portfolio_id')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Portfolio.page_ptr'
        raise RuntimeError("Cannot reverse this migration. 'Portfolio.page_ptr' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Portfolio.page_ptr'
        db.add_column(u'theme_portfolio', u'page_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'Portfolio.id'
        db.delete_column(u'theme_portfolio', u'id')

        # Deleting field 'Portfolio._order'
        db.delete_column(u'theme_portfolio', '_order')

        # Deleting field 'Portfolio.homepage'
        db.delete_column(u'theme_portfolio', 'homepage_id')

        # Deleting field 'Portfolio.section'
        db.delete_column(u'theme_portfolio', 'section_id')

        # Deleting field 'Portfolio.icon'
        db.delete_column(u'theme_portfolio', 'icon')

        # Deleting field 'Portfolio.title'
        db.delete_column(u'theme_portfolio', 'title')

        # Deleting field 'Portfolio.description'
        db.delete_column(u'theme_portfolio', 'description')

        # Deleting field 'Portfolio.link'
        db.delete_column(u'theme_portfolio', 'link')

        # Adding field 'HomePage.featured_portfolio'
        db.add_column(u'theme_homepage', 'featured_portfolio',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['theme.Portfolio'], null=True, blank=True),
                      keep_default=False)


    models = {
        u'pages.page': {
            'Meta': {'ordering': "(u'titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2, 3)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'theme.homepage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'HomePage', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'content_heading': ('django.db.models.fields.CharField', [], {'default': "'About us!'", 'max_length': '200'}),
            'featured_works_heading': ('django.db.models.fields.CharField', [], {'default': "'Featured Works'", 'max_length': '200'}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'latest_posts_heading': ('django.db.models.fields.CharField', [], {'default': "'Latest Posts'", 'max_length': '200'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'subheading': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'theme.iconblurb': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'IconBlurb'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blurbs'", 'to': u"orm['theme.HomePage']"}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blurbs'", 'to': u"orm['theme.Section']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'theme.portfolio': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Portfolio'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'portfolio'", 'to': u"orm['theme.HomePage']"}),
            'icon': ('mezzanine.core.fields.FileField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'portfolio'", 'to': u"orm['theme.Section']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'theme.section': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Section'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sections'", 'to': u"orm['theme.HomePage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subheader': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'theme.slide': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Slide'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'slides'", 'to': u"orm['theme.HomePage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['theme']