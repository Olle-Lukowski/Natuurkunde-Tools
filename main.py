import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Natuurkunde Tools!")

main_frm = ttk.Frame(window, padding=10)
main_frm.grid()

formula_frm = ttk.Frame(window, padding=10)
formula_frm.grid()

unit_list = ["W (arbeid in Joule)", "F (kracht in Newton)", "s (afstand in Meter)", "Vgem (gemiddelde snelheid in Meter per Seconde)", "t (tijd in Seconden)", "stoot (stoot in Newton Seconde)"]

def findAndCalculate(unit1, unit2, unit3, value1, value2, value3, requested_value):
    #Arbeid Formule
    if unit1 == "W (arbeid in Joule)" and unit2 == "F (kracht in Newton)" and requested_value == "s (afstand in Meter)":
        answer = ttk.Label(formula_frm, text=str(float(value1) / float(value2))+" Meter.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="s = W ÷ F = " + f"{value1} ÷ {value2} = " + str(float(value1) / float(value2)))
        answer_calculation.grid(column=1, row=5)

    elif unit1 == "F (kracht in Newton)" and unit2 == "W (arbeid in Joule)" and requested_value == "s (afstand in Meter)":
        answer = ttk.Label(formula_frm, text=str(float(value2) / float(value1))+" Meter.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="s = W ÷ F = " + f"{value2} ÷ {value1} = " + str(float(value2) / float(value1)))
        answer_calculation.grid(column=1, row=5)

    elif unit2 == "W (arbeid in Joule)" and unit3 == "F (kracht in Newton)" and requested_value == "s (afstand in Meter)":
        answer = ttk.Label(formula_frm, text=str(float(value2) / float(value3))+" Meter.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="s = W ÷ F = " + f"{value2} ÷ {value3} = " + str(float(value2) / float(value3)))
        answer_calculation.grid(column=1, row=5)

    elif unit2 == "F (kracht in Newton)" and unit3 == "W (arbeid in Joule)" and requested_value == "s (afstand in Meter)":
        answer = ttk.Label(formula_frm, text=str(float(value3) / float(value2))+" Meter.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="s = W ÷ F = " + f"{value3} ÷ {value2} = " + str(float(value3) / float(value2)))
        answer_calculation.grid(column=1, row=5)
    
    #------------------------------------------------------------------------------------------------------------------------------------------

    if unit1 == "F (kracht in Newton)" and unit2 == "s (afstand in Meter)" and requested_value == "W (arbeid in Joule)":
        answer = ttk.Label(formula_frm, text=str(float(value1) * float(value2))+" Joule.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="W = F x s = " + f"{value1} x {value2} = " + str(float(value1) * float(value2)))
        answer_calculation.grid(column=1, row=5)

    elif unit1 == "s (afstand in Meter)" and unit2 == "F (kracht in Newton)" and requested_value == "W (arbeid in Joule)":
        answer = ttk.Label(formula_frm, text=str(float(value2) * float(value1))+" Joule.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="W = F x s = " + f"{value2} x {value1} = " + str(float(value2) * float(value1)))
        answer_calculation.grid(column=1, row=5)

    elif unit2 == "F (kracht in Newton)" and unit3 == "s (afstand in Meter)" and requested_value == "W (arbeid in Joule)":
        answer = ttk.Label(formula_frm, text=str(float(value2) * float(value3))+" Joule.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="W = F x s = " + f"{value2} x {value3} = " + str(float(value2) * float(value3)))
        answer_calculation.grid(column=1, row=5)

    elif unit2 == "s (afstand in Meter)" and unit3 == "F (kracht in Newton)" and requested_value == "W (arbeid in Joule)":
        answer = ttk.Label(formula_frm, text=str(float(value3) * float(value2))+" Joule.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="W = F x s = " + f"{value3} x {value2} = " + str(float(value3) * float(value2)))
        answer_calculation.grid(column=1, row=5)

    #------------------------------------------------------------------------------------------------------------------------------------------

    if unit1 == "W (arbeid in Joule)" and unit2 == "s (afstand in Meter)" and requested_value == "F (kracht in Newton)":
        answer = ttk.Label(formula_frm, text=str(float(value1) / float(value2))+" Newton.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="s = W ÷ F = " + f"{value1} ÷ {value2} = " + str(float(value1) / float(value2)))
        answer_calculation.grid(column=1, row=5)

    elif unit1 == "s (afstand in Meter)" and unit2 == "W (arbeid in Joule)" and requested_value == "F (kracht in Newton)":
        answer = ttk.Label(formula_frm, text=str(float(value2) / float(value1))+" Newton.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="s = W ÷ F = " + f"{value2} ÷ {value1} = " + str(float(value2) / float(value1)))
        answer_calculation.grid(column=1, row=5)

    elif unit2 == "W (arbeid in Joule)" and unit3 == "s (afstand in Meter)" and requested_value == "F (kracht in Newton)":
        answer = ttk.Label(formula_frm, text=str(float(value2) / float(value3))+" Newton.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="s = W ÷ F = " + f"{value2} ÷ {value3} = " + str(float(value2) / float(value3)))
        answer_calculation.grid(column=1, row=5)

    elif unit2 == "s (afstand in Meter)" and unit3 == "W (arbeid in Joule)" and requested_value == "F (kracht in Newton)":
        answer = ttk.Label(formula_frm, text=str(float(value3) / float(value2))+" Newton.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="s = W ÷ F = " + f"{value3} ÷ {value2} = " + str(float(value3) / float(value2)))
        answer_calculation.grid(column=1, row=5)

    #Gemiddlde Snelheid formule
    if unit1 == "s (afstand in Meter)" and unit2 == "t (tijd in Seconden)" and requested_value == "Vgem (gemiddelde snelheid in Meter per Seconde)":
        answer = ttk.Label(formula_frm, text=str(float(value1) / float(value2))+" Meter per Seconde.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="Vgem = s ÷ t = " + f"{value1} ÷ {value2} = " + str(float(value1) / float(value2)))
        answer_calculation.grid(column=1, row=5)

    elif unit1 == "t (tijd in Seconden)" and unit2 == "s (afstand in Meter)" and requested_value == "Vgem (gemiddelde snelheid in Meter per Seconde)":
        answer = ttk.Label(formula_frm, text=str(float(value2) / float(value1))+" Meter per Seconde.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="Vgem = s ÷ t = " + f"{value2} ÷ {value1} = " + str(float(value2) / float(value1)))
        answer_calculation.grid(column=1, row=5)

    elif unit2 == "s (afstand in Meter)" and unit3 == "t (tijd in Seconden)" and requested_value == "Vgem (gemiddelde snelheid in Meter per Seconde)":
        answer = ttk.Label(formula_frm, text=str(float(value2) / float(value3))+" Meter per Seconde.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="Vgem = s ÷ t = " + f"{value2} ÷ {value3} = " + str(float(value2) / float(value3)))
        answer_calculation.grid(column=1, row=5)

    elif unit2 == "t (tijd in Seconden)" and unit3 == "s (afstand in Meter)" and requested_value == "Vgem (gemiddelde snelheid in Meter per Seconde)":
        answer = ttk.Label(formula_frm, text=str(float(value3) / float(value2))+" Meter per Seconde.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="Vgem = s ÷ t = " + f"{value3} ÷ {value2} = " + str(float(value3) / float(value2)))
        answer_calculation.grid(column=1, row=5)

    #------------------------------------------------------------------------------------------------------------------------------------------

    if unit1 == "s (afstand in Meter)" and unit2 == "Vgem (gemiddelde snelheid in Meter per Seconde)" and requested_value == "t (tijd in Seconden)":
        answer = ttk.Label(formula_frm, text=str(float(value1) / float(value2))+" Seconde.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="t = s ÷ Vgem = " + f"{value1} ÷ {value2} = " + str(float(value1) / float(value2)))
        answer_calculation.grid(column=1, row=5)

    elif unit1 == "Vgem (gemiddelde snelheid in Meter per Seconde)" and unit2 == "s (afstand in Meter)" and requested_value == "t (tijd in Seconden)":
        answer = ttk.Label(formula_frm, text=str(float(value2) / float(value1))+" Seconde.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="t = s ÷ Vgem = " + f"{value2} ÷ {value1} = " + str(float(value2) / float(value1)))
        answer_calculation.grid(column=1, row=5)

    elif unit2 == "s (afstand in Meter)" and unit3 == "Vgem (gemiddelde snelheid in Meter per Seconde)" and requested_value == "t (tijd in Seconden)":
        answer = ttk.Label(formula_frm, text=str(float(value2) / float(value3))+" Seconde.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="t = s ÷ Vgem = " + f"{value2} ÷ {value3} = " + str(float(value2) / float(value3)))
        answer_calculation.grid(column=1, row=5)

    elif unit2 == "Vgem (gemiddelde snelheid in Meter per Seconde)" and unit3 == "s (afstand in Meter)" and requested_value == "t (tijd in Seconden)":
        answer = ttk.Label(formula_frm, text=str(float(value3) / float(value2))+" Seconde.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="t = s ÷ Vgem = " + f"{value3} ÷ {value2} = " + str(float(value3) / float(value2)))
        answer_calculation.grid(column=1, row=5)

    #------------------------------------------------------------------------------------------------------------------------------------------

    if unit1 == "Vgem (gemiddelde snelheid in Meter per Seconde)" and unit2 == "t (tijd in Seconden)" and requested_value == "s (afstand in Meter)":
        answer = ttk.Label(formula_frm, text=str(float(value1) * float(value2))+" Meter.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="t = s x Vgem = " + f"{value1} x {value2} = " + str(float(value1) * float(value2)))
        answer_calculation.grid(column=1, row=5)

    elif unit1 == "t (tijd in Seconden)" and unit2 == "Vgem (gemiddelde snelheid in Meter per Seconde)" and requested_value == "s (afstand in Meter)":
        answer = ttk.Label(formula_frm, text=str(float(value2) * float(value1))+" Meter.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="t = s x Vgem = " + f"{value2} x {value1} = " + str(float(value2) * float(value1)))
        answer_calculation.grid(column=1, row=5)

    elif unit2 == "Vgem (gemiddelde snelheid in Meter per Seconde)" and unit3 == "t (tijd in Seconden)" and requested_value == "s (afstand in Meter)":
        answer = ttk.Label(formula_frm, text=str(float(value2) * float(value3))+" Meter.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="t = s x Vgem = " + f"{value2} x {value3} = " + str(float(value2) * float(value3)))
        answer_calculation.grid(column=1, row=5)

    elif unit2 == "t (tijd in Seconden)" and unit3 == "Vgem (gemiddelde snelheid in Meter per Seconde)" and requested_value == "s (afstand in Meter)":
        answer = ttk.Label(formula_frm, text=str(float(value3) * float(value2))+" Meter.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="t = s x Vgem = " + f"{value3} x {value2} = " + str(float(value3) * float(value2)))
        answer_calculation.grid(column=1, row=5)

    # Stoot Formule
    if unit1 == "stoot (stoot in Newton Seconde)"and unit2 == "F (kracht in Newton)" and requested_value == "t (tijd in Seconden)":
        answer = ttk.Label(formula_frm, text=str(float(value1) / float(value2))+" Seconde.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="t = stoot ÷ F = " + f"{value1} ÷ {value2} = " + str(float(value1) / float(value2)))
        answer_calculation.grid(column=1, row=5)

    elif unit1 == "F (kracht in Newton)" and unit2 == "stoot (stoot in Newton Seconde)" and requested_value == "t (tijd in Seconden)":
        answer = ttk.Label(formula_frm, text=str(float(value2) / float(value1))+" Seconde.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="t = stoot ÷ F = " + f"{value2} ÷ {value1} = " + str(float(value2) / float(value1)))
        answer_calculation.grid(column=1, row=5)

    elif unit2 == "stoot (stoot in Newton Seconde)" and unit3 == "F (kracht in Newton)" and requested_value == "t (tijd in Seconden)":
        answer = ttk.Label(formula_frm, text=str(float(value2) / float(value3))+" Seconde.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="t = stoot ÷ F = " + f"{value2} ÷ {value3} = " + str(float(value2) / float(value3)))
        answer_calculation.grid(column=1, row=5)

    elif unit2 == "F (kracht in Newton)" and unit3 == "stoot (stoot in Newton Seconde)" and requested_value == "t (tijd in Seconden)":
        answer = ttk.Label(formula_frm, text=str(float(value3) / float(value2))+" Seconde.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="t = stoot ÷ F = " + f"{value3} ÷ {value2} = " + str(float(value3) / float(value2)))
        answer_calculation.grid(column=1, row=5)
    
    #------------------------------------------------------------------------------------------------------------------------------------------

    if unit1 == "F (kracht in Newton)" and unit2 == "t (tijd in Seconden)" and requested_value == "stoot (stoot in Newton Seconde)":
        answer = ttk.Label(formula_frm, text=str(float(value1) * float(value2))+" Newton Seconde.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="stoot = F x t = " + f"{value1} x {value2} = " + str(float(value1) * float(value2)))
        answer_calculation.grid(column=1, row=5)

    elif unit1 == "t (tijd in Seconden)" and unit2 == "F (kracht in Newton)" and requested_value == "stoot (stoot in Newton Seconde)":
        answer = ttk.Label(formula_frm, text=str(float(value2) * float(value1))+" Newton Seconde.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="stoot = F x t = " + f"{value2} x {value1} = " + str(float(value2) * float(value1)))
        answer_calculation.grid(column=1, row=5)

    elif unit2 == "F (kracht in Newton)" and unit3 == "t (tijd in Seconden)" and requested_value == "stoot (stoot in Newton Seconde)":
        answer = ttk.Label(formula_frm, text=str(float(value2) * float(value3))+" Newton Seconde.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="stoot = F x t = " + f"{value2} x {value3} = " + str(float(value2) * float(value3)))
        answer_calculation.grid(column=1, row=5)

    elif unit2 == "t (tijd in Seconden)" and unit3 == "F (kracht in Newton)" and requested_value == "stoot (stoot in Newton Seconde)":
        answer = ttk.Label(formula_frm, text=str(float(value3) * float(value2))+" Newton Seconde.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="stoot = F x t = " + f"{value3} x {value2} = " + str(float(value3) * float(value2)))
        answer_calculation.grid(column=1, row=5)

    #------------------------------------------------------------------------------------------------------------------------------------------

    if unit1 == "stoot (stoot in Newton Seconde)" and unit2 == "t (tijd in Seconden)" and requested_value == "F (kracht in Newton)":
        answer = ttk.Label(formula_frm, text=str(float(value1) / float(value2))+" Newton.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="F = stoot ÷ t = " + f"{value1} ÷ {value2} = " + str(float(value1) / float(value2)))
        answer_calculation.grid(column=1, row=5)

    elif unit1 == "t (tijd in Seconden)" and unit2 == "stoot (stoot in Newton Seconde)" and requested_value == "F (kracht in Newton)":
        answer = ttk.Label(formula_frm, text=str(float(value2) / float(value1))+" Newton.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="F = stoot ÷ t = " + f"{value2} ÷ {value1} = " + str(float(value2) / float(value1)))
        answer_calculation.grid(column=1, row=5)

    elif unit2 == "stoot (stoot in Newton Seconde)" and unit3 == "t (tijd in Seconden)" and requested_value == "F (kracht in Newton)":
        answer = ttk.Label(formula_frm, text=str(float(value2) / float(value3))+" Newton.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="F = stoot ÷ t = " + f"{value2} ÷ {value3} = " + str(float(value2) / float(value3)))
        answer_calculation.grid(column=1, row=5)

    elif unit2 == "t (tijd in Seconden)" and unit3 == "stoot (stoot in Newton Seconde)" and requested_value == "F (kracht in Newton)":
        answer = ttk.Label(formula_frm, text=str(float(value3) / float(value2))+" Newton.")
        answer.grid(column=1, row=6)
        answer_calculation = ttk.Label(formula_frm, text="F = stoot ÷ t = " + f"{value3} ÷ {value2} = " + str(float(value3) / float(value2)))
        answer_calculation.grid(column=1, row=5)


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
    ttk.Label(formula_frm, text="Gevraagde eenheid:").grid(column=0, row=3)
    requested_value = ttk.Combobox(formula_frm, values=unit_list, width=50)
    requested_value.grid(column=1, row=3)
    calculate_button = ttk.Button(formula_frm, command=lambda: findAndCalculate(unit1.get(), unit2.get(), unit3.get(), value1.get(), value2.get(), value3.get(), requested_value.get()), text="Bereken!")
    calculate_button.grid(column=1, row=4)
    main_frm.destroy()

ttk.Label(main_frm, text="Kies één van de tools!").grid(column=0, row=0)

ttk.Button(main_frm, command=formulaFinder, text="Formules Vinden en Uitvoeren").grid(column=0, row=1)


window.mainloop()