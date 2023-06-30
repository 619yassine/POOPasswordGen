from flask import Flask, redirect, render_template, request, url_for
from options.optionDate import OptionDate
from options.optionWord import OptionWord
from options.optionpersonal import PersonalInfo
from generator.passwordGenerator import PasswordGenerator
from generator.getPossibilities import Checker

app = Flask(__name__)

@app.route("/",  methods=["GET","POST"])
def home():
    return redirect(url_for('new_password'))

@app.route("/passwordgen", methods=["GET","POST"])
def new_password():
    return render_template("index.html")

@app.route('/render', methods=['GET'])
def resultat():
    date = request.args.get('date').split()
    mots = request.args.get('mot').split()

    allMin = request.args.get('min')
    allMaj = request.args.get('maj')
    capital = request.args.get('fMaj')
    noAccent = request.args.get('accent')
    leet = request.args.get('leet')

    useDate = request.args.get('datenbr')
    monthToWord = request.args.get('monthword')
    yearTwoChar = request.args.get('yeartwo')
    yearFourChar = request.args.get('yearfour')
    frenchMonth = request.args.get('frdate')

    optionWord = OptionWord(allMin,allMaj,capital,noAccent,leet)
    optionDate = OptionDate(useDate,monthToWord,yearTwoChar,yearFourChar,frenchMonth)
    personalInfo = PersonalInfo(mots,date)
    
    checker = Checker( personalInfo, optionWord, optionDate)
    passwordGenerator=PasswordGenerator(checker)

    return render_template("render.html", data=passwordGenerator.all_combinations)