from textMethods import WorkOnStrings

class WorkOnDates:
    
    def convertDay(self, day):
        return [*set([str(day),"0" + str(day)])] if day<10 else [*set([str(day),str(day)])]
    
    def convertMonth( self, month):
        result=[]
        result.extend([*set([str(month),str(month).lstrip("0")])])
        result.extend(self.monthToLetter(str(month)))
        return result
    
    def convertYear(self, year):
        return [*set([str(year),str(year % 100)])]
    
    def monthToLetter(self, month):
        result =''
        workOnStrings =WorkOnStrings()
        match month:
            case "01":
                result= "janvier"
            case "02":
                result ="fevrier"
            case "03":
                result= "mars"
            case "04":
                result ="avril"
            case "05":
                result= "mai"
            case "06":
                result ="juin"
            case "07":
                result= "juillet"
            case "08":
                result ="aout"
            case "09":
                result= "septembre"
            case "10":
                result ="octobre"
            case "11":
                result= "novembre"
            case "12":
                result ="decembre"
        return workOnStrings.stringOptions(result)