from peewee import *
import psycopg2


#from peewee import SqliteDatabase, AutoField, CharField, DateField, ForeignKeyField, Model

pg_db = PostgresqlDatabase("ejemplo", user="labuser", password="labuser", host="192.168.56.101", port=5432)

class Profesores(Model):
   maestro_id = AutoField()
   nombre = CharField()
   apellido = CharField()
   telefono = CharField()
   email = CharField(unique=True)

   class Meta:
       database = pg_db

class Clases(Model):
   clase_id = AutoField()
   cod_curso = CharField()
   fecha_inicio_curso = DateField()
   fecha_fin_curso = DateField()
   horario = CharField()
   maestro_id = ForeignKeyField(Profesores)

   class Meta:
       database = pg_db

pg_db.connect()
pg_db.create_tables([Profesores, Clases])