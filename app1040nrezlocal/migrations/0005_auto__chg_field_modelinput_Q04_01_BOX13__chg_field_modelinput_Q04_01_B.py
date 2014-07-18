# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'modelInput.Q04_01_BOX13'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX13', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'modelInput.Q04_01_BOX12b'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX12b', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'modelInput.Q04_01_BOX16'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX16', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'modelInput.Q04_01_BOX17'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX17', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'modelInput.A02'
        db.alter_column(u'app1040nrezlocal_modelinput', 'A02', self.gf('django.db.models.fields.CharField')(max_length=128, null=True))

        # Changing field 'modelInput.Q04_01_BOX19'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX19', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'modelInput.A01'
        db.alter_column(u'app1040nrezlocal_modelinput', 'A01', self.gf('django.db.models.fields.CharField')(max_length=128, null=True))

        # Changing field 'modelInput.Q04_01_BOX12a'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX12a', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'modelInput.Q04_01_BOX3'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX3', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'modelInput.Q04_01_BOX18'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX18', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'modelInput.Q04_01_BOX1'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX1', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'modelInput.Q04_01_BOX6'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX6', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'modelInput.Q04_01_BOX20'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX20', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'modelInput.Q04_01_BOX4'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX4', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'modelInput.Q04_01_BOX5'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX5', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'modelInput.Q04_01_BOX2'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX2', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'modelInput.Q04_01_BOX15'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX15', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'modelInput.Q04_01_BOX13'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX13', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'modelInput.Q04_01_BOX12b'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX12b', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'modelInput.Q04_01_BOX16'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX16', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'modelInput.Q04_01_BOX17'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX17', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'modelInput.A02'
        db.alter_column(u'app1040nrezlocal_modelinput', 'A02', self.gf('django.db.models.fields.CharField')(default='', max_length=128))

        # Changing field 'modelInput.Q04_01_BOX19'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX19', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'modelInput.A01'
        db.alter_column(u'app1040nrezlocal_modelinput', 'A01', self.gf('django.db.models.fields.CharField')(default='', max_length=128))

        # Changing field 'modelInput.Q04_01_BOX12a'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX12a', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'modelInput.Q04_01_BOX3'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX3', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'modelInput.Q04_01_BOX18'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX18', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'modelInput.Q04_01_BOX1'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX1', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'modelInput.Q04_01_BOX6'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX6', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'modelInput.Q04_01_BOX20'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX20', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'modelInput.Q04_01_BOX4'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX4', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'modelInput.Q04_01_BOX5'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX5', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'modelInput.Q04_01_BOX2'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX2', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'modelInput.Q04_01_BOX15'
        db.alter_column(u'app1040nrezlocal_modelinput', 'Q04_01_BOX15', self.gf('django.db.models.fields.IntegerField')(default=0))

    models = {
        u'app1040nrezlocal.model1040nrez': {
            'A01': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'A02': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'A03': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'A04': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'A05': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'A06': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'A07': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'A08': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'L03': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L04': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L05': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L06': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L07': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L08': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L09': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L10': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L11': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L12': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L13': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L14': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L15': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L16': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L17': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L18a': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L18b': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L19': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L20': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L21': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L22': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L23a': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L24': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L25': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'L26': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'Meta': {'object_name': 'model1040NREZ'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app1040nrezlocal.modelinput': {
            'A01': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'A02': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'modelInput'},
            'Q04_01_BOX1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Q04_01_BOX12a': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Q04_01_BOX12b': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Q04_01_BOX13': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Q04_01_BOX15': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Q04_01_BOX16': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Q04_01_BOX17': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Q04_01_BOX18': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Q04_01_BOX19': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Q04_01_BOX2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Q04_01_BOX20': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Q04_01_BOX3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Q04_01_BOX4': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Q04_01_BOX5': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Q04_01_BOX6': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['app1040nrezlocal']