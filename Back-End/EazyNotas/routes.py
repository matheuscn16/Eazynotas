import json
from flask import Flask, request
from flask_cors import CORS
from controllers import aluno
from controllers import professor
from controllers import materias
from controllers import turmas
from controllers import notas
from controllers import frequencia
from controllers import signin
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "EazyNotas"

@app.route('/aluno',methods = ['POST'])
def createAluno():
    data = request.json
    nome = data['nome']
    senhaAluno = data['senhaAluno']
    idTurma = data['turma']
    user = aluno.createAluno(nome, idTurma, senhaAluno)
    print()
    return 'sucesso'

@app.route('/aluno')
def getAllAlunos():
    als = aluno.getAllAlunos()
    return als

@app.route('/aluno/<rA>')
def getAluno(rA):
    alu = aluno.getAluno(rA)
    return alu

@app.route('/login',methods = ['POST'])
def login():
    data = request.json
    nome = data['login']
    senha = data['senha']
    return signin.login(nome,senha)

@app.route('/professor',methods = ['POST'])
def createProf():
    data = request.json
    nome = data['nome']
    senhaProfessor = data['senha']
    user = professor.createProf(nome, senhaProfessor)
    print()
    return 'sucesso'

@app.route('/professor')
def getAllProf():
    profs = professor.getAllProf()
    return profs

@app.route('/professor/<idProfessor>')
def getProf(idProfessor):
    profe = professor.getProf(idProfessor)
    return profe

@app.route('/materias',methods = ['POST'])
def createMaterias():
    data = request.json
    nomeMat = data['nomeMat']
    idProfessor = data['idProfessor']
    diaMateria = data['diaMateria']
    horarioAula = data['horarioAula']
    user = materias.createMaterias(nomeMat, idProfessor, diaMateria, horarioAula)
    print()
    return 'sucesso'

@app.route('/materias')
def getAllMaterias():
    mats = materias.getAllMaterias()
    return mats

@app.route('/materias/<idMateria>')
def getMaterias(idMateria):
    mate = materias.getMaterias(idMateria)
    return mate

@app.route('/turmas',methods = ['POST'])
def createTurma():
    data = request.json
    sala = data['sala']
    idProfessor = data['idProfessor']
    user = turmas.createTurma(sala, idProfessor)
    print()
    return 'sucesso'

@app.route('/turmas')
def getAllTurma():
    turm = turmas.getAllTurma()
    return turm

@app.route('/turmas/<idTurma>')
def getTurma(idTurma):
    tur = turmas.getTurma(idTurma)
    return tur

@app.route('/notas',methods = ['POST'])
def createNota():
    data = request.json
    rA = data['rA']
    idMateria = data['idMateria']
    notaP1 = data['notaP1']
    notaP2 = data['notaP2']
    notaRC = data['notaRC']
    user = notas.createNota(rA, idMateria, notaP1, notaP2, notaRC)
    print()
    return 'sucesso'

@app.route('/notas')
def getAllNota():
    nots = notas.getAllNota()
    return nots

@app.route('/notas/<rA>')
def getNota(rA):
    v_nota = notas.getNota(rA)
    return v_nota

@app.route('/frequencia',methods = ['POST'])
def createFrequencia():
    data = request.json
    rA = data['rA']
    idMateria = data['idMateria']
    pAluno = data['pAluno']
    fAluno = data['fAluno']
    freqAluno = data['freqAluno']
    user = frequencia.createFrequencia(rA, idMateria, NumFreq)
    print()
    return 'sucesso'

@app.route('/frequencia')
def getAllFrequencia():
    frequ = frequencia.getAllFrequencia()
    return frequ

@app.route('/frequencia/<rA>')
def getFrequencia(rA):
    t_freq = frequencia.getFrequencia(rA)
    return t_freq

if __name__ == '__main__':
    app.run(debug=True, port=3000)

