from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# In-memory stores
usuarios = {}
materias = {}
cursos = {}
notas = {}
notificaciones = {}
actividades = {}

def next_id(store):
	return max(store.keys()) + 1 if store else 1

@app.route('/')
def index():
	return jsonify({"message": "API Académica - endpoints: usuarios, materias, cursos, notas, notificaciones, actividades"})

# Usuarios
@app.route('/usuarios', methods=['GET'])
def list_usuarios():
	return jsonify(list(usuarios.values()))

@app.route('/usuarios', methods=['POST'])
def create_usuario():
	data = request.get_json() or {}
	required = ['nombre', 'correo', 'contrasena']
	if not all(k in data for k in required):
		return jsonify({'error':'Faltan campos requeridos'}), 400
	uid = next_id(usuarios)
	usuario = {
		'id': uid,
		'nombre': data['nombre'],
		'correo': data['correo'],
		'contrasena': data['contrasena'],
		'tipo': data.get('tipo','usuario')
	}
	usuarios[uid] = usuario
	return jsonify(usuario), 201

@app.route('/usuarios/<int:uid>', methods=['GET'])
def get_usuario(uid):
	u = usuarios.get(uid)
	if not u:
		abort(404)
	return jsonify(u)

@app.route('/usuarios/<int:uid>', methods=['PUT'])
def update_usuario(uid):
	u = usuarios.get(uid)
	if not u:
		abort(404)
	data = request.get_json() or {}
	u['nombre'] = data.get('nombre', u['nombre'])
	u['correo'] = data.get('correo', u['correo'])
	if 'contrasena' in data:
		u['contrasena'] = data['contrasena']
	return jsonify(u)

@app.route('/usuarios/<int:uid>', methods=['DELETE'])
def delete_usuario(uid):
	if uid in usuarios:
		del usuarios[uid]
		return '', 204
	abort(404)

# Materias
@app.route('/materias', methods=['GET','POST'])
def materias_handler():
	if request.method == 'GET':
		return jsonify(list(materias.values()))
	data = request.get_json() or {}
	if 'nombre' not in data:
		return jsonify({'error':'Falta nombre'}), 400
	mid = next_id(materias)
	materia = {'id': mid, 'nombre': data['nombre']}
	materias[mid] = materia
	return jsonify(materia), 201

@app.route('/materias/<int:mid>', methods=['GET','PUT','DELETE'])
def materia_detail(mid):
	m = materias.get(mid)
	if not m:
		abort(404)
	if request.method == 'GET':
		return jsonify(m)
	if request.method == 'PUT':
		data = request.get_json() or {}
		m['nombre'] = data.get('nombre', m['nombre'])
		return jsonify(m)
	del materias[mid]
	return '', 204

# Cursos
@app.route('/cursos', methods=['GET','POST'])
def cursos_handler():
	if request.method == 'GET':
		return jsonify(list(cursos.values()))
	data = request.get_json() or {}
	required = ['materia_id', 'docente_id']
	if not all(k in data for k in required):
		return jsonify({'error':'Faltan campos materia_id/docente_id'}), 400
	cid = next_id(cursos)
	curso = {'id': cid, 'materia_id': data['materia_id'], 'docente_id': data['docente_id'], 'estudiantes': [], 'notas': []}
	cursos[cid] = curso
	return jsonify(curso), 201

@app.route('/cursos/<int:cid>', methods=['GET','PUT','DELETE'])
def curso_detail(cid):
	c = cursos.get(cid)
	if not c:
		abort(404)
	if request.method == 'GET':
		return jsonify(c)
	if request.method == 'PUT':
		data = request.get_json() or {}
		c['materia_id'] = data.get('materia_id', c['materia_id'])
		c['docente_id'] = data.get('docente_id', c['docente_id'])
		return jsonify(c)
	del cursos[cid]
	return '', 204

@app.route('/cursos/<int:cid>/estudiantes', methods=['POST'])
def inscribir_estudiante(cid):
	c = cursos.get(cid)
	if not c:
		abort(404)
	data = request.get_json() or {}
	if 'estudiante_id' not in data:
		return jsonify({'error':'Falta estudiante_id'}), 400
	eid = data['estudiante_id']
	if eid not in usuarios:
		return jsonify({'error':'Estudiante no existe'}), 404
	if eid in c['estudiantes']:
		return jsonify({'error':'Ya inscrito'}), 400
	c['estudiantes'].append(eid)
	return jsonify(c)

# Notas
@app.route('/notas', methods=['GET','POST'])
def notas_handler():
	if request.method == 'GET':
		return jsonify(list(notas.values()))
	data = request.get_json() or {}
	required = ['estudiante_id','curso_id','valor']
	if not all(k in data for k in required):
		return jsonify({'error':'Faltan campos requeridos'}), 400
	nid = next_id(notas)
	nota = {'id': nid, 'estudiante_id': data['estudiante_id'], 'curso_id': data['curso_id'], 'valor': data['valor']}
	notas[nid] = nota
	# attach to curso if exists
	c = cursos.get(nota['curso_id'])
	if c is not None:
		c['notas'].append(nid)
	# generate notification if valor < 3.0
	if nota['valor'] < 3.0:
		mid = next_id(notificaciones)
		mensaje = f"[Alerta] Nota baja en curso {nota['curso_id']}: {nota['valor']}"
		noti = {'id': mid, 'mensaje': mensaje, 'estudiante_id': nota['estudiante_id'], 'leida': False}
		notificaciones[mid] = noti
	return jsonify(nota), 201

@app.route('/notas/<int:nid>', methods=['GET','PUT','DELETE'])
def nota_detail(nid):
	n = notas.get(nid)
	if not n:
		abort(404)
	if request.method == 'GET':
		return jsonify(n)
	if request.method == 'PUT':
		data = request.get_json() or {}
		n['valor'] = data.get('valor', n['valor'])
		return jsonify(n)
	# DELETE
	del notas[nid]
	return '', 204

# Notificaciones
@app.route('/notificaciones', methods=['GET','POST'])
def notificaciones_handler():
	if request.method == 'GET':
		return jsonify(list(notificaciones.values()))
	data = request.get_json() or {}
	required = ['mensaje','estudiante_id']
	if not all(k in data for k in required):
		return jsonify({'error':'Faltan campos requeridos'}), 400
	nid = next_id(notificaciones)
	noti = {'id': nid, 'mensaje': data['mensaje'], 'estudiante_id': data['estudiante_id'], 'leida': False}
	notificaciones[nid] = noti
	return jsonify(noti), 201

@app.route('/notificaciones/<int:nid>', methods=['GET','PUT','DELETE'])
def noti_detail(nid):
	n = notificaciones.get(nid)
	if not n:
		abort(404)
	if request.method == 'GET':
		return jsonify(n)
	if request.method == 'PUT':
		data = request.get_json() or {}
		n['leida'] = bool(data.get('leida', n['leida']))
		return jsonify(n)
	del notificaciones[nid]
	return '', 204

# Actividades / Calendario
@app.route('/actividades', methods=['GET','POST'])
def actividades_handler():
	if request.method == 'GET':
		return jsonify(list(actividades.values()))
	data = request.get_json() or {}
	required = ['nombre','fecha','descripcion']
	if not all(k in data for k in required):
		return jsonify({'error':'Faltan campos requeridos'}), 400
	aid = next_id(actividades)
	act = {'id': aid, 'nombre': data['nombre'], 'fecha': data['fecha'], 'descripcion': data['descripcion']}
	actividades[aid] = act
	return jsonify(act), 201

@app.route('/actividades/<int:aid>', methods=['GET','PUT','DELETE'])
def actividad_detail(aid):
	a = actividades.get(aid)
	if not a:
		abort(404)
	if request.method == 'GET':
		return jsonify(a)
	if request.method == 'PUT':
		data = request.get_json() or {}
		a['nombre'] = data.get('nombre', a['nombre'])
		a['fecha'] = data.get('fecha', a['fecha'])
		a['descripcion'] = data.get('descripcion', a['descripcion'])
		return jsonify(a)
	del actividades[aid]
	return '', 204


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)

