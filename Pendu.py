# -*- coding: utf-8 -*-
import json
import random
from tkinter.constants import END

class jeu_pendu() :

    def __init__(self) :
        self.sol =[]
        self.motsol=""
        self.vie = 8
        self.lettre_util = ""
        self.motl=""
        with open('Dico.json') as json_dic:
            self.data_dict = json.load(json_dic)


    def difficult(self) : 
        self.lvl = input("difficulté : ")
        if self.lvl.isdigit() :
            
            if int(self.lvl) in [3,4,5,6,7] :
                self.mot = self.data_dict[self.lvl][random.randint(0,len(self.data_dict[self.lvl]))]
                self.mot = self.mot.lower()
                self.motl = list(self.mot)
                print(self.mot)
            else :
                print("il faut choisir entre 3 et 7 lettres")
                jeu_pendu.difficult(self)
        else :
            print("il faut choisir entre 3 et 7 lettres")
            jeu_pendu.difficult(self)

    def verif(self) :
        self.mot_essai = input("quelle lettre : ")
        

        self.mot_essai = self.mot_essai.lower()

    def liste_mot(self) :
        for i in range(len(self.motl)) :
            self.sol.append("_ ")
            self.sol[0] = self.motl[0] 


    def pendu(self) :  
        jeu_pendu.difficult(self)
        jeu_pendu.liste_mot(self)
        while self.sol != self.motl :  
            
            jeu_pendu.verif(self)
            
            self.lettre_util += self.mot_essai + " , "
            print("lettres utilisée : ", self.lettre_util)            
            for self.lettresol in self.mot_essai:
                if int(self.vie) >= 0 :
                    if self.lettresol in self.mot :
                        for i,self.lettre in enumerate(self.motl) :
                            if self.lettresol == self.lettre :
                                self.sol[int(i)] = self.lettre
                                self.motsol =""
                                for j in self.sol : 
                                    self.motsol += j
                                print(self.motsol,"sol")
                                
                    else :
                        print("perdu")
                        self.vie -= 1
                        if int(self.vie) >= 0 :
                            print("il te reste ",self.vie," vie")
                        if self.vie == 0:
                            self.sol = self.motl
                            print("t as perdu ")
                            
        jeu_pendu.rejouer(self)

    def rejouer(self) :                
        self.rejouer = input("rejouer oui   non ") 
        if self.rejouer  == "oui" :
            self.sol =[]
            self.motsol=""
            self.vie = 8
            self.lettre_util = ""
            self.motl=""
            jeu_pendu.pendu(self)
        if self.rejouer == "non" :
            END
        else :
            jeu_pendu.rejouer(self)



jeu = jeu_pendu()
jeu.pendu()