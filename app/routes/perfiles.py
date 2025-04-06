from flask import Blueprint, request, jsonify
from app.models.perfil import Perfil
from app.models.usuario import Usuario
from app.config.database import db

perfiles_bp = Blueprint('perfiles', __name__)

# Crear perfil
@perfiles_bp.route('/perfiles', methods=['POST'])
def crear_perfil():
    data = request.get_json()
    usuario_id = data.get('usuario_id')
    usuario = Usuario.query.get(usuario_id)

    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    if usuario.perfil:
        return jsonify({"error": "Este usuario ya tiene un perfil"}), 400

    nuevo_perfil = Perfil(
        usuario_id=usuario_id,
        rol=data.get('rol'),
        estado_registro_facial=data.get('estado_registro_facial', 'pendiente'),
        departamento=data.get('departamento')
    )
    db.session.add(nuevo_perfil)
    db.session.commit()
    return jsonify(nuevo_perfil.to_dict()), 201

# Obtener todos los perfiles
@perfiles_bp.route('/perfiles', methods=['GET'])
def obtener_perfiles():
    perfiles = Perfil.query.all()
    return jsonify([p.to_dict() for p in perfiles])

# Obtener perfil por ID
@perfiles_bp.route('/perfiles/<int:id>', methods=['GET'])
def obtener_perfil(id):
    perfil = Perfil.query.get(id)
    if perfil:
        return jsonify(perfil.to_dict())
    return jsonify({"error": "Perfil no encontrado"}), 404

# Actualizar perfil
@perfiles_bp.route('/perfiles/<int:id>', methods=['PUT'])
def actualizar_perfil(id):
    perfil = Perfil.query.get(id)
    if not perfil:
        return jsonify({"error": "Perfil no encontrado"}), 404

    data = request.get_json()
    perfil.rol = data.get('rol', perfil.rol)
    perfil.estado_registro_facial = data.get('estado_registro_facial', perfil.estado_registro_facial)
    perfil.departamento = data.get('departamento', perfil.departamento)
    db.session.commit()
    return jsonify(perfil.to_dict())

# Eliminar perfil
@perfiles_bp.route('/perfiles/<int:id>', methods=['DELETE'])
def eliminar_perfil(id):
    perfil = Perfil.query.get(id)
    if not perfil:
        return jsonify({"error": "Perfil no encontrado"}), 404

    db.session.delete(perfil)
    db.session.commit()
    return jsonify({"message": "Perfil eliminado correctamente"})
