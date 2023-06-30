import unicodedata

class textMethods:
    
    @staticmethod
    def removeAccents( word: str):
        result = unicodedata.normalize('NFKD', word).encode('ASCII', 'ignore').decode()
        return result
    
    @classmethod
    def leetOptions(self, word: str):
        result=[]
        stringOptionResult=[]
        result.append(word)
        index=0
        while index < len(result):
            for character in result[index]:
                match character.lower():
                    case "a":
                        result.append(result[index].replace("A","4",1))
                        result.append(result[index].replace("a","4",1))
                    case "e":
                        result.append(result[index].replace("E","3",1))
                        result.append(result[index].replace("e","3",1))
                    case "i":
                        result.append(result[index].replace("I","1",1))
                        result.append(result[index].replace("i","1",1))
                    case "o":
                        result.append(result[index].replace("O","0",1))
                        result.append(result[index].replace("o","0",1))
                    case "l":
                        result.append(result[index].replace("L","1",1))
                        result.append(result[index].replace("l","1",1))
                    case "s":
                        result.append(result[index].replace("S","5",1))
                        result.append(result[index].replace("s","5",1))
                    case "b":
                        result.append(result[index].replace("B","8",1))
                        result.append(result[index].replace("b","8",1))
                    case "t":
                        result.append(result[index].replace("T","7",1))
                        result.append(result[index].replace("t","7",1))
                    case "z":
                        result.append(result[index].replace("Z","2",1))
                        result.append(result[index].replace("z","2",1))
                    case "g":
                        result.append(result[index].replace("G","6",1))
                        result.append(result[index].replace("g","6",1))  
            result = list(dict.fromkeys(result))
            index +=1
        for option in result:
            stringOptionResult.extend(self.stringOptions(option))
            
        return stringOptionResult
    
    def stringOptions(self, word: str):
        return [word.upper(),word.lower(), word.capitalize()]
    
    def printMessage(self):
        print(textMethods.message)
