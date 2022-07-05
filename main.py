# This is a sample Python script.
import importlib

import tesouro
dice = importlib.import_module("dice","venv\Lib\site-packages\ ")

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def RollLoot(nd):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Rolagem para ND: {nd}')  # Press Ctrl+F8 to toggle the breakpoint.
    rollDadoD = dice.roll('1d100')
    rollDadoL = dice.roll('1d100')
    #print(f'rollD: {rollDadoD[0]}')
    #print(f'rollL: {rollDadoL[0]}')
    #print(dice.roll('1d1'))
    rollTesouro = tesouro.Search(nd, rollDadoL[0])
    rollDinheiro = tesouro.Search(nd, rollDadoD[0])

    Tesouro = rollTesouro.dinheiro.replace("'","")
    Dinheiros = rollDinheiro.dinheiro.replace("'","")
    if Dinheiros == "-":
        Dinheiros = "Nada!"
    else:
        #print(Dinheiros)
        Lista = Dinheiros.split(" ")
        #print(Lista)

        dadoDinheiro = dice.roll(Lista[0].__str__().replace("x","*"))
        #print(dadoDinheiro)
        Dinheiros = f'{dadoDinheiro}{Lista[1]}'
        Dinheiros = Dinheiros.replace("s","$")
    Items = rollTesouro.item.replace("'","")
    if Items == "-":
        Items = "Nada!"

    print(f' Você recebeu de dinheiro: {Dinheiros} e de items: {Items}')

def DiceRoll(Dado):
    DadoS = Dado.split("d")
    seMod = DadoS[1].__str__()
    Mod = ""
    Tdado = DadoS
    if seMod.find("+") != -1 :
        seMod.split("+")
        Tdado = seMod[0]
        Mod = seMod[1]
    print(DadoS)
    if isinstance(seMod, int) :
        print("DadoS é STR!!")
    else:
        maxDice = dice.roll_max(DadoS[0])
    #    maxDice = maxDice[0].__str__()
        minDice = dice.roll_min(DadoS[0])
    #    minDice = minDice[0].__str__()
        print(f'{maxDice},{minDice}')
        rolls = dice.roll(DadoS[0])
        rolls.sort()
        c = 0
        rollsF = []
        Soma = 0
        for i in rolls:
            #print(f'I={i}')
            if i == maxDice[0] or i == minDice[0]:

                rollsF.append(f'**{i}**')
                #print(rollsF)
            else:
                rollsF.append(f'{i}')
            c = c + 1
            Soma = Soma + i
        rollsF = rollsF.__str__().replace("'","")
        RollRusult = f' `{Soma}` ⟵ {rollsF} {Dado}'
        #rolls = rolls.replace(maxDice, f'**{maxDice}**')
        #rolls = rolls.replace(minDice, f'**{minDice}**')
        #print(f'Rolei {rollsF}')
    return  RollRusult

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    RollLoot('3')

    #DiceRoll("5d10")
    print(DiceRoll("5d10+5"))
    #print(dice.roll("3d20"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
