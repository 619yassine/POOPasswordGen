import itertools
from getPossibilities import Checker

class PasswordGenerator:
    def __init__(self, checker:Checker):
        self.checker = checker
        self.optionMatrix = []
        self.all_combinations = [] 
        self.__createOptionMatrix()
        self.__findAllCombinations()

    def __createOptionMatrix(self):
        self.optionMatrix.extend(self.checker.getPossibleStrings())
        for optionList in self.checker.getPossibleDates():
            self.optionMatrix.extend(optionList)

    def __pwdOptions(self):
        passwordOptions = []
        for length in range(max(6,len(self.optionMatrix)+1)):
            passwordOptions.extend(itertools.combinations(self.optionMatrix, length))
        return passwordOptions

    def __getResults(self, passwordOptions):
        results=[]
        for combination in passwordOptions:
            results.extend(itertools.product(*combination))
        return results

    def __combineResults(self, results):
        for tuple in results:
            combinations =[]
            combinations=itertools.permutations(tuple,len(tuple))
            for option in combinations:
                password = ""
                for element in option:
                    password += element
                self.all_combinations.append(password)

    def __findAllCombinations(self): 
        passwordOptions = self.__pwdOptions()
        results=self.__getResults(passwordOptions)
        self.__combineResults(results)

