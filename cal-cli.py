#created 12 mart,
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------")
    print("  CAL-CLI  ")
    print("-----------")
clear()

age = int(input("Unesi godine: "))
weight = float(input("Unesi tezinu: "))
height = int(input("Unesi visinu: "))
clear()
#os.system komanda koja cleara terminal, cls za windows, clear za mac/linux
print("Unesi nivo aktivnosti!\n1.Sjedis cijeli dan (Desk job)\n2.Slabije aktivan (1-2 dana/sedmicno vjezbanja)\n3.Srednje aktivan (3-5 dana)\n4.Aktivan (6-7 dana)\n5.Ekstremno aktivan (Fizicki posao)")
#aktivnost je napravljeno sa dictionary, ko sto je switch u cpp ovo je bolje
aktivnost = {
 1: 1.2,
 2: 1.375,
 3: 1.55,
 4: 1.725,
 5: 1.9
}
aktivnost_izbor = int(input("(1-5): "))
multiplier = aktivnost.get(aktivnost_izbor)
clear()
#.get kao default u switch case u cpp, jer ako stavis 6 ili 0, program crasha, ovako po defaultu daje none value

while True:
    spol = int(input("Unesi spol: Musko(1) - Zensko(2): " ))
    if 1 <= spol <= 2:
      break
    print("Odaberi 1 ili 2!")
if spol == 1:
    spol = "Musko"
    print(f"Trenutni podaci: Godine: {age}, Tezina: {weight}, Visina: {height}, Spol: {spol}")
    BMR = (10 * weight) + (6.25 * height) - (5 * age) + 5
    Maintenance_Calories = BMR * multiplier

elif spol == 2:
    spol = "Zensko"
    print(f"Trenutni podaci: Godine: {age}, Tezina: {weight}, Visina: {height}, Spol: {spol}")
    #trenutni podaci print - NE RADI ali ne javlja error pa jebat ga
    BMR = (10 * weight) + (6.25 * height) - (5 * age) - 161
    Maintenance_Calories = BMR * multiplier
surplus = Maintenance_Calories + 500
deficit = Maintenance_Calories - 500
clear()
print(f"Surplus (+0.5lbs/week): {surplus}\nMaintenance Calories: {Maintenance_Calories}\nDeficit (-0.5lbs/week): {deficit} ")
#NASTAVAK- macro calculator, pa meal logger, napp nesto kao myfitnesspal ali bez preseravanja, onda flask  web app verzija