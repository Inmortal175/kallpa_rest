from user.models import User

from rest_framework.serializers import ModelSerializer

class RegisterClientSerializer(ModelSerializer):
  class Meta: 
    model = User
    fields=[
      'id',
      'email',
      'username',
      'password',
      'id_rol',
    ]
  
  def create(self, validated_data):
    password = validated_data.pop('password', None)
    instance = self.Meta.model(**validated_data)

    if password is not None:
      instance.set_password(password)
    instance.save()
    return instance

class UserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'email', 'username','nombres', 'apellido_paterno',
     'apellido_materno', 'celular', 'documento_identidad', 'kallpa_punto', 'fecha_nac',
     'profile', 'es_validado', 'id_rol']

class UserDetailSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'email', 'username', 'id_rol']

class ClientUserUpdateSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ['nombres', 'apellido_paterno', 'apellido_materno', 'celular', 'documento_identidad', 'profile']