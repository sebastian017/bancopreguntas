from __future__ import unicode_literals
from django.db import models
from django.contrib import admin 

class estudiante(models.Model):
		cod_estudiante = models.IntegerField()
		nom_estudiante = models.CharField(max_length=30)
		dir_estudiante = models.CharField(max_length=30)
		tel_estudiante = models.IntegerField(max_length=20)
		email_estudiante = models.EmailField(max_length=30)
		clave_estudiante = models.CharField(max_length=20)
		semestre_estudiante = models.IntegerField(max_length=3)
		def __unicode__(self):
			return u'%s'%self.cod_estudiante
	

class estudianteAdmin(admin.ModelAdmin):
		list_display = ('cod_estudiante','nom_estudiante','dir_estudiante','tel_estudiante',
		'email_estudiante','clave_estudiante','semestre_estudiante')


class docente(models.Model):
		cod_docente = models.IntegerField()
		nom_docente = models.CharField(max_length=30)
		dir_docente= models.CharField(max_length=30)
		tel_docente = models.IntegerField(max_length=20)
		email_docente = models.EmailField(max_length=30)
		clave_docente = models.CharField(max_length=20)
		def __unicode__(self):
			return u'%s'%self.cod_docente


class docenteAdmin(admin.ModelAdmin):
		list_display = ('cod_docente','nom_docente','dir_docente','tel_docente',
		'email_docente','clave_docente',)

class grupo(models.Model):
		cod_grupo = models.IntegerField(max_length=10)
		cod_docente = models.ForeignKey(docente)
		nom_grupo = models.CharField(max_length=30)
		cod_estudiante = models.ForeignKey(estudiante)
		
		def __unicode__(self):
			return u'%s'%self.cod_grupo

class grupoAdmin(admin.ModelAdmin):
		list_display = ('cod_grupo','cod_docente','nom_grupo','cod_estudiante')

admin.site.register(estudiante,estudianteAdmin)
admin.site.register(docente,docenteAdmin)
admin.site.register(grupo,grupoAdmin)
