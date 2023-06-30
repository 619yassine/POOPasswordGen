from optionDate import OptionDate
from optionWord import OptionWord
from optionpersonal import PersonalInfo
from textMethods import WorkOnStrings
from datesMethods import WorkOnDates

class Checker:

    def __init__(self, personalInfo:PersonalInfo, optionWord:OptionWord, optionDate:OptionDate):
        self.personalInfo = personalInfo
        self.optionWord = optionWord
        self.optionDate = optionDate

    def getPossibleStrings(self):
        result = []
        for word in self.personalInfo.stringData:
            options = []

            if self.optionWord.noAccent :
                options.append(WorkOnStrings.removeAccents( word ))

            if self.optionWord.allMin :
                options.append( word.lower())

            if self.optionWord.allMaj :
                options.append( word.upper())
                
            if self.optionWord.capital:
                options.append( word.capitalize()) 

            if self.optionWord.leet :
                options.extend(WorkOnStrings.leetOptions( self, word ))
            
            result.append(options)
        return result

    def getPossibleDates(self):
        result=[]
        dates = WorkOnDates()
        for date in self.personalInfo.dateData:
            options=[]
            year, month, day = date.split("-")

            options.append(dates.convertDay(int(day)))
            options.append(dates.convertMonth(int(month)))
            options.append(dates.convertYear(int(year)))

            result.append(options)
        return result

    def stringOptions(self, word: str):
        return [word.upper(),word.lower(), word.capitalize()]
    