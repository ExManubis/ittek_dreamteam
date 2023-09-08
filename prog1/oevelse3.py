#! /usr/bin/env python3
biler = 100 # sætter antallet af biler til int 100
plads_i_en_bil = 4.0 # sætter plads i hver bil til float 4.0
førere = 30 # sætter antallet af førere til int 30
passagerer = 90 # sætter antallet af passagerer til int 90
biler_ude_af_drift = biler - førere # finder antallet af førerløse biler
biler_i_kørsel = førere # fortæller hvor biler der bliver kørt af førere
samlet_bil_kapacitet = biler_i_kørsel * plads_i_en_bil # finder den samlede bil kapacitet
gennemsnit_af_passagerer_per_bil = passagerer / biler_i_kørsel # finder hvor mange passagerer der i gennemsnit skal være i hver bil

print('Der er', biler, 'biler til rådighed.') # printer hvor mange biler der er
print('Der er kun', førere, 'førere til rådighed.') # printer hvor mange biler der har førere
print('Der vil være', biler_ude_af_drift, 'tomme biler i dag.') # printer antaller af føreløse biler
print('Vi kan transportere', samlet_bil_kapacitet, 'personer i dag.') # printer den samlede flådekapacitet
print('Vi har', passagerer, 'passagerer i dag.') # printer antallet af passagerer
print('Vi skal cirka putte', gennemsnit_af_passagerer_per_bil, 'i hver bil.') # printer hvor mange personer der i gennemsnit skal sættes i hver bil
