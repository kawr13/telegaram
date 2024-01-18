from distutils.command import upload
from tortoise import Tortoise, fields, models
from config import post_pass
import re
import os

DATABASE_URL = "sqlite://database.db"

class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255)
    usertelegram_id = fields.IntField(unique=True)
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255)
    password = fields.CharField(max_length=255, null=True, blank=True)

class StatusConteiner(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name='status_conteiner')
    number = fields.CharField(max_length=255, unique=True)
    data = fields.DatetimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-data']
        
class ImagesConteiner(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name='images_conteiner')
    conteiner = fields.ForeignKeyField('models.StatusConteiner', related_name='images_conteiner')
    image = fields.CharField(max_length=300)
    update_data = fields.DatetimeField(auto_now=True)

        
    
async def init():
    await Tortoise.init(
        db_url=f'postgres://itmadmin:{post_pass}@localhost:5432/myproject',
        modules={'models': ['models']},  # указываем модуль, где определены модели
    )
    await Tortoise.generate_schemas()

async def create_user(username, usertelegram_id, first_name, last_name, password):
    await User.create(
        username=username,
        usertelegram_id=usertelegram_id,
        first_name=first_name,
        last_name=last_name,
        password=password,
    )

async def create_conteiner(user, number, data):
    await StatusConteiner.create(
        user=user,
        number=number,
        data=data,
    )
    
async def get_user(usertelegram_id):
    user = await User.get_or_none(usertelegram_id=usertelegram_id)
    return user

async def get_users():
    return await User.all()


async def get_first_conteiner(usertelegram_id):
    conteiner = await StatusConteiner.filter(user__usertelegram_id=usertelegram_id).first()
    return conteiner

async def get_conteiner(conteiner):
    return await StatusConteiner.get_or_none(number=conteiner)