import requests
import time
import os
import argparse

# Allow overriding the base URL via CLI arg or TEST_BASE env var
def get_base():
    parser = argparse.ArgumentParser(description='Demo API tester')
    parser.add_argument('--base', help='Base URL for the API (e.g. http://127.0.0.1:5000)')
    args = parser.parse_args()
    return args.base or os.getenv('TEST_BASE') or 'http://127.0.0.1:5000'

BASE = get_base()

def wait_for_server(timeout=10):
    start = time.time()
    while True:
        try:
            r = requests.get(BASE + '/')
            if r.status_code == 200:
                print('Servidor arriba')
                return True
        except Exception:
            pass
        if time.time() - start > timeout:
            print('Timeout esperando al servidor')
            return False
        time.sleep(0.5)

def post(path, json):
    r = requests.post(BASE + path, json=json)
    print('POST', path, r.status_code, r.text)
    return r

def get(path):
    r = requests.get(BASE + path)
    print('GET', path, r.status_code, r.text)
    return r

def main():
    if not wait_for_server():
        return

    # 1) Crear usuario docente y estudiante
    post('/usuarios', {'nombre':'Docente1','correo':'doc1@x.com','contrasena':'pwd','tipo':'docente'})
    post('/usuarios', {'nombre':'Estudiante1','correo':'est1@x.com','contrasena':'pwd','tipo':'estudiante'})

    # 2) Crear materia
    post('/materias', {'nombre':'Matematicas'})

    # 3) Crear curso usando materia_id=1 y docente_id=1
    post('/cursos', {'materia_id':1,'docente_id':1})

    # 4) Inscribir estudiante id=2 en curso id=1
    r = post('/cursos/1/estudiantes', {'estudiante_id':2})

    # 5) Registrar nota baja para que genere notificación
    post('/notas', {'estudiante_id':2,'curso_id':1,'valor':2.5})

    # 6) Consultar notificaciones
    get('/notificaciones')

    # 7) Listar usuarios y cursos
    get('/usuarios')
    get('/cursos')

if __name__ == '__main__':
    main()
