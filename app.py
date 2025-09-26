from flask import Flask, jsonify
from models import get_cliente_by_id

app = Flask(__name__)

@app.route('/clientes/<cliente_id>', methods=['GET'])
def get_cliente(cliente_id):
    cliente = get_cliente_by_id(cliente_id)
    if cliente:
        return jsonify(cliente)
    return jsonify({'error': 'Cliente no encontrado'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
