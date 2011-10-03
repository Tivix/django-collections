# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Collection.description'
        db.delete_column('dynamic_collections_collection', 'description')

        # Adding field 'Collection.body_text'
        db.add_column('dynamic_collections_collection', 'body_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Collection.description'
        db.add_column('dynamic_collections_collection', 'description', self.gf('django.db.models.fields.TextField')(default='Learn more with National Geographic!'), keep_default=False)

        # Deleting field 'Collection.body_text'
        db.delete_column('dynamic_collections_collection', 'body_text')


    models = {
        'dynamic_collections.collection': {
            'Meta': {'ordering': "['title']", 'object_name': 'Collection'},
            'body_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'create_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'parameters': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'update_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['dynamic_collections']
