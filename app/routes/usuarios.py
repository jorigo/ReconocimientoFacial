from flask import Blueprint, request, jsonify
from app.models.usuario import db, Usuario

usuarios_bp = Blueprint('usuarios', __name__)

# Crear usuario
@usuarios_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    nuevo_usuario = Usuario(
        nombre=data['nombre'], 
        email=data['email'], 
        telefono=data.get('telefono')
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({"message": "Usuario creado exitosamente"}), 201

# Obtener todos los usuarios
@usuarios_bp.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([u.to_dict() for u in usuarios])

# Obtener un usuario por ID
@usuarios_bp.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        return jsonify(usuario.to_dict())
    return jsonify({"message": "Usuario no encontrado"}), 404

# Actualizar usuario
@usuarios_bp.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        data = request.get_json()
        usuario.nombre = data.get('nombre', usuario.nombre)
        usuario.email = data.get('email', usuario.email)
        usuario.telefono = data.get('telefono', usuario.telefono)
        db.session.commit()
        return jsonify({"message": "Usuario actualizado"})
    return jsonify({"message": "Usuario no encontrado"}), 404

# Eliminar usuario
@usuarios_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({"message": "Usuario eliminado"})
    return jsonify({"message": "Usuario no encontrado"}), 404
