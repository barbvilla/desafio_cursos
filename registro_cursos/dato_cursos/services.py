from dato_cursos.models import Profesor, Curso, Estudiante, Direccion
from datetime import date

def crear_profesor(rut: str, nombre: str, apellido: str, activo: bool, creado_por: str):
    profesor = Profesor(rut=rut, nombre=nombre, apellido=apellido, activo=activo, creado_por=creado_por)
    profesor.save()
    return profesor

def crear_curso(codigo: str, nombre: str, version: int):
    curso = Curso(codigo=codigo, nombre=nombre, version=version)
    curso.save()
    return curso

def crear_estudiante(rut: str, nombre: str, apellido: str, fecha_nac: date, activo: bool, creado_por: str):
    estudiante = Estudiante(rut=rut, nombre=nombre, apellido=apellido, fecha_nac=fecha_nac, activo=activo, creado_por=creado_por)
    estudiante.save()
    return estudiante

def crear_direccion(calle: str, numero: str, depto: str, comuna: str, ciudad: str, region: str, rut_estudiante: str):
    estudiante = Estudiante.objects.get(rut = rut_estudiante)
    direccion = Direccion(calle=calle, numero=numero, depto=depto, comuna=comuna, ciudad=ciudad, region=region, estudiante=estudiante)
    direccion.save()
    return direccion

def obtiene_estudiante(obtiene_estudiante: str):
    return Estudiante.objects.get(rut = obtiene_estudiante)

def obtiene_profesor(obtiene_profesor: str):
    return Profesor.objects.get(rut = obtiene_profesor)

def obtiene_curso(obtiene_curso: str):
    return Curso.objects.get(codigo = obtiene_curso)

def agregar_profesor_a_curso(agregar_profesor: str, agregar_curso: str):
    curso = Curso.objects.get(codigo = agregar_curso)
    profesor = Profesor.objects.get(rut = agregar_profesor)
    curso.profesores.add(profesor)
    return profesor

def agregar_cursos_a_estudiante(agregar_curso: str, agregar_estudiante: str):
    estudiante = Estudiante.objects.get(rut = agregar_estudiante)
    curso = Curso.objects.get(codigo = agregar_curso)
    estudiante.cursos.add(curso)
    return curso    

def imprime_estudiante_cursos():
    datos_estudiantes = Estudiante.objects.all()
    for estudiante in datos_estudiantes:
        print(f'Estudiante {estudiante.nombre} {estudiante.apellido}, rut: {estudiante.rut}, fecha de nacimiento {estudiante.fecha_nac}, {"activo" if estudiante.activo == True else "no activo"}, creado el {estudiante.creacion_registro}.')
        if estudiante.cursos.count() == 0:
            print('____No tiene cursos asignados.')
        else:
            cursos_asignados = estudiante.cursos.all()
            print(f'____Tiene los siguientes cursos asignados: ')
            for curso_asignado in cursos_asignados:
                print(f'______{curso_asignado.nombre}, Version {curso_asignado.version}.')
                if curso_asignado.profesores.count() == 0:
                    print('______El curso no tiene profesor asignado.')
                else:
                    profesor_asignado = curso_asignado.profesores.all()[0]
                    print(f'______El profesor del curso es: {profesor_asignado.nombre} {profesor_asignado.apellido}.') 
                  