# api.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

# Conexão com o banco
db = pymysql.connect(
    host='ns1172.hostgator.com.br',
    user='cicer580_usuario_escola',
    password='kh2c4l1T4L',
    database='cicer580_escola',
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/dados', methods=['POST'])
def inserir_dados():
    data = request.json
    semana = data.get('semana')
    matricula = data.get('matricula')
    disciplina = data.get('disciplina')
    horario = data.get('horario')

    with db.cursor() as cursor:
        sql = "INSERT INTO grade_horarios (semana, matricula, disciplina, horario) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (semana, matricula, disciplina, horario))
    db.commit()

    return jsonify({'mensagem': 'Dados inseridos com sucesso!'}), 201

@app.route('/dados', methods=['GET'])
def listar_dados():
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM grade_horarios")
        dados = cursor.fetchall()
    return jsonify(dados), 200

    