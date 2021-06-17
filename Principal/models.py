from django.db import models

# Create your models here.
class Persona(models.Model):
    idpersona = models.AutoField(primary_key=True)
    DUI = models.CharField(max_length=9,unique=True)
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length=50)
    genero = models.CharField(max_length=1)
    numeroTelefono = models.CharField(max_length=50)
    correoElectronico = models.EmailField(max_length=254)
    rol = models.IntegerField()


class usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    idpersona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    contrasena = models.CharField(max_length=50)

class administrador(models.Model):
    idAdministrador = models.AutoField(primary_key=True)
    idpersona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    contrasena = models.CharField(max_length=50)

class zona(models.Model):
    codigoZona = models.AutoField(primary_key=True)
    departamento = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return str(self.codigoZona)

class asignacion(models.Model):
    comprobante = models.AutoField(primary_key=True)
    idAdmistrador = models.ForeignKey(administrador, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    codigoZona = models.ForeignKey(zona, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fechaDeAsignacion = models.DateField()

    def __str__(self):
        return str(self.comprobante)


class paqueteAlimentario(models.Model):
    codigo = models.AutoField(primary_key=True)
    idAdministrador = models.ForeignKey(administrador, on_delete=models.CASCADE)
    fechaDeExpedicion = models.DateField()
    fechaDeCaducidad = models.DateField()

    def __str__(self):
        return str(self.codigo) 

