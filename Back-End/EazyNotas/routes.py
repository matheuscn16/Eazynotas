import json
from flask import Flask, request
from controllers import usuario
from controllers import aluno
from controllers import professor
from controllers import materias
from controllers import turmas
from controllers import notas
from controllers import frequencia
app = Flask(__name__)

@app.route('/')
def index():
    return "EazyNotas"

@app.route('/aluno',methods = ['POST'])
def createAluno():
    data = request.json
    idUsuario = data['rA']
    nome = data['nome']
    idTipo = data['idTipo']
    idTurma = data['idTurma']
    user = aluno.createAluno(idUsuario, nome, idTipo, idTurma)
    print()
    return 'sucesso'

@app.route('/alunos')
def getAllAlunos():
    als = aluno.getAllAlunos()
    return als

@app.route('/aluno/<rA>')
def getAluno(rA):
    alu = aluno.getAluno(rA)
    return alu

@app.route('/professor',methods = ['POST'])
def createProf():
    data = request.json
    nome = data['nome']
    idTipo = data['idTipo']
    user = professor.createProf(nome, idTipo)
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
    user = materias.createMaterias(nomeMat, idProfessor)
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
    idAluno = data['rA']
    idMateria = data['idMateria']
    valorNota = data['valorNota']
    user = notas.createNota(rA, idMateria, valorNota)
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
    idAluno = data['rA']
    idMateria = data['idMateria']
    NumFreq = data['NumFreq']
    user = frequencia.createFrequencia(rA, idMateria, NumFreq)
    print()
    return 'sucesso'

@app.route('/frequencia')
def getAllFrequencia():
    frequ = frequencia.getAllFrequencia()
    return frequ

@app.route('/frequencia/<idAluno>')
def getFrequencia(rA):
    t_freq = frequencia.getFrequencia(rA)
    return t_freq

if __name__ == '__main__':
    app.run(debug=True, port=8080)

