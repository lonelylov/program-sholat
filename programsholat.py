import streamlit as st
import math
import numpy as np
import pandas as pd

st.title("""
Program Jadwal Sholat
Tugas Kuliah Komputasi Astronomi
""") 

############################

#############################

kota = st.selectbox ("Pilih lokasi anda:", ("jakarta", "Surabaya", "batang", "denpasar", "pekalongan", "Malang")
)

df = pd.read_csv(r'database_kota.csv')

lintang = df[kota][0]
bujur = df[kota][1]
H = df[kota][2]
Z = df[kota][3]

D=int(st.number_input("tanggal:",1,31))
M=int(st.number_input("bulan:",1,12))
Y=int(st.number_input("tahun:",1))

cari=st.button("cari")

col1,col2=st.columns([1,2])

if cari:
 #with col1:
  #gregorian to julian
  if M > 2 :
   M = M
   Y = Y
  elif M in [1 or 2]:
   M = M +12
   Y = Y -1

  A=int(Y/100)
  B=2+int(A/4)-A

  JD=1720994.5+int(365.25*Y)+int(30.6001*(M+1))+(B)+D+0.5
  JDlokal=float(JD-(Z/24))

  #sudut tanggal
  T=float(2*math.pi*(JDlokal-2451545)/365.25)

  #sudut deklinasi
  delta=0.37877+23.264*math.sin((57.297*T-79.547)*(math.pi/180))+0.3812*math.sin((2*57.297*T-82.682)*(math.pi/180))+0.17132*math.sin((3*57.297*T-59.722)*(math.pi/180))

  #Equation of time
  U=(JDlokal-2451545)/36525
  L0=280.46607+36000.7698*U
  L0n=L0%360
  ET=(-(1789+237*U)*math.sin(math.pi*L0n/180)-(7146-62*U)*math.cos(math.pi*L0n/180)+(9934-14*U)*math.sin(2*math.pi*L0n/180)-(29+5*U)*math.cos(2*math.pi*L0n/180)+(74+10*U)*math.sin(3*math.pi*L0n/180)+(320-4*U)*math.cos(3*math.pi*L0n/180)-212*math.sin(4*math.pi*L0n/180))/1000

  #waktu transit
  WT=12+Z-(bujur/15)-(ET/60)

  #Penentuan h & HA
  KA=1
  h_as=(math.atan(1/(KA+math.tan((abs(delta-lintang))*(math.pi/180)))))*180/math.pi
  h_m=(-0.8333-0.0347*(H**0.5))
  h_i=-18
  h_s=-20
 
  HA_as=math.acos((((math.sin(h_as*(math.pi/180)))-(math.sin(lintang*(math.pi/180)))*(math.sin(delta*(math.pi/180))))/((math.cos(lintang*(math.pi/180)))*(math.cos(delta*(math.pi/180))))))*180/math.pi
  HA_m=math.acos((((math.sin(h_m*(math.pi/180)))-(math.sin(lintang*(math.pi/180)))*(math.sin(delta*(math.pi/180))))/((math.cos(lintang*(math.pi/180)))*(math.cos(delta*(math.pi/180))))))*180/math.pi
  HA_i=math.acos((((math.sin(h_i*(math.pi/180)))-(math.sin(lintang*(math.pi/180)))*(math.sin(delta*(math.pi/180))))/((math.cos(lintang*(math.pi/180)))*(math.cos(delta*(math.pi/180))))))*180/math.pi
  HA_s=math.acos((((math.sin(h_s*(math.pi/180)))-(math.sin(lintang*(math.pi/180)))*(math.sin(delta*(math.pi/180))))/((math.cos(lintang*(math.pi/180)))*(math.cos(delta*(math.pi/180))))))*180/math.pi

  dzuhur=WT
  subuh=WT-(HA_s/15)
  terbit=WT-(HA_m/15)
  ashar=WT+(HA_as/15)
  maghrib=WT+(HA_m/15)
  isya=WT+(HA_i/15)
 

  st.write("WAKTU SHOLAT", D,'/',M,'/',Y)
  #subuh
  st.write("subuh-->", int(subuh),":",int(subuh*60%60),":", int(subuh*3600%60))
  #terbit
  st.write("terbit-->", int(terbit),":",int(terbit*60%60),":", int(terbit*3600%60))
  #dzuhur
  st.write("dzuhur-->", int(dzuhur), ":", int(dzuhur*60%60),":", int(dzuhur*3600%60))
  #ashar
  st.write("ashar-->", int(ashar),":",int(ashar*60%60),":", int(ashar*3600%60))
  #maghrib
  st.write("maghrib-->", int(maghrib),":",int(maghrib*60%60),":", int(maghrib*3600%60))
  #dzuhur
  st.write("isya-->", int(isya),":",int(isya*60%60),":", int(isya*3600%60))

 
  #with col2:
  #30 hari
  bulan_ganjil=[1,3,5,8,10,12]
  bulan_genap=[4,6,7,9,11]
  if M==2:
   jh=28
  elif M in bulan_genap:
   jh=30
  elif M in bulan_ganjil:
   jh=31 
   
 #with st.expander("Waktu sholat dalam 1 bulan"):
  st.write("WAKTU SHOLAT DALAM 1 BULAN")

  st.write("tgl","|","---SUBUH---","||","---TERBIT---","||","---DZUHUR---","||","---ASHAR---","||","---MAGHRIB---","||","---ISYA'---","||")
 
  ite = range(1,jh+1,1)
  for D in ite :
    #gregorian to julian
    if M > 2 :
     M = M
     Y = Y
    elif M in [1 or 2]:
     M = M +12
     Y = Y -1

    A=int(Y/100)
    B=2+int(A/4)-A

    JD=1720994.5+int(365.25*Y)+int(30.6001*(M+1))+(B)+D+0.5
    JDlokal=float(JD-(Z/24))

    #sudut tanggal
    T=float(2*math.pi*(JDlokal-2451545)/365.25)

    #sudut deklinasi
    delta=0.37877+23.264*math.sin((57.297*T-79.547)*(math.pi/180))+0.3812*math.sin((2*57.297*T-82.682)*(math.pi/180))+0.17132*math.sin((3*57.297*T-59.722)*(math.pi/180))

    #Equation of time
    U=(JDlokal-2451545)/36525
    L0=280.46607+36000.7698*U
    L0n=L0%360
    ET=(-(1789+237*U)*math.sin(math.pi*L0n/180)-(7146-62*U)*math.cos(math.pi*L0n/180)+(9934-14*U)*math.sin(2*math.pi*L0n/180)-(29+5*U)*math.cos(2*math.pi*L0n/180)+(74+10*U)*math.sin(3*math.pi*L0n/180)+(320-4*U)*math.cos(3*math.pi*L0n/180)-212*math.sin(4*math.pi*L0n/180))/1000


    #waktu transit
    WT=12+Z-(bujur/15)-(ET/60)


    #Penentuan h & HA
    KA=1
    h_as=(math.atan(1/(KA+math.tan((abs(delta-lintang))*(math.pi/180)))))*180/math.pi
    h_m=(-0.8333-0.0347*(H**0.5))
    h_i=-18
    h_s=-20
 

    HA_as=math.acos((((math.sin(h_as*(math.pi/180)))-(math.sin(lintang*(math.pi/180)))*(math.sin(delta*(math.pi/180))))/((math.cos(lintang*(math.pi/180)))*(math.cos(delta*(math.pi/180))))))*180/math.pi
    HA_m=math.acos((((math.sin(h_m*(math.pi/180)))-(math.sin(lintang*(math.pi/180)))*(math.sin(delta*(math.pi/180))))/((math.cos(lintang*(math.pi/180)))*(math.cos(delta*(math.pi/180))))))*180/math.pi
    HA_i=math.acos((((math.sin(h_i*(math.pi/180)))-(math.sin(lintang*(math.pi/180)))*(math.sin(delta*(math.pi/180))))/((math.cos(lintang*(math.pi/180)))*(math.cos(delta*(math.pi/180))))))*180/math.pi
    HA_s=math.acos((((math.sin(h_s*(math.pi/180)))-(math.sin(lintang*(math.pi/180)))*(math.sin(delta*(math.pi/180))))/((math.cos(lintang*(math.pi/180)))*(math.cos(delta*(math.pi/180))))))*180/math.pi


    dzuhur=WT
    subuh=WT-(HA_s/15)
    terbit=WT-(HA_m/15)
    ashar=WT+(HA_as/15)
    maghrib=WT+(HA_m/15)
    isya=WT+(HA_i/15)
 
    st.write(D,"|",int(subuh),":",int(subuh*60%60),":",int(subuh*3600%60),"|",int(terbit),":",int(terbit*60%60),":",int(terbit*3600%60),"|",int(dzuhur),":",int(dzuhur*60%60),":",int(dzuhur*3600%60),"|",int(ashar),":",int(ashar*60%60),':',int(ashar*3600%60),"|",int(maghrib),":",int(maghrib*60%60),":",int(maghrib*3600%60),"|",int(isya),":",int(isya*60%60),":",int(isya*3600%60))
 
