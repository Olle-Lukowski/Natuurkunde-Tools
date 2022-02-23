import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Natuurkunde Tools!")

main_frm = ttk.Frame(window, padding=10)
main_frm.grid()

formula_frm = ttk.Frame(window, padding=10)
formula_frm.grid()

answer_text = ttk.Label(formula_frm)

unit_list = ["W (arbeid in Joule)", "F (kracht in Newton)", "s (afstand in Meter)", "Vgem (gemiddelde snelheid in Meter per Seconde)", "t (tijd in Seconden)", "stoot (stoot in Newton Seconde)", "m (de massa in kilogram)", "Wz (arbeid om iets omhoog te tillen in Joule)", "g (9,81 newton per kilogram)", "h (de verplaatsing omhoog in meter)"]

def checkInputType(*args):
    print(f"Unit args: {args}")
    EpicDictCounter = int(0)
    global EpicDict
    EpicDict = {"W": None, "F": None, "s": None, "Vgem": None, "t": None, "stoot": None, "m": None, "Wz": None, "g": None, "h": None}
    type_list = []
    for unit in args:
        if unit == "W (arbeid in Joule)":
            type_list.append("W")
            EpicDict["W"] = EpicDictCounter
        elif unit == "F (kracht in Newton)":
            type_list.append("F")
            EpicDict["F"] = EpicDictCounter
        elif unit == "s (afstand in Meter)":
            type_list.append("s")
            EpicDict["s"] = EpicDictCounter
        elif unit == "Vgem (gemiddelde snelheid in Meter per Seconde)":
            type_list.append("Vgem")
            EpicDict["Vgem"] = EpicDictCounter
        elif unit == "t (tijd in Seconden)":
            type_list.append("t")
            EpicDict["t"] = EpicDictCounter
        elif unit == "stoot (stoot in Newton Seconde)":
            type_list.append("stoot")
            EpicDict["stoot"] = EpicDictCounter
        elif unit == "m (de massa in kilogram)":
            type_list.append("m")
            EpicDict["m"] = EpicDictCounter
        elif unit == "Wz (arbeid om iets omhoog te tillen in Joule)":
            type_list.append("Wz")
            EpicDict["Wz"] = EpicDictCounter
        elif unit == "g (9,81 newton per kilogram)":
            type_list.append("g")
            EpicDict["g"] = EpicDictCounter
        elif unit == "h (de verplaatsing omhoog in meter)":
            type_list.append("h")
            EpicDict["h"] = EpicDictCounter
        else:
            pass
        EpicDictCounter += 1
    return type_list


def checkForEmptyInput(*args):
    print(f"Input args: {args}")
    value_list = []
    for value in args:
        if value != "":
            value_list.append(value)
    return value_list


def findAndFormFormula(type_list):
    print(f"Type list: {type_list}")
    formula_list = ["W=F*s", "stoot=F*t", "Vgem=s/t", "F*t=m*Vgem", "stoot=m*Vgem", "Wz=m*g*h"]
    used_formula = ""
    if len(type_list) == 2:
        for unit in type_list:
            if unit == "W":
                try:
                    formula_list.remove("stoot=F*t")
                    formula_list.remove("Vgem=s/t")
                    formula_list.remove("F*t=m*Vgem")
                    formula_list.remove("stoot=m*Vgem")
                    formula_list.remove("Wz=m*g*h")
                except:
                    print("USER IS DUMB!")
            if unit == "stoot":
                try:
                    formula_list.remove("W=F*s")
                    formula_list.remove("Vgem=s/t")
                    formula_list.remove("F*t=m*Vgem")
                    formula_list.remove("Wz=m*g*h")
                    if type_list[0] == "Vgem" or type_list[1] == "Vgem":
                        formula_list.remove("stoot=F*t")
                except:
                    print("USER IS DUMB!")
            if unit == "Vgem":
                try:
                    formula_list.remove("W=F*s")
                    formula_list.remove("stoot=F*t")
                    formula_list.remove("F*t=m*Vgem")
                    formula_list.remove("Wz=m*g*h")
                except:
                    print("USER IS DUMB!")

            if unit == "F":
                try:
                    formula_list.remove("Vgem=s/t")
                    formula_list.remove("stoot=m*Vgem")
                    formula_list.remove("F*t=m*Vgem")
                    formula_list.remove("Wz=m*g*h")
                except:
                    print("USER IS DUMB!")
            if unit == "s":
                try:
                    formula_list.remove("stoot=F*t")
                    formula_list.remove("F*t=m*Vgem")
                    formula_list.remove("stoot=m*Vgem")
                    formula_list.remove("Wz=m*g*h")
                except:
                    print("USER IS DUMB!")

            if unit == "t":
                try:
                    formula_list.remove("W=F*s")
                    formula_list.remove("F*t=m*Vgem")
                    formula_list.remove("stoot=m*Vgem")
                    formula_list.remove("Wz=m*g*h")
                except:
                    print("USER IS DUMB!")

        used_formula = formula_list[0]
        print(f"Used Formula: {used_formula}")
        if used_formula == "W=F*s":
            if EpicDict["W"] == None:
                return "W=F*s"

            elif EpicDict["s"] == None:
                return "s=W/F"

            elif EpicDict["F"] == None:
                return "F=W/s"

        if used_formula == "stoot=F*t":
            if EpicDict["stoot"] == None:
                return "stoot=F*t"

            elif EpicDict["t"] == None:
                return "t=stoot/F"

            elif EpicDict["F"] == None:
                return "F=stoot/t"

        if used_formula == "Vgem=s/t":
            if EpicDict["Vgem"] == None:
                return "Vgem=s/t"

            elif EpicDict["t"] == None:
                return "t=s/Vgem"

            elif EpicDict["s"] == None:
                return "s=Vgem*t"

        if used_formula == "stoot=m*Vgem":
            if EpicDict["stoot"] == None:
                return "stoot=m*Vgem"

            elif EpicDict["Vgem"] == None:
                return "Vgem=stoot/m"

            elif EpicDict["m"] == None:
                return "m=stoot/Vgem"

    elif len(type_list) == 3:
        for unit in type_list:
            if unit == "m":
                try:
                    formula_list.remove("stoot=F*t")
                    formula_list.remove("Vgem=s/t")
                    formula_list.remove("W=F*s")
                    formula_list.remove("stoot=m*Vgem")
                    if EpicDict["F"] != None:
                        formula_list.remove("Wz=m*g*h")
                except:
                    print("EpicDict!")
            if unit == "Wz":
                try:
                    formula_list.remove("stoot=F*t")
                    formula_list.remove("Vgem=s/t")
                    formula_list.remove("W=F*s")
                    formula_list.remove("stoot=m*Vgem")
                    formula_list.remove("F*t=m*Vgem")
                except:
                    print("EpicDict!")
            if unit == "g":
                try:
                    formula_list.remove("stoot=F*t")
                    formula_list.remove("Vgem=s/t")
                    formula_list.remove("W=F*s")
                    formula_list.remove("stoot=m*Vgem")
                    formula_list.remove("F*t=m*Vgem")
                except:
                    print("EpicDict!")
            if unit == "h":
                try:
                    formula_list.remove("stoot=F*t")
                    formula_list.remove("Vgem=s/t")
                    formula_list.remove("W=F*s")
                    formula_list.remove("stoot=m*Vgem")
                    formula_list.remove("F*t=m*Vgem")
                except:
                    print("EpicDict!")
            if unit == "F":
                try:
                    formula_list.remove("stoot=F*t")
                    formula_list.remove("Vgem=s/t")
                    formula_list.remove("W=F*s")
                    formula_list.remove("stoot=m*Vgem")
                    formula_list.remove("Wz=m*g*h")
                    
                except:
                    print("EpicDict!")
            if unit == "t":
                try:
                    formula_list.remove("stoot=F*t")
                    formula_list.remove("Vgem=s/t")
                    formula_list.remove("W=F*s")
                    formula_list.remove("stoot=m*Vgem")
                    formula_list.remove("Wz=m*g*h")
                except:
                    print("EpicDict!")
            if unit == "Vgem":
                try:
                    formula_list.remove("stoot=F*t")
                    formula_list.remove("Vgem=s/t")
                    formula_list.remove("W=F*s")
                    formula_list.remove("stoot=m*Vgem")
                    formula_list.remove("Wz=m*g*h")
                except:
                    print("EpicDict!")
        
        used_formula = formula_list[0]
        print(f"Used Formula: {used_formula}")
        if used_formula == "F*t=m*Vgem":
            if EpicDict["Vgem"] == None:
                return "Vgem=(F*t)/m"

            elif EpicDict["F"] == None:
                return "F=(m*Vgem)/t"

            elif EpicDict["t"] == None:
                return "t=(m*Vgem)/F"

            elif EpicDict["m"] == None:
                return "m=(F*t)/Vgem"

        if used_formula == "Wz=m*g*h":
            if EpicDict["Wz"] == None:
                return "Wz=m*g*h"

            elif EpicDict["m"] == None:
                return "m=Wz/(g*h)"

            elif EpicDict["g"] == None:
                return "g=Wz/(m*h)"

            elif EpicDict["h"] == None:
                return "h=Wz/(m*g)"


def runCalculation(formula, value_list):
    print(f"Formula: {formula}")
    print(f"Value list: {value_list}")

    print(EpicDict)
    EpicDictCounter = int(0)
    EpicDictCounterList = ["W", "F", "s", "Vgem", "t", "stoot", "m", "Wz", "g", "h"]
    EpicDictDictCounter = int(0)
    
    while True:
        try:
            print(EpicDict[EpicDictCounterList[EpicDictCounter]])
            if EpicDict[EpicDictCounterList[EpicDictCounter]] == 0:
                EpicDict[EpicDictCounterList[EpicDictCounter]] = value_list[0]
            elif EpicDict[EpicDictCounterList[EpicDictCounter]] == 1:
                EpicDict[EpicDictCounterList[EpicDictCounter]] = value_list[1]
            elif EpicDict[EpicDictCounterList[EpicDictCounter]] == 2:
                EpicDict[EpicDictCounterList[EpicDictCounter]] = value_list[2]
            EpicDictCounter += 1
        except:
            break
        

    print(EpicDict)

    if formula == "W=F*s":
        answer_calculation = ttk.Label(formula_frm, text="W = F x s = " + f"{EpicDict['F']} x {EpicDict['s']} = " + str(float(EpicDict["F"]) * float(EpicDict["s"])))
        answer_calculation.grid(column=1, row=5)
        return str(float(EpicDict["F"])*float(EpicDict["s"])) + " Joule."

    elif formula == "s=W/F":
        answer_calculation = ttk.Label(formula_frm, text="s = W ÷ F = " + f"{EpicDict['W']} ÷ {EpicDict['F']} = " + str(float(EpicDict["W"]) / float(EpicDict["F"])))
        answer_calculation.grid(column=1, row=5)
        return str(float(EpicDict["W"])/float(EpicDict["F"])) + " Meter."
    
    elif formula == "F=W/s":
        answer_calculation = ttk.Label(formula_frm, text="F = W ÷ s = " + f"{EpicDict['W']} ÷ {EpicDict['s']} = " + str(float(EpicDict["W"]) / float(EpicDict["s"])))
        answer_calculation.grid(column=1, row=5)
        return str(float(EpicDict["W"])/float(EpicDict["s"])) + " Newton."
    

    elif formula == "stoot=F*t":
        answer_calculation = ttk.Label(formula_frm, text="stoot = F x t = " + f"{EpicDict['F']} x {EpicDict['t']} = " + str(float(EpicDict['F']) * float(EpicDict['t'])))
        answer_calculation.grid(column=1, row=5)
        return str(float(EpicDict["F"])*float(EpicDict["t"])) + " Newton Seconde."

    elif formula == "t=stoot/F":
        answer_calculation = ttk.Label(formula_frm, text="t = stoot ÷ F = " + f"{EpicDict['stoot']} ÷ {EpicDict['F']} = " + str(float(EpicDict['stoot']) / float(EpicDict['F'])))
        answer_calculation.grid(column=1, row=5)
        return str(float(EpicDict['stoot'])/float(EpicDict['F'])) + " Seconde."
    
    elif formula == "F=stoot/t":
        answer_calculation = ttk.Label(formula_frm, text="F = stoot ÷ t = " + f"{EpicDict['stoot']} ÷ {EpicDict['t']} = " + str(float(EpicDict['stoot']) / float(EpicDict['t'])))
        answer_calculation.grid(column=1, row=5)
        return str(float(EpicDict['stoot'])/float(EpicDict['t'])) + " Newton."

    elif formula == "Vgem=s/t":
        answer_calculation = ttk.Label(formula_frm, text="Vgem = s ÷ t = " + f"{EpicDict['s']} ÷ {EpicDict['t']} = " + str(float(value_list[0]) / float(value_list[1])))
        answer_calculation.grid(column=1, row=5)
        return str(float(EpicDict['s'])/float(EpicDict['t'])) + " Meter per Seconde."

    elif formula == "t=s/Vgem":
        answer_calculation = ttk.Label(formula_frm, text="t = s ÷ Vgem = " + f"{EpicDict['s']} ÷ {EpicDict['Vgem']} = " + str(float(value_list[1]) / float(value_list[0])))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[1])/float(value_list[0])) + " Seconde."

    elif formula == "s=1*2":
        answer_calculation = ttk.Label(formula_frm, text="s = Vgem x t = " + f"{value_list[0]} x {value_list[1]} = " + str(float(value_list[0]) * float(value_list[1])))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[0])*float(value_list[1])) + " Meter."
    elif formula == "s=2*1":
        answer_calculation = ttk.Label(formula_frm, text="s = Vgem x t = " + f"{value_list[1]} x {value_list[0]} = " + str(float(value_list[1]) * float(value_list[0])))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[1])*float(value_list[0])) + " Meter."

    elif formula == "stoot2=1*2":
        answer_calculation = ttk.Label(formula_frm, text="stoot = m x Vgem = " + f"{value_list[0]} x {value_list[1]} = " + str(float(value_list[0]) * float(value_list[1])))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[0])*float(value_list[1])) + " Newton Seconde."
    elif formula == "stoot2=2*1":
        answer_calculation = ttk.Label(formula_frm, text="stoot = m x Vgem = " + f"{value_list[1]} x {value_list[0]} = " + str(float(value_list[1]) * float(value_list[0])))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[1])*float(value_list[0])) + " Newton Seconde."
    elif formula == "Vgem2=1/2":
        answer_calculation = ttk.Label(formula_frm, text="Vgem = stoot ÷ m = " + f"{value_list[0]} ÷ {value_list[1]} = " + str(float(value_list[0]) / float(value_list[1])))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[0])/float(value_list[1])) + " Meter per Seconde."
    elif formula == "Vgem2=2/1":
        answer_calculation = ttk.Label(formula_frm, text="Vgem = stoot ÷ m = " + f"{value_list[1]} ÷ {value_list[0]} = " + str(float(value_list[1]) / float(value_list[0])))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[1])/float(value_list[0])) + " Meter per Seconde."
    elif formula == "m=1/2":
        answer_calculation = ttk.Label(formula_frm, text="m = stoot ÷ Vgem = " + f"{value_list[0]} ÷ {value_list[1]} = " + str(float(value_list[0]) / float(value_list[1])))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[0])/float(value_list[1])) + " kilogram."
    elif formula == "m=2/1":
        answer_calculation = ttk.Label(formula_frm, text="m = stoot ÷ Vgem = " + f"{value_list[1]} ÷ {value_list[0]} = " + str(float(value_list[1]) / float(value_list[0])))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[1])/float(value_list[0])) + " kilogram."



    elif formula == "Vgem=(0*1)/2":
        answer_calculation = ttk.Label(formula_frm, text="Vgem = F x t ÷ m = " + f"{value_list[0]} x {value_list[1]} ÷ {value_list[2]} = " + str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " Meter per Seconde."
    elif formula == "Vgem=(0*2)/1":
        answer_calculation = ttk.Label(formula_frm, text="Vgem = F x t ÷ m = " + f"{value_list[0]} x {value_list[2]} ÷ {value_list[1]} = " + str((float(value_list[0]) * float(value_list[2])) / float(value_list[1])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " Meter per Seconde."
    elif formula == "Vgem=(1*0)/2":
        answer_calculation = ttk.Label(formula_frm, text="Vgem = F x t ÷ m = " + f"{value_list[1]} x {value_list[0]} ÷ {value_list[2]} = " + str((float(value_list[1]) * float(value_list[0])) / float(value_list[2])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " Meter per Seconde."
    elif formula == "Vgem=(1*2)/0":
        answer_calculation = ttk.Label(formula_frm, text="Vgem = F x t ÷ m = " + f"{value_list[1]} x {value_list[2]} ÷ {value_list[0]} = " + str((float(value_list[1]) * float(value_list[2])) / float(value_list[0])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " Meter per Seconde."
    elif formula == "Vgem=(2*0)/1":
        answer_calculation = ttk.Label(formula_frm, text="Vgem = F x t ÷ m = " + f"{value_list[2]} x {value_list[0]} ÷ {value_list[1]} = " + str((float(value_list[2]) * float(value_list[0])) / float(value_list[1])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " Meter per Seconde."
    elif formula == "Vgem=(2*1)/0":
        answer_calculation = ttk.Label(formula_frm, text="Vgem = F x t ÷ m = " + f"{value_list[2]} x {value_list[1]} ÷ {value_list[0]} = " + str((float(value_list[2]) * float(value_list[1])) / float(value_list[0])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " Meter per Seconde."

    elif formula == "F=(0*1)/2":
        answer_calculation = ttk.Label(formula_frm, text="F = m x Vgem ÷ t = " + f"{value_list[0]} x {value_list[1]} ÷ {value_list[2]} = " + str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " Newton."
    elif formula == "F=(0*2)/1":
        answer_calculation = ttk.Label(formula_frm, text="F = m x Vgem ÷ t = " + f"{value_list[0]} x {value_list[2]} ÷ {value_list[1]} = " + str((float(value_list[0]) * float(value_list[2])) / float(value_list[1])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " Newton."
    elif formula == "F=(1*0)/2":
        answer_calculation = ttk.Label(formula_frm, text="F = m x Vgem ÷ t = " + f"{value_list[1]} x {value_list[0]} ÷ {value_list[2]} = " + str((float(value_list[1]) * float(value_list[0])) / float(value_list[2])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " Newton."
    elif formula == "F=(1*2)/0":
        answer_calculation = ttk.Label(formula_frm, text="F = m x Vgem ÷ t = " + f"{value_list[1]} x {value_list[2]} ÷ {value_list[0]} = " + str((float(value_list[1]) * float(value_list[2])) / float(value_list[0])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " Newton."
    elif formula == "F=(2*0)/1":
        answer_calculation = ttk.Label(formula_frm, text="F = m x Vgem ÷ t = " + f"{value_list[2]} x {value_list[0]} ÷ {value_list[1]} = " + str((float(value_list[2]) * float(value_list[0])) / float(value_list[1])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " Newton."
    elif formula == "F=(2*1)/0":
        answer_calculation = ttk.Label(formula_frm, text="F = m x Vgem ÷ t = " + f"{value_list[2]} x {value_list[1]} ÷ {value_list[0]} = " + str((float(value_list[2]) * float(value_list[1])) / float(value_list[0])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " Newton."

    elif formula == "t=(0*1)/2":
        answer_calculation = ttk.Label(formula_frm, text="t = m x Vgem ÷ F = " + f"{value_list[0]} x {value_list[1]} ÷ {value_list[2]} = " + str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " Seconde."
    elif formula == "t=(0*2)/1":
        answer_calculation = ttk.Label(formula_frm, text="t = m x Vgem ÷ F = " + f"{value_list[0]} x {value_list[2]} ÷ {value_list[1]} = " + str((float(value_list[0]) * float(value_list[2])) / float(value_list[1])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " Seconde."
    elif formula == "t=(1*0)/2":
        answer_calculation = ttk.Label(formula_frm, text="t = m x Vgem ÷ F = " + f"{value_list[1]} x {value_list[0]} ÷ {value_list[2]} = " + str((float(value_list[1]) * float(value_list[0])) / float(value_list[2])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " Seconde."
    elif formula == "t=(1*2)/0":
        answer_calculation = ttk.Label(formula_frm, text="t = m x Vgem ÷ F = " + f"{value_list[1]} x {value_list[2]} ÷ {value_list[0]} = " + str((float(value_list[1]) * float(value_list[2])) / float(value_list[0])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " Seconde."
    elif formula == "t=(2*0)/1":
        answer_calculation = ttk.Label(formula_frm, text="t = m x Vgem ÷ F = " + f"{value_list[2]} x {value_list[0]} ÷ {value_list[1]} = " + str((float(value_list[2]) * float(value_list[0])) / float(value_list[1])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " Seconde."
    elif formula == "t=(2*1)/0":
        answer_calculation = ttk.Label(formula_frm, text="t = m x Vgem ÷ F = " + f"{value_list[2]} x {value_list[1]} ÷ {value_list[0]} = " + str((float(value_list[2]) * float(value_list[1])) / float(value_list[0])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " Seconde."

    elif formula == "m=(0*1)/2":
        answer_calculation = ttk.Label(formula_frm, text="m = F x t ÷ Vgem = " + f"{value_list[0]} x {value_list[1]} ÷ {value_list[2]} = " + str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " kilogram."
    elif formula == "m=(0*2)/1":
        answer_calculation = ttk.Label(formula_frm, text="m = F x t ÷ Vgem = " + f"{value_list[0]} x {value_list[2]} ÷ {value_list[1]} = " + str((float(value_list[0]) * float(value_list[2])) / float(value_list[1])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " kilogram."
    elif formula == "m=(1*0)/2":
        answer_calculation = ttk.Label(formula_frm, text="m = F x t ÷ Vgem = " + f"{value_list[1]} x {value_list[0]} ÷ {value_list[2]} = " + str((float(value_list[1]) * float(value_list[0])) / float(value_list[2])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " kilogram."
    elif formula == "m=(1*2)/0":
        answer_calculation = ttk.Label(formula_frm, text="m = F x t ÷ Vgem = " + f"{value_list[1]} x {value_list[2]} ÷ {value_list[0]} = " + str((float(value_list[1]) * float(value_list[2])) / float(value_list[0])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " kilogram."
    elif formula == "m=(2*0)/1":
        answer_calculation = ttk.Label(formula_frm, text="m = F x t ÷ Vgem = " + f"{value_list[2]} x {value_list[0]} ÷ {value_list[1]} = " + str((float(value_list[2]) * float(value_list[0])) / float(value_list[1])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " kilogram."
    elif formula == "m=(2*1)/0":
        answer_calculation = ttk.Label(formula_frm, text="m = F x t ÷ Vgem = " + f"{value_list[2]} x {value_list[1]} ÷ {value_list[0]} = " + str((float(value_list[2]) * float(value_list[1])) / float(value_list[0])))
        answer_calculation.grid(column=1, row=5)
        return str((float(value_list[0]) * float(value_list[1])) / float(value_list[2])) + " kilogram."


    elif formula == "Wz=0*1*2":
        answer_calculation = ttk.Label(formula_frm, text="Wz = m x g x h = " + f"{value_list[0]} x {value_list[1]} x {value_list[2]} = " + str((float(value_list[0]) * float(value_list[1])) * float(value_list[2])))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[0]) * float(value_list[1]) * float(value_list[2])) + " Joule."
    elif formula == "Wz=0*2*1":
        answer_calculation = ttk.Label(formula_frm, text="Wz = m x g x h = " + f"{value_list[0]} x {value_list[2]} x {value_list[1]} = " + str((float(value_list[0]) * float(value_list[2])) * float(value_list[1])))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[0]) * float(value_list[2]) * float(value_list[1])) + " Joule."
    elif formula == "Wz=1*0*2":
        answer_calculation = ttk.Label(formula_frm, text="Wz = m x g x h = " + f"{value_list[1]} x {value_list[0]} x {value_list[2]} = " + str((float(value_list[1]) * float(value_list[0])) * float(value_list[2])))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[1]) * float(value_list[0]) * float(value_list[2])) + " Joule."
    elif formula == "Wz=1*2*0":
        answer_calculation = ttk.Label(formula_frm, text="Wz = m x g x h = " + f"{value_list[1]} x {value_list[2]} x {value_list[0]} = " + str((float(value_list[1]) * float(value_list[2])) * float(value_list[0])))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[1]) * float(value_list[2]) * float(value_list[0])) + " Joule."
    elif formula == "Wz=2*0*1":
        answer_calculation = ttk.Label(formula_frm, text="Wz = m x g x h = " + f"{value_list[2]} x {value_list[0]} x {value_list[1]} = " + str((float(value_list[2]) * float(value_list[0])) * float(value_list[1])))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[2]) * float(value_list[0]) * float(value_list[1])) + " Joule."
    elif formula == "Wz=2*1*0":
        answer_calculation = ttk.Label(formula_frm, text="Wz = m x g x h = " + f"{value_list[2]} x {value_list[1]} x {value_list[0]} = " + str((float(value_list[2]) * float(value_list[1])) * float(value_list[0])))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[2]) * float(value_list[1]) * float(value_list[0])) + " Joule."
    elif formula == "Wz=0*2*1":
        answer_calculation = ttk.Label(formula_frm, text="Wz = m x g x h = " + f"{value_list[0]} x {value_list[2]} x {value_list[1]} = " + str((float(value_list[0]) * float(value_list[2])) * float(value_list[1])))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[2]) * float(value_list[1]) * float(value_list[0])) + " Joule."

    elif formula == "m=0/(1*2)":
        answer_calculation = ttk.Label(formula_frm, text="m = Wz ÷ (g x h) = " + f"{value_list[0]} ÷ ({value_list[1]} x {value_list[2]}) = " + str((float(value_list[0]) / (float(value_list[1]) * float(value_list[2])))))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[0]) / (float(value_list[1]) * float(value_list[2]))) + " kilogram."
    elif formula == "m=0/(2*1)":
        answer_calculation = ttk.Label(formula_frm, text="m = Wz ÷ (g x h) = " + f"{value_list[0]} ÷ ({value_list[2]} x {value_list[1]}) = " + str((float(value_list[0]) / (float(value_list[2]) * float(value_list[1])))))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[0]) / (float(value_list[2]) * float(value_list[1]))) + " kilogram."
    elif formula == "m=1/(0*2)":
        answer_calculation = ttk.Label(formula_frm, text="m = Wz ÷ (g x h) = " + f"{value_list[1]} ÷ ({value_list[0]} x {value_list[2]}) = " + str((float(value_list[1]) / (float(value_list[0]) * float(value_list[2])))))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[1]) / (float(value_list[0]) * float(value_list[2]))) + " kilogram."
    elif formula == "m=1/(2*0)":
        answer_calculation = ttk.Label(formula_frm, text="m = Wz ÷ (g x h) = " + f"{value_list[1]} ÷ ({value_list[2]} x {value_list[0]}) = " + str((float(value_list[1]) / (float(value_list[2]) * float(value_list[0])))))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[1]) / (float(value_list[2]) * float(value_list[0]))) + " kilogram."
    elif formula == "m=2/(0*1)":
        answer_calculation = ttk.Label(formula_frm, text="m = Wz ÷ (g x h) = " + f"{value_list[2]} ÷ ({value_list[0]} x {value_list[1]}) = " + str((float(value_list[2]) / (float(value_list[0]) * float(value_list[1])))))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[2]) / (float(value_list[0]) * float(value_list[1]))) + " kilogram."
    elif formula == "m=2/(1*0)":
        answer_calculation = ttk.Label(formula_frm, text="m = Wz ÷ (g x h) = " + f"{value_list[2]} ÷ ({value_list[1]} x {value_list[0]}) = " + str((float(value_list[2]) / (float(value_list[1]) * float(value_list[0])))))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[2]) / (float(value_list[1]) * float(value_list[0]))) + " kilogram."

    elif formula == "g=0/(1*2)":
        answer_calculation = ttk.Label(formula_frm, text="g = Wz ÷ (m x h) = " + f"{value_list[0]} ÷ ({value_list[1]} x {value_list[2]}) = " + str((float(value_list[0]) / (float(value_list[1]) * float(value_list[2])))))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[0]) / (float(value_list[1]) * float(value_list[2]))) + " Newton per kilogram."
    elif formula == "g=0/(2*1)":
        answer_calculation = ttk.Label(formula_frm, text="g = Wz ÷ (m x h) = " + f"{value_list[0]} ÷ ({value_list[2]} x {value_list[1]}) = " + str((float(value_list[0]) / (float(value_list[2]) * float(value_list[1])))))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[0]) / (float(value_list[2]) * float(value_list[1]))) + " Newton per kilogram."
    elif formula == "g=1/(0*2)":
        answer_calculation = ttk.Label(formula_frm, text="g = Wz ÷ (m x h) = " + f"{value_list[1]} ÷ ({value_list[0]} x {value_list[2]}) = " + str((float(value_list[1]) / (float(value_list[0]) * float(value_list[2])))))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[1]) / (float(value_list[0]) * float(value_list[2]))) + " Newton per kilogram."
    elif formula == "g=1/(2*0)":
        answer_calculation = ttk.Label(formula_frm, text="g = Wz ÷ (m x h) = " + f"{value_list[1]} ÷ ({value_list[2]} x {value_list[0]}) = " + str((float(value_list[1]) / (float(value_list[2]) * float(value_list[0])))))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[1]) / (float(value_list[2]) * float(value_list[0]))) + " Newton per kilogram."
    elif formula == "g=2/(0*1)":
        answer_calculation = ttk.Label(formula_frm, text="g = Wz ÷ (m x h) = " + f"{value_list[2]} ÷ ({value_list[0]} x {value_list[1]}) = " + str((float(value_list[2]) / (float(value_list[0]) * float(value_list[1])))))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[2]) / (float(value_list[0]) * float(value_list[1]))) + " Newton per kilogram."
    elif formula == "g=2/(1*0)":
        answer_calculation = ttk.Label(formula_frm, text="g = Wz ÷ (m x h) = " + f"{value_list[2]} ÷ ({value_list[1]} x {value_list[0]}) = " + str((float(value_list[2]) / (float(value_list[1]) * float(value_list[0])))))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[2]) / (float(value_list[1]) * float(value_list[0]))) + " Newton per kilogram."

    elif formula == "h=0/(1*2)":
        answer_calculation = ttk.Label(formula_frm, text="g = Wz ÷ (m x g) = " + f"{value_list[0]} ÷ ({value_list[1]} x {value_list[2]}) = " + str((float(value_list[0]) / (float(value_list[1]) * float(value_list[2])))))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[0]) / (float(value_list[1]) * float(value_list[2]))) + " Meter."
    elif formula == "h=0/(2*1)":
        answer_calculation = ttk.Label(formula_frm, text="g = Wz ÷ (m x g) = " + f"{value_list[0]} ÷ ({value_list[2]} x {value_list[1]}) = " + str((float(value_list[0]) / (float(value_list[2]) * float(value_list[1])))))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[0]) / (float(value_list[2]) * float(value_list[1]))) + " Meter."
    elif formula == "h=1/(0*2)":
        answer_calculation = ttk.Label(formula_frm, text="g = Wz ÷ (m x g) = " + f"{value_list[1]} ÷ ({value_list[0]} x {value_list[2]}) = " + str((float(value_list[1]) / (float(value_list[0]) * float(value_list[2])))))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[1]) / (float(value_list[0]) * float(value_list[2]))) + " Meter."
    elif formula == "h=1/(2*0)":
        answer_calculation = ttk.Label(formula_frm, text="g = Wz ÷ (m x g) = " + f"{value_list[1]} ÷ ({value_list[2]} x {value_list[0]}) = " + str((float(value_list[1]) / (float(value_list[2]) * float(value_list[0])))))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[1]) / (float(value_list[2]) * float(value_list[0]))) + " Meter."
    elif formula == "h=2/(0*1)":
        answer_calculation = ttk.Label(formula_frm, text="g = Wz ÷ (m x g) = " + f"{value_list[2]} ÷ ({value_list[0]} x {value_list[1]}) = " + str((float(value_list[2]) / (float(value_list[0]) * float(value_list[1])))))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[2]) / (float(value_list[0]) * float(value_list[1]))) + " Meter."
    elif formula == "h=2/(1*0)":
        answer_calculation = ttk.Label(formula_frm, text="g = Wz ÷ (m x g) = " + f"{value_list[2]} ÷ ({value_list[1]} x {value_list[0]}) = " + str((float(value_list[2]) / (float(value_list[1]) * float(value_list[0])))))
        answer_calculation.grid(column=1, row=5)
        return str(float(value_list[2]) / (float(value_list[1]) * float(value_list[0]))) + " Meter."

def showAnswer(answer):
    print(f"Answer: {answer}")
    answer_text = ttk.Label(formula_frm, text=str(answer))
    answer_text.grid(column=1, row=6)


def formulaFinder():
    ttk.Label(formula_frm, text="Eerste Gegeven Eenheid:").grid(column=0, row=0)
    unit1 = ttk.Combobox(formula_frm, values=unit_list, width=50)
    unit1.grid(column=1, row=0)
    ttk.Label(formula_frm, text="Eerste Gegeven Waarde:").grid(column=2, row=0)
    value1 = ttk.Entry(formula_frm, width=20)
    value1.grid(column=3, row=0)
    ttk.Label(formula_frm, text="Tweede Gegeven Eenheid:").grid(column=0, row=1)
    unit2 = ttk.Combobox(formula_frm, values=unit_list, width=50)
    unit2.grid(column=1, row=1)
    ttk.Label(formula_frm, text="Tweede Gegeven Waarde:").grid(column=2, row=1)
    value2 = ttk.Entry(formula_frm, width=20)
    value2.grid(column=3, row=1)
    ttk.Label(formula_frm, text="Derde Gegeven Eenheid:").grid(column=0, row=2)
    unit3 = ttk.Combobox(formula_frm, values=unit_list, width=50)
    unit3.grid(column=1, row=2)
    ttk.Label(formula_frm, text="Derde Gegeven Waarde:").grid(column=2, row=2)
    value3 = ttk.Entry(formula_frm, width=20)
    value3.grid(column=3, row=2)
    calculate_button = ttk.Button(formula_frm, command=lambda: showAnswer(runCalculation(findAndFormFormula(checkInputType(unit1.get(), unit2.get(), unit3.get())), checkForEmptyInput(value1.get(), value2.get(), value3.get()))), text="Bereken!")
    calculate_button.grid(column=1, row=4)
    main_frm.destroy()

ttk.Label(main_frm, text="Kies één van de tools!").grid(column=0, row=0)

ttk.Button(main_frm, command=formulaFinder, text="Formules Vinden en Uitvoeren").grid(column=0, row=1)


window.mainloop()