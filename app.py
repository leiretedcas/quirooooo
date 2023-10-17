from flask import Flask ,render_template ,request ,jsonify #line:1
import pandas as pd #line:2
import numpy as np #line:3
import xlrd2 as xlrd #line:4
import unicodedata #line:5
import spacy #line:6
import inflect #line:7
nlp =spacy .load ("es_core_news_sm")#line:9
from inflector import Inflector ,Spanish #line:10
inflector =Inflector (Spanish )#line:11
import speech_recognition as sr #line:12
import os #line:13
import requests #line:14
from requests .auth import HTTPBasicAuth #line:15
import asyncio #line:16
import aiohttp #line:17
auth =aiohttp .BasicAuth ('1234','API')#line:19
base_url ='https://orva.tedcas.com/api/'#line:20
async def buscar_faq (O000O0OO0O00OOOOO ,OO0O00OOOOOOOOO00 ):#line:22
    O0OO0OO0O0OO00OOO ="preguntas_qh_tags2.xlsx"#line:23
    OOOOO0O0O0000OO00 =pd .read_excel (O0OO0OO0O0OO00OOO ,engine ="openpyxl")#line:24
    OO00000O00O0OO0O0 =0 #line:25
    O0OO0OO0O0O0O00O0 =O000O0OO0O00OOOOO #line:26
    O0OO0O0OOOO0O00OO =[]#line:27
    print ("result"+str (O0OO0OO0O0O0O00O0 ))#line:28
    for OOOO00OOOO0000O00 ,O00OOOOO0O0OOO000 in OOOOO0O0O0000OO00 .iterrows ():#line:29
        O0OOO0O0OO000O00O =OOOOO0O0O0000OO00 .loc [OOOO00OOOO0000O00 ,'TAGS2']#line:30
        O0OOO0O0OO000O00O =O0OOO0O0OO000O00O .split (",")#line:31
        O0OO0O0OOOO0O00OO .append (O0OOO0O0OO000O00O )#line:32
    OO000OO0OOOO00000 =[]#line:33
    O0OOO0O0OO000O00O =[]#line:34
    for OO0O00OO00OO0OO0O ,OO00OOO0O000OOO00 in enumerate (O0OO0OO0O0O0O00O0 ):#line:35
        O0OO0OO0O0O0O00O0 [OO0O00OO00OO0OO0O ]=inflector .singularize (str (OO00OOO0O000OOO00 ))#line:36
    O0OOOOOOOOO00OO00 =np .zeros (len (OOOOO0O0O0000OO00 .index ),dtype =int )#line:37
    for OO00O000OO0000OOO ,O00OOOOO0O0OOO000 in enumerate (O0OO0O0OOOO0O00OO ):#line:38
        O00OOO00OOOO000O0 =[]#line:39
        for OO00OOO0O000OOO00 in O00OOOOO0O0OOO000 :#line:40
            if OO0O00OOOOOOOOO00 ==0 :#line:41
                if OO00OOO0O000OOO00 !=[]:#line:42
                    OO00000O00O0OO0O0 =0 #line:43
                    for OOOOO0OOO00OOOOO0 in range (100 ):#line:44
                        OOOOO0OOO00OOOOO0 =OOOOO0OOO00OOOOO0 /10 #line:45
                        OOOOO0OOO00OOOOO0 =str (OOOOO0OOO00OOOOO0 )#line:46
                        if OO00OOO0O000OOO00 ==OOOOO0OOO00OOOOO0 :#line:47
                            OOOOO0OOO00OOOOO0 =OOOOO0OOO00OOOOO0 .split (".")#line:48
                            O00OOO00OOOO000O0 .append (OOOOO0OOO00OOOOO0 [0 ])#line:49
                            O00OOO00OOOO000O0 .append ("con")#line:50
                            O00OOO00OOOO000O0 .append (OOOOO0OOO00OOOOO0 [1 ])#line:51
                            OO00000O00O0OO0O0 =OO00000O00O0OO0O0 +1 #line:52
                    if OO00000O00O0OO0O0 ==0 :#line:53
                        O00OOO00OOOO000O0 .append (OO00OOO0O000OOO00 )#line:54
            if OO0O00OOOOOOOOO00 ==1 :#line:55
                O00OOO00OOOO000O0 .append (OO00OOO0O000OOO00 )#line:56
        OO000OO0OOOO00000 .append (O00OOO00OOOO000O0 )#line:57
        for OOO0OO0O0000O0OOO in O0OO0OO0O0O0O00O0 :#line:58
            for O000000OOO00O000O ,OO00OOO0O000OOO00 in enumerate (OO000OO0OOOO00000 [OO00O000OO0000OOO ]):#line:59
                            if str (OOO0OO0O0000O0OOO )=="maya":#line:60
                                OOO0OO0O0000O0OOO ="malla"#line:61
                            if str (OOO0OO0O0000O0OOO )=="pilos"or str (OOO0OO0O0000O0OOO )=="pilo":#line:62
                                OOO0OO0O0000O0OOO ="philo"#line:63
                            if str (OOO0OO0O0000O0OOO )=="filos"or str (OOO0OO0O0000O0OOO )=="filo":#line:64
                                OOO0OO0O0000O0OOO ="philo"#line:65
                            if str (OOO0OO0O0000O0OOO )=="sinces"or str (OOO0OO0O0000O0OOO )=="sinc":#line:66
                                OOO0OO0O0000O0OOO ="synthe"#line:67
                            if str (OOO0OO0O0000O0OOO )=="sintes"or str (OOO0OO0O0000O0OOO )=="sint":#line:68
                                OOO0OO0O0000O0OOO ="synthe"#line:69
                            if str (OOO0OO0O0000O0OOO )=="axos"or str (OOO0OO0O0000O0OOO )=="axo":#line:70
                                OOO0OO0O0000O0OOO ="axso"#line:71
                            if str (OOO0OO0O0000O0OOO )=="uno":#line:72
                                OOO0OO0O0000O0OOO ="1"#line:73
                            if str (OOO0OO0O0000O0OOO )=="dos"or str (OOO0OO0O0000O0OOO )=="do":#line:74
                                OOO0OO0O0000O0OOO ="2"#line:75
                            if str (OOO0OO0O0000O0OOO )=="tres"or str (OOO0OO0O0000O0OOO )=="tr":#line:76
                                OOO0OO0O0000O0OOO ="3"#line:77
                            if str (OOO0OO0O0000O0OOO )=="cuatro":#line:78
                                OOO0OO0O0000O0OOO ="4"#line:79
                            if str (OOO0OO0O0000O0OOO )=="cinco":#line:80
                                OOO0OO0O0000O0OOO ="5"#line:81
                            if str (OOO0OO0O0000O0OOO )=="seis"or str (OOO0OO0O0000O0OOO )=="sei":#line:82
                                OOO0OO0O0000O0OOO ="6"#line:83
                            if str (OOO0OO0O0000O0OOO )=="siete":#line:84
                                OOO0OO0O0000O0OOO ="7"#line:85
                            if str (OOO0OO0O0000O0OOO )=="ocho":#line:86
                                OOO0OO0O0000O0OOO ="8"#line:87
                            if str (OOO0OO0O0000O0OOO )=="nueve":#line:88
                                OOO0OO0O0000O0OOO ="9"#line:89
                            if str (OOO0OO0O0000O0OOO )=="cero":#line:90
                                OOO0OO0O0000O0OOO ="0"#line:91
                            if str (OOO0OO0O0000O0OOO )=="veintiuno":#line:92
                                OOO0OO0O0000O0OOO ="21"#line:93
                            if str (OOO0OO0O0000O0OOO )=="veinte":#line:94
                                OOO0OO0O0000O0OOO ="20"#line:95
                            if str (OOO0OO0O0000O0OOO )=="veintidos"or str (OOO0OO0O0000O0OOO )=="veintido":#line:96
                                OOO0OO0O0000O0OOO ="22"#line:97
                            if str (OOO0OO0O0000O0OOO )=="veintitres"or str (OOO0OO0O0000O0OOO )=="veintitre":#line:98
                                OOO0OO0O0000O0OOO ="23"#line:99
                            if str (OOO0OO0O0000O0OOO )=="veinticuatro":#line:100
                                OOO0OO0O0000O0OOO ="24"#line:101
                            if str (OOO0OO0O0000O0OOO )=="veinticinco":#line:102
                                OOO0OO0O0000O0OOO ="25"#line:103
                            if str (OOO0OO0O0000O0OOO )=="veintiseis"or str (OOO0OO0O0000O0OOO )=="veintisei":#line:104
                                OOO0OO0O0000O0OOO ="26"#line:105
                            if str (OOO0OO0O0000O0OOO )=="veintisiete":#line:106
                                OOO0OO0O0000O0OOO ="27"#line:107
                            if str (OOO0OO0O0000O0OOO )=="veintiocho":#line:108
                                OOO0OO0O0000O0OOO ="28"#line:109
                            if str (OOO0OO0O0000O0OOO )=="veintinueve":#line:110
                                OOO0OO0O0000O0OOO ="29"#line:111
                            if str (OOO0OO0O0000O0OOO )=="treinta":#line:112
                                OOO0OO0O0000O0OOO ="30"#line:113
                            if str (remove_accents (OO00OOO0O000OOO00 )).lower ()==str (remove_accents (OOO0OO0O0000O0OOO )).lower ():#line:114
                                O0OOOOOOOOO00OO00 [OO00O000OO0000OOO ]=O0OOOOOOOOO00OO00 [OO00O000OO0000OOO ]+1 #line:115
                                OO000OO0OOOO00000 [OO00O000OO0000OOO ].pop (O000000OOO00O000O )#line:116
        O0OOO0O00OOO00O0O =np .argwhere (O0OOOOOOOOO00OO00 ==np .amax (O0OOOOOOOOO00OO00 ))#line:118
        O00O0O00OOO0OO0OO =[]#line:119
        OOO000000OO0O0000 ={}#line:120
        OOOOO0O0O0000OO00 =xlrd .open_workbook (O0OO0OO0O0OO00OOO )#line:121
        OOOOO0O0O0000OO00 =OOOOO0O0O0000OO00 .sheet_by_index (0 )#line:122
        if not np .all (O0OOOOOOOOO00OO00 ==0 ):#line:123
            for OOO0OO0OO0OO00OO0 in O0OOO0O00OOO00O0O :#line:124
                OOOOOO00000000OOO =OOOOO0O0O0000OO00 .cell (int (OOO0OO0OO0OO00OO0 )+1 ,3 )#line:125
                OO0OO00O000O0OOO0 =OOOOO0O0O0000OO00 .cell (int (OOO0OO0OO0OO00OO0 )+1 ,4 )#line:126
                OOOOOO00000000OOO =str (OOOOOO00000000OOO )#line:127
                OO0OO00O000O0OOO0 =str (OO0OO00O000O0OOO0 )#line:128
                OOOOOO00000000OOO =OOOOOO00000000OOO .split ("'")#line:129
                OO0OO00O000O0OOO0 =OO0OO00O000O0OOO0 .split ("'")#line:130
                O00O0O00OOO0OO0OO .append (f" {OOOOOO00000000OOO[1]} {OO0OO00O000O0OOO0[1]} ")#line:131
    return O00O0O00OOO0OO0OO #line:132
async def boton_pdf_video (O0O0000O0OOO0OO00 ,O0O00O0OOOOO00000 ,OO00OO0O0OOOO0O00 ):#line:134
    OO00OOOOOO0000000 =aiohttp .TCPConnector (ssl =True )#line:135
    async with aiohttp .ClientSession (connector =OO00OOOOOO0000000 )as O0OO00OO0OOO0O000 :#line:136
        OOO0OO0OO0OOOOO00 =await O0OO00OO0OOO0O000 .get (f'{base_url}all-content/{O0O0000O0OOO0OO00}',auth =auth )#line:137
        OOOOO0O0000OO00OO =await OOO0OO0OO0OOOOO00 .json ()#line:138
        O00000OOO00OOO00O =[]#line:140
        O00OO0O00O00OO0O0 ={}#line:141
        if OO00OO0O0OOOO0O00 =="0":#line:143
            for OOO000O0000OOO00O in OOOOO0O0000OO00OO :#line:144
                if OOO000O0000OOO00O ['type']=="Intervencion":#line:145
                    O00000OOO00OOO00O .append (OOO000O0000OOO00O ['nid'])#line:146
        else :#line:147
            O00000OOO00OOO00O .append (OO00OO0O0OOOO0O00 )#line:148
        for O0OOOO0O00000000O in O00000OOO00OOO00O :#line:150
            O0O0O000000O00O0O =await O0OO00OO0OOO0O000 .get (f'{base_url}intervenciones/{O0OOOO0O00000000O}',auth =auth )#line:151
            O000O000OO0OOOO00 =await O0O0O000000O00O0O .json ()#line:152
            O000O000OO0OOOO00 =O000O000OO0OOOO00 [0 ]#line:153
            O000OOOOO0O000O0O ={}#line:154
            if O0O00O0OOOOO00000 in O000O000OO0OOOO00 :#line:156
                O0OO00000OO00OOOO =O000O000OO0OOOO00 [O0O00O0OOOOO00000 ]#line:157
                for O000O0O0O00OOO000 in O0OO00000OO00OOOO :#line:158
                    if O0O00O0OOOOO00000 =='field_pdf':#line:159
                        O000OOOOO0O000O0O [O000O0O0O00OOO000 ['descripcion']]="https://orva.tedcas.com/"+str (O000O0O0O00OOO000 ['url'])#line:160
                    if O0O00O0OOOOO00000 =='field_video':#line:161
                        O000OOOOO0O000O0O [O000O0O0O00OOO000 ['descripcion']]=str (O000O0O0O00OOO000 ['url'])#line:162
                O00OO0O00O00OO0O0 [O000O000OO0OOOO00 ['title']]=O000OOOOO0O000O0O #line:164
            else :#line:165
                if OO00OO0O0OOOO0O00 =='0':#line:166
                    OO00OO0O0OOOO0O00 ='0'#line:167
                else :#line:168
                    print ("nid dentro del if "+str (OO00OO0O0OOOO0O00 ))#line:169
                    O000OOOOO0O000O0O ["No hay archivos"]=""#line:170
                    O00OO0O00O00OO0O0 ["No hay archivos"]=O000OOOOO0O000O0O #line:171
        return O00OO0O00O00OO0O0 #line:173
async def boton_word_ppt (O00O0O0OOOOOO0OOO ,O0O000O0O0O000OOO ,O0O000O00O00O0000 ):#line:175
    O000O000OOOO0OO00 =aiohttp .TCPConnector (ssl =True )#line:176
    async with aiohttp .ClientSession (connector =O000O000OOOO0OO00 )as O0O000000000OOOOO :#line:177
        O0O00O00OO0O0OO0O =await O0O000000000OOOOO .get (f'{base_url}all-content/{O00O0O0OOOOOO0OOO}',auth =auth )#line:178
        OO0O0OOOO0O0O0O00 =await O0O00O00OO0O0OO0O .json ()#line:179
        OO0O0OO0O0O00O0O0 =[]#line:181
        O0OOOO00000O00O00 ={}#line:182
        if O0O000O00O00O0000 =='0':#line:184
            for O00OOO00O0O00000O in OO0O0OOOO0O0O0O00 :#line:185
                if O00OOO00O0O00000O ['type']=="Intervencion":#line:186
                    OO0O0OO0O0O00O0O0 .append (O00OOO00O0O00000O ['nid'])#line:187
        else :#line:188
            OO0O0OO0O0O00O0O0 .append (O0O000O00O00O0000 )#line:189
        for OOOOO000OOOO0OOO0 in OO0O0OO0O0O00O0O0 :#line:191
            OO0O00O00OO00000O =await O0O000000000OOOOO .get (f'{base_url}intervenciones/{OOOOO000OOOO0OOO0}',auth =auth )#line:192
            OOO00OO0OOOO0OOOO =await OO0O00O00OO00000O .json ()#line:193
            OOO00OO0OOOO0OOOO =OOO00OO0OOOO0OOOO [0 ]#line:194
            if len (OOO00OO0OOOO0OOOO [O0O000O0O0O000OOO ])!=0 :#line:195
                O0OOOO00000O00O00 [OOO00OO0OOOO0OOOO ['title']]="https://orva.tedcas.com/"+str (OOO00OO0OOOO0OOOO [O0O000O0O0O000OOO ])#line:196
            if len (OOO00OO0OOOO0OOOO [O0O000O0O0O000OOO ])==0 and O0O000O00O00O0000 !='0':#line:197
                O0OOOO00000O00O00 ["No hay archivos"]=""#line:198
        return O0OOOO00000O00O00 #line:200
async def boton_materiales (OOOOOO00OOO000O0O ,OO0O00O00O0O0OO00 ):#line:202
    OOO00OOOOOOOOO00O =aiohttp .TCPConnector (ssl =True )#line:203
    async with aiohttp .ClientSession (connector =OOO00OOOOOOOOO00O )as O0OOOOO0OO00O000O :#line:204
        O00O0OO0O0O00O0OO ={}#line:205
        if OO0O00O00O0O0OO00 =='0':#line:207
            O0O0000O000O000O0 =await O0OOOOO0OO00O000O .get (f'{base_url}listado_completo_cajas/{OOOOOO00OOO000O0O}',auth =auth )#line:208
            OOOOOO0OO0O0OOOO0 =await O0O0000O000O000O0 .json ()#line:209
            for OO0OO0000O0OOO00O in OOOOOO0OO0O0OOOO0 :#line:210
                O00O0OO0O0O00O0OO [OO0OO0000O0OOO00O ['title']]=OO0OO0000O0OOO00O ['nid']#line:211
            O00O0OO0O0O00O0OO ['']="si hay"#line:212
        else :#line:213
            O0O0000O000O000O0 =await O0OOOOO0OO00O000O .get (f'{base_url}intervenciones/{OO0O00O00O0O0OO00}',auth =auth )#line:214
            OOOOOO0OO0O0OOOO0 =await O0O0000O000O000O0 .json ()#line:215
            OOOOOO0OO0O0OOOO0 =OOOOOO0OO0O0OOOO0 [0 ]#line:216
            if 'field_cajas'in OOOOOO0OO0O0OOOO0 :#line:217
                OOOOOO0OO0O0OOOO0 =OOOOOO0OO0O0OOOO0 ['field_cajas']#line:218
                for OO0OO0000O0OOO00O in OOOOOO0OO0O0OOOO0 :#line:219
                    O00O0OO0O0O00O0OO [OO0OO0000O0OOO00O ['caja']]=OO0OO0000O0OOO00O ['id']#line:220
                O00O0OO0O0O00O0OO ['']="si hay"#line:221
            else :#line:222
                if OO0O00O00O0O0OO00 !=0 :#line:223
                    O00O0OO0O0O00O0OO ['']=""#line:224
        return O00O0OO0O0O00O0OO #line:225
async def cargar_base_datos (O000OO00O0O0OO0OO ,OOOO0OO00OO000O0O ):#line:227
    O000000OOOOOOO0OO =None #line:228
    OOOOO0O0O0OO000O0 =[]#line:229
    OOO0OOOOOO0OO0O0O =aiohttp .TCPConnector (ssl =True )#line:230
    async with aiohttp .ClientSession (connector =OOO0OOOOOO0OO0O0O )as OO0O0O0O0OOOOO0OO :#line:231
        OO00OOO000000OO00 =await OO0O0O0O0OOOOO0OO .get ('https://orva.tedcas.com/api/all-content/'+str (OOOO0OO00OO000O0O ),auth =auth )#line:232
        O0OOO0OOOOO00O00O =await OO00OOO000000OO00 .json ()#line:233
        OOOO0O0OOOOO000O0 =np .zeros (len (O0OOO0OOOOO00O00O ),dtype =int )#line:234
        OO0000O0OOO0OO0OO =[]#line:235
        for OO00O000000O00O0O in O000OO00O0O0OO0OO :#line:236
            O0OOOO000O0OOOO00 =0 #line:237
            for O00000O0OO0OOO000 in range (100 ):#line:238
                O00000O0OO0OOO000 =O00000O0OO0OOO000 /10 #line:239
                if OO00O000000O00O0O ==str (O00000O0OO0OOO000 ):#line:240
                    OO00O000000O00O0O =str (O00000O0OO0OOO000 ).split ('.')#line:241
                    OO0000O0OOO0OO0OO .append (OO00O000000O00O0O )#line:242
                    O0OOOO000O0OOOO00 =O0OOOO000O0OOOO00 +1 #line:243
            if OO00O000000O00O0O =='con':#line:244
                O0OOOO000O0OOOO00 =O0OOOO000O0OOOO00 +1 #line:245
            if O0OOOO000O0OOOO00 ==0 :#line:246
                OO0000O0OOO0OO0OO .append (OO00O000000O00O0O )#line:247
        for O000O0O0OOOO0O0OO in range (len (O0OOO0OOOOO00O00O )):#line:248
            O0OO0OOO0OO0OO0OO =0 #line:249
            O0OO00O0O0O0O0OO0 =O0OOO0OOOOO00O00O [O000O0O0OOOO0O0OO ]#line:250
            O0OOOOOO00O000OO0 =str (O0OO00O0O0O0O0OO0 ['title']).lower ()#line:251
            O0OOOOOO00O000OO0 =remove_accents (O0OOOOOO00O000OO0 )#line:252
            O0OOOOOO00O000OO0 =O0OOOOOO00O000OO0 .split (' ')#line:253
            for OO00000O0O0OO0O00 ,O00OO0000O00O0O0O in enumerate (O0OOOOOO00O000OO0 ):#line:254
                for O0O00000O0O0O00OO ,O00OO00O0O000OOOO in enumerate (O0OOOOOO00O000OO0 ):#line:255
                    if O0O00000O0O0O00OO !=OO00000O0O0OO0O00 :#line:256
                        if O00OO0000O00O0O0O ==O00OO00O0O000OOOO :#line:257
                            O0OOOOOO00O000OO0 .pop (O0O00000O0O0O00OO )#line:258
            for OO00000O0O0OO0O00 ,O00OO0000O00O0O0O in enumerate (O0OOOOOO00O000OO0 ):#line:259
                for O00000O0OO0OOO000 in range (100 ):#line:260
                    O00000O0OO0OOO000 =O00000O0OO0OOO000 /10 #line:261
                    if O00OO0000O00O0O0O ==str (O00000O0OO0OOO000 ):#line:262
                        O00OO0000O00O0O0O =str (O00000O0OO0OOO000 ).split ('.')#line:263
                        O0OOOOOO00O000OO0 .append (O00OO0000O00O0O0O )#line:264
                for OOOO0OO00O0OOOO00 in OO0000O0OOO0OO0OO :#line:265
                            if OOOO0OO00O0OOOO00 =="maya":#line:266
                                OOOO0OO00O0OOOO00 ="malla"#line:267
                            if OOOO0OO00O0OOOO00 =="pilos"or OOOO0OO00O0OOOO00 =="pilo":#line:268
                                OOOO0OO00O0OOOO00 ="philo"#line:269
                            if OOOO0OO00O0OOOO00 =="filos"or OOOO0OO00O0OOOO00 =="filo":#line:270
                                OOOO0OO00O0OOOO00 ="philo"#line:271
                            if OOOO0OO00O0OOOO00 =="sinces"or OOOO0OO00O0OOOO00 =="sinc":#line:272
                                OOOO0OO00O0OOOO00 ="synthe"#line:273
                            if OOOO0OO00O0OOOO00 =="sintes"or OOOO0OO00O0OOOO00 =="sint":#line:274
                                OOOO0OO00O0OOOO00 ="synthe"#line:275
                            if OOOO0OO00O0OOOO00 =="axos"or OOOO0OO00O0OOOO00 =="axo":#line:276
                                OOOO0OO00O0OOOO00 ="axso"#line:277
                            if OOOO0OO00O0OOOO00 =="uno":#line:278
                                OOOO0OO00O0OOOO00 =1 #line:279
                            if OOOO0OO00O0OOOO00 =="dos"or OOOO0OO00O0OOOO00 =="do":#line:280
                                OOOO0OO00O0OOOO00 =2 #line:281
                            if OOOO0OO00O0OOOO00 =="tres"or OOOO0OO00O0OOOO00 =="tr":#line:282
                                OOOO0OO00O0OOOO00 =3 #line:283
                            if OOOO0OO00O0OOOO00 =="cuatro":#line:284
                                OOOO0OO00O0OOOO00 =4 #line:285
                            if OOOO0OO00O0OOOO00 =="cinco":#line:286
                                OOOO0OO00O0OOOO00 =5 #line:287
                            if OOOO0OO00O0OOOO00 =="seis"or OOOO0OO00O0OOOO00 =="sei":#line:288
                                OOOO0OO00O0OOOO00 =6 #line:289
                            if OOOO0OO00O0OOOO00 =="siete":#line:290
                                OOOO0OO00O0OOOO00 =7 #line:291
                            if OOOO0OO00O0OOOO00 =="ocho":#line:292
                                OOOO0OO00O0OOOO00 =8 #line:293
                            if OOOO0OO00O0OOOO00 =="nueve":#line:294
                                OOOO0OO00O0OOOO00 =9 #line:295
                            if OOOO0OO00O0OOOO00 =="cero":#line:296
                                OOOO0OO00O0OOOO00 =0 #line:297
                            if OOOO0OO00O0OOOO00 =="veintiuno":#line:298
                                OOOO0OO00O0OOOO00 ="21"#line:299
                            if OOOO0OO00O0OOOO00 =="veinte":#line:300
                                OOOO0OO00O0OOOO00 ="20"#line:301
                            if OOOO0OO00O0OOOO00 =="veintidos"or OOOO0OO00O0OOOO00 =="veintido":#line:302
                                OOOO0OO00O0OOOO00 ="22"#line:303
                            if OOOO0OO00O0OOOO00 =="veintitres"or OOOO0OO00O0OOOO00 =="veintitre":#line:304
                                OOOO0OO00O0OOOO00 ="23"#line:305
                            if OOOO0OO00O0OOOO00 =="veinticuatro":#line:306
                                OOOO0OO00O0OOOO00 ="24"#line:307
                            if OOOO0OO00O0OOOO00 =="veinticinco":#line:308
                                OOOO0OO00O0OOOO00 ="25"#line:309
                            if OOOO0OO00O0OOOO00 =="veintiseis"or OOOO0OO00O0OOOO00 =="veintisei":#line:310
                                OOOO0OO00O0OOOO00 ="26"#line:311
                            if OOOO0OO00O0OOOO00 =="veintisiete":#line:312
                                OOOO0OO00O0OOOO00 ="27"#line:313
                            if OOOO0OO00O0OOOO00 =="veintiocho":#line:314
                                OOOO0OO00O0OOOO00 ="28"#line:315
                            if OOOO0OO00O0OOOO00 =="veintinueve":#line:316
                                OOOO0OO00O0OOOO00 ="29"#line:317
                            if OOOO0OO00O0OOOO00 =="treinta":#line:318
                                OOOO0OO00O0OOOO00 ="30"#line:319
                            if type (OOOO0OO00O0OOOO00 )==int and type (O000000OOOOOOO0OO )==int :#line:320
                                O00000O0OO0OOO000 =str (O000000OOOOOOO0OO )+'.'+str (OOOO0OO00O0OOOO00 )#line:321
                                OOOO0OO00O0OOOO00 =O00000O0OO0OOO000 .split ('.')#line:322
                            O000000OOOOOOO0OO =OOOO0OO00O0OOOO00 #line:323
                            OOOO0OO00O0OOOO00 =inflector .singularize (str (OOOO0OO00O0OOOO00 ))#line:324
                            O00OO0000O00O0O0O =inflector .singularize (str (O00OO0000O00O0O0O ))#line:325
                            OOOO0OO00O0OOOO00 =remove_accents (OOOO0OO00O0OOOO00 )#line:326
                            if O00OO0000O00O0O0O ==OOOO0OO00O0OOOO00 :#line:327
                                O0OO0OOO0OO0OO0OO =O0OO0OOO0OO0OO0OO +1 #line:328
            OOOO0O0OOOOO000O0 [O000O0O0OOOO0O0OO ]=O0OO0OOO0OO0OO0OO #line:329
        O0O0OO0O000OO0O00 =np .argwhere (OOOO0O0OOOOO000O0 ==np .amax (OOOO0O0OOOOO000O0 ))#line:330
        for O000O0O0OOOO0O0OO in O0O0OO0O000OO0O00 :#line:331
            OOOOO0O0O0OO000O0 .append (O0OOO0OOOOO00O00O [int (O000O0O0OOOO0O0OO )])#line:332
        if np .all (OOOO0O0OOOOO000O0 ==0 ):#line:333
            OOOOO0O0O0OO000O0 =None #line:334
    return OOOOO0O0O0OO000O0 #line:335
async def cargar_tipo (O00OOO000OOO000OO ,O0O00OO0O0OOO0OO0 ):#line:337
    OOOO0O0OO00OO0000 =aiohttp .TCPConnector (ssl =True )#line:338
    async with aiohttp .ClientSession (connector =OOOO0O0OO00OO0000 )as O0OOOO0OOO00OO00O :#line:339
        O0000O000OOO00OOO =await O0OOOO0OOO00OO00O .get (f'{base_url}all-content/{O0O00OO0O0OOO0OO0}',auth =auth )#line:340
        O0OOOOO00000OO0OO =await O0000O000OOO00OOO .json ()#line:341
        OOOO0O000O00OO0OO =None #line:342
        O00O0OOO000O0O00O =None #line:343
        for OO0OOO00OO0OOO00O in O0OOOOO00000OO0OO :#line:344
            if O00OOO000OOO000OO ==OO0OOO00OO0OOO00O ["nid"]:#line:345
                OOOO0O000O00OO0OO =OO0OOO00OO0OOO00O ["type"]#line:346
                O00O0OOO000O0O00O =OO0OOO00OO0OOO00O #line:347
                break #line:348
    return O00O0OOO000O0O00O ,OOOO0O000O00OO0OO #line:349
async def cargar_archivo (OOOOO0O000O000OOO ,O0OOO000O0O0O0OO0 ,O00O0O0000O000OOO ):#line:351
    O000O0O0O0OOO0O0O =[]#line:352
    OO00000000OOO0OOO =aiohttp .TCPConnector (ssl =True )#line:353
    async with aiohttp .ClientSession (connector =OO00000000OOO0OOO )as OOOOOOOOOOO0O00OO :#line:354
        OO0OOOOOO0OO00000 =await OOOOOOOOOOO0O00OO .get ('https://orva.tedcas.com/api/'+str (O00O0O0000O000OOO ),auth =auth )#line:355
        OOOOOOO0000O0O000 =await OO0OOOOOO0OO00000 .json ()#line:356
        OOOOOOO0000O0O000 =OOOOOOO0000O0O000 [0 ]#line:357
        OOO000O0OOO00O00O ="field_"+str (OOOOO0O000O000OOO )#line:358
        OOO00O0O00OO0OOO0 =OOOOOOO0000O0O000 [OOO000O0OOO00O00O ]#line:359
        if OOO000O0OOO00O00O =="field_image":#line:360
            OOOOOOO0000O0O000 =OOOOOOO0000O0O000 ['field_image']#line:361
            OOOOOOO0000O0O000 =OOOOOOO0000O0O000 .split (',')#line:362
            OOOOOOO0000O0O000 =[OO00OO0O0O0000OO0 .replace (' ','')for OO00OO0O0O0000OO0 in OOOOOOO0000O0O000 ]#line:363
            for OO0O0OOO0OO0OOO0O in OOOOOOO0000O0O000 :#line:364
                 O000O0O0O0OOO0O0O .append ("https://orva.tedcas.com/"+str (OO0O0OOO0OO0OOO0O ))#line:365
            print (O000O0O0O0OOO0O0O )#line:366
            return O000O0O0O0OOO0O0O #line:367
        if len (OOO00O0O00OO0OOO0 )==0 :#line:368
             O00OOOO00OOO0O000 ="No hay archivos subidos"#line:369
             O000O0O0O0OOO0O0O ="https://quirohelp.onrender.com/especialidad"#line:370
        elif type (OOO00O0O00OO0OOO0 )==str :#line:371
             O000O0O0O0OOO0O0O ="https://orva.tedcas.com/"+str (OOO00O0O00OO0OOO0 )#line:372
             O00OOOO00OOO0O000 =OOO00O0O00OO0OOO0 #line:373
        elif type (OOO00O0O00OO0OOO0 )==list :#line:374
            for OO000O0OOO00O0000 ,O00000000OO0O0O00 in OOO00O0O00OO0OOO0 :#line:375
                O000O0O0O0OOO0O0O [OO000O0OOO00O0000 ]="https://orva.tedcas.com/"+str (O00000000OO0O0O00 )#line:376
                O00OOOO00OOO0O000 =OOO00O0O00OO0OOO0 #line:377
        return O0OOO000O0O0O0OO0 ,O000O0O0O0OOO0O0O ,O00OOOO00OOO0O000 #line:378
async def cargar_archivo_grande (O0OO000O0OO0O0OO0 ,O00O0O0O00O0000O0 ,O0O00O00O000O0OOO ):#line:380
    OO000OO000OO00O00 =aiohttp .TCPConnector (ssl =True )#line:381
    async with aiohttp .ClientSession (connector =OO000OO000OO00O00 )as OO0OOOO00OOO0O00O :#line:382
        OOOO0OOOO00OOOOO0 =await OO0OOOO00OOO0O00O .get ('https://orva.tedcas.com/api/'+str (O0O00O00O000O0OOO ),auth =auth )#line:383
        O00O0OOO0O0O00000 =await OOOO0OOOO00OOOOO0 .json ()#line:384
        O000OOO0OO000OOO0 ={}#line:385
        if O0OO000O0OO0O0OO0 =='title_material':#line:386
            for O0O0O00OOOO000OO0 in O00O0OOO0O0O00000 :#line:387
                  O000OOO0OO000OOO0 [O0O0O00OOOO000OO0 [O0OO000O0OO0O0OO0 ]]=(O0O0O00OOOO000OO0 [O0OO000O0OO0O0OO0 ])#line:388
            return O000OOO0OO000OOO0 ,O00O0O0O00O0000O0 #line:389
        O00O0OOO0O0O00000 =O00O0OOO0O0O00000 [0 ]#line:390
        O00OOOO0000O00000 ="field_"+str (O0OO000O0OO0O0OO0 )#line:391
        O00OOOO0000O00000 =O00O0OOO0O0O00000 [O00OOOO0000O00000 ]#line:392
        if len (O00OOOO0000O00000 )==0 :#line:393
             O000OOO0OO000OOO0 ["No hay archivos"]="https://quirohelp.onrender.com/especialidad"#line:394
        else :#line:395
            for O0O0O00OOOO000OO0 in O00OOOO0000O00000 :#line:396
                O000OOO0OO000OOO0 [O0O0O00OOOO000OO0 ['descripcion']]="https://orva.tedcas.com/"+str (O0O0O00OOOO000OO0 ['url'])#line:397
        return O00O0O0O00O0000O0 ,O000OOO0OO000OOO0 #line:398
async def cargar_caja (O000O0O0O000OOO0O ,OO00O00OOOO000000 ):#line:400
    O00OOO00000OOO0OO ={}#line:401
    O00O00OO0000O0O00 =aiohttp .TCPConnector (ssl =True )#line:402
    async with aiohttp .ClientSession (connector =O00O00OO0000O0O00 )as OO0O0O0O00OOOO00O :#line:403
        OOO000OOOOO00OO00 =await OO0O0O0O00OOOO00O .get (f'{base_url}intervenciones/{O000O0O0O000OOO0O}',auth =auth )#line:404
        O0OO000OOO000OO00 =await OOO000OOOOO00OO00 .json ()#line:405
        O0OO000OOO000OO00 =O0OO000OOO000OO00 [0 ]#line:406
    if 'field_cajas'in O0OO000OOO000OO00 :#line:407
        O0OO000OOO000OO00 =O0OO000OOO000OO00 ['field_cajas']#line:408
        for O00000O0O0O0OOOO0 in O0OO000OOO000OO00 :#line:409
            O00OOO00000OOO0OO [O00000O0O0O0OOOO0 ['id']]=O00000O0O0O0OOOO0 ['caja']#line:410
    else :#line:411
        O00OOO00000OOO0OO [str (O000O0O0O000OOO0O )]="No hay archivos"#line:412
    return O00OOO00000OOO0OO ,OO00O00OOOO000000 #line:413
async def cargar_instrumental (OOOO0OOO0O00OOOO0 ,OOOOOO0OOO0OO0000 ):#line:415
    OOO0OOOOO000O0OOO ={}#line:416
    OO00O00O000O0OO0O =aiohttp .TCPConnector (ssl =True )#line:417
    async with aiohttp .ClientSession (connector =OO00O00O000O0OO0O )as O0O0OOOOOOO00O000 :#line:418
        O0O00O0O00O0OOOO0 =await O0O0OOOOOOO00O000 .get ('https://orva.tedcas.com/api/'+str (OOOOOO0OOO0OO0000 ),auth =auth )#line:419
        OO0O00OOO00OO000O =await O0O00O0O00O0OOOO0 .json ()#line:420
        for O0O00OOOO0000O00O in OO0O00OOO00OO000O :#line:421
         if 'instrumental'in O0O00OOOO0000O00O :#line:422
            for O0OO0000000O000OO in O0O00OOOO0000O00O ['instrumental']:#line:423
                if O0OO0000000O000OO ['id']==OOOO0OOO0O00OOOO0 :#line:424
                    OOO0OOOOO000O0OOO [O0O00OOOO0000O00O ['nid']]=O0O00OOOO0000O00O ['title']#line:425
    return OOO0OOOOO000O0OOO #line:426
async def cargar_botones_pdf_admision ():#line:428
    O00000O00O0O00000 ={}#line:429
    O00OO00O00O0O0OOO ={}#line:430
    O0OO0OO0O0OOOO0OO ={}#line:431
    OO0O00OO0O00O0O00 ={}#line:432
    O0O00O000000O00O0 =aiohttp .TCPConnector (ssl =True )#line:433
    async with aiohttp .ClientSession (connector =O0O00O000000O00O0 )as OO0OOOO0OO0OOO0O0 :#line:434
        OO000O0OOOOOOO000 =await OO0OOOO0OO0OOO0O0 .get ('https://orva.tedcas.com/api/all-content/1621',auth =auth )#line:435
        O0OOO0OOOO000OOOO =await OO000O0OOOOOOO000 .json ()#line:436
        for O00O00000OO0O00O0 in O0OOO0OOOO000OOOO :#line:437
            O000O0O0O0O000000 =await OO0OOOO0OO0OOO0O0 .get ('https://orva.tedcas.com/api/intervenciones/'+str (O00O00000OO0O00O0 ['nid']),auth =auth )#line:438
            O00O00OO0OOOO000O =await O000O0O0O0O000000 .json ()#line:439
            O00O00OO0OOOO000O =O00O00OO0OOOO000O [0 ]#line:440
            OOO000OO00O0OOOOO =O00O00OO0OOOO000O ['field_pdf']#line:441
            OOO000OO00O0OOOOO =OOO000OO00O0OOOOO [0 ]#line:442
            if O00O00OO0OOOO000O ['field_tecnica']=="Mapa de camas":#line:443
                O00000O00O0O00000 [O00O00OO0OOOO000O ['title']]="https://orva.tedcas.com/"+str (OOO000OO00O0OOOOO ['url'])#line:444
            elif O00O00OO0OOOO000O ['field_tecnica']=="Ambulancias":#line:445
                O00OO00O00O0O0OOO [O00O00OO0OOOO000O ['title']]="https://orva.tedcas.com/"+str (OOO000OO00O0OOOOO ['url'])#line:446
            elif O00O00OO0OOOO000O ['field_tecnica']=="Programación quirúrgica":#line:447
                O0OO0OO0O0OOOO0OO [O00O00OO0OOOO000O ['title']]="https://orva.tedcas.com/"+str (OOO000OO00O0OOOOO ['url'])#line:448
            elif O00O00OO0OOOO000O ['field_tecnica']=="Otros":#line:449
                OO0O00OO0O00O0O00 [O00O00OO0OOOO000O ['title']]="https://orva.tedcas.com/"+str (OOO000OO00O0OOOOO ['url'])#line:450
    return O00000O00O0O00000 ,O00OO00O00O0O0OOO ,O0OO0OO0O0OOOO0OO ,OO0O00OO0O00O0O00 #line:451
def remove_accents (OOO000O0O00O0OO00 ):#line:453
    O0OOO00OO0OO0O0O0 =unicodedata .normalize ('NFKD',OOO000O0O00O0OO00 )#line:454
    return u"".join ([OO00000O0OOOOO0OO for OO00000O0OOOOO0OO in O0OOO00OO0OO0O0O0 if not unicodedata .combining (OO00000O0OOOOO0OO )])#line:455
def adaptar_salida (O0OO0OO0OO000O00O ):#line:457
    OOO00O0O0O0OOOOO0 =[]#line:458
    O0OO0OO0OO000O00O =str (O0OO0OO0OO000O00O ).lower ()#line:459
    O0OO0OO0OO000O00O =O0OO0OO0OO000O00O .split ("}")#line:460
    O0OO0OO0OO000O00O =O0OO0OO0OO000O00O [0 ].split (":")#line:461
    if len (O0OO0OO0OO000O00O )>=2 :#line:462
        OOOOO0000OOO0OOO0 =O0OO0OO0OO000O00O [1 ].split ("'")#line:463
        OOO00O0O0O0OOOOO0 =OOOOO0000OOO0OOO0 [1 ].split ()#line:464
    return OOO00O0O0O0OOOOO0 #line:465
def takeCommand ():#line:467
    OOO00OO0OO0O0OO0O =sr .Recognizer ()#line:468
    with sr .Microphone ()as O00OO000O0000OO00 :#line:469
        print ("Listening...")#line:470
        OOO00OO0OO0O0OO0O .pause_threshold =1 #line:471
        O00OOOOOOOOOO0OO0 =OOO00OO0OO0O0OO0O .adjust_for_ambient_noise (O00OO000O0000OO00 )#line:472
        O00OOOOOOOOOO0OO0 =OOO00OO0OO0O0OO0O .listen (O00OO000O0000OO00 )#line:473
    try :#line:474
        print ("Recognizing...")#line:475
        OOOO0OO00O0OO0OO0 =OOO00OO0OO0O0OO0O .recognize_google (O00OOOOOOOOOO0OO0 ,language ='es-ES')#line:476
        print (f"User said: {OOOO0OO00O0OO0OO0}\n")#line:477
    except Exception as O00OO00OOOOO00O0O :#line:478
        print (O00OO00OOOOO00O0O )#line:479
        print ("Unable to Recognize your voice.")#line:480
        return "none"#line:481
    return OOOO0OO00O0OO0OO0 #line:482
app =Flask (__name__ )#line:484
app .config ['SECRET_KEY']='mysecretkey'#line:485
IMG_FOLDER =os .path .join ('static','IMG')#line:487
app .config ['UPLOAD_FOLDER']=IMG_FOLDER #line:488
@app .route ("/")#line:490
async def hello ():#line:491
    OOOOOOO000OO0O00O =os .path .join (app .config ['UPLOAD_FOLDER'],'trauma.jpeg')#line:492
    O00OO0O00OOO000O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'uro.jpeg')#line:493
    O0O0O0OOO0000OOOO =os .path .join (app .config ['UPLOAD_FOLDER'],'adm.jpeg')#line:494
    O0000O0OO0OO0O0O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'tijerass.png')#line:495
    return render_template ('especialidad.html',user_image0 =O0000O0OO0OO0O0O0 ,user_image1 =OOOOOOO000OO0O00O ,user_image2 =O00OO0O00OOO000O0 ,user_image3 =O0O0O0OOO0000OOOO )#line:496
@app .route ("/especialidad")#line:498
async def especialidad ():#line:499
    O0O00OOOOOOOOOOO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'trauma.jpeg')#line:500
    O0OOO000OO0O0000O =os .path .join (app .config ['UPLOAD_FOLDER'],'uro.jpeg')#line:501
    O0O000O00OOOOO0OO =os .path .join (app .config ['UPLOAD_FOLDER'],'adm.jpeg')#line:502
    O0OO00OO0O0OO0OO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'tijerass.png')#line:503
    return render_template ('especialidad.html',user_image0 =O0OO00OO0O0OO0OO0 ,user_image1 =O0O00OOOOOOOOOOO0 ,user_image2 =O0OOO000OO0O0000O ,user_image3 =O0O000O00OOOOO0OO )#line:504
@app .route ("/seleccion_trauma",methods =['GET','POST'])#line:506
async def seleccion_trauma ():#line:507
    OOOO0OOOOOO0OO0O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'lupa.png')#line:508
    OO00O0OO0O000000O =os .path .join (app .config ['UPLOAD_FOLDER'],'micro.png')#line:509
    OO0O0O000O00O0OO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:510
    OOO0000000O00O000 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:511
    return render_template ('seleccion_trauma.html',user_image4 =OOOO0OOOOOO0OO0O0 ,user_image5 =OO00O0OO0O000000O ,user_image6 =OO0O0O000O00O0OO0 ,user_image7 =OOO0000000O00O000 )#line:512
@app .route ("/buscador_trauma",methods =['GET','POST'])#line:514
async def buscador_trauma ():#line:515
    OO00OO0OOO0000O00 =os .path .join (app .config ['UPLOAD_FOLDER'],'lupa.png')#line:516
    O00O0O0000O000OO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'micro.png')#line:517
    O0O0O000O0OO00OOO =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:518
    O00OOOOOO000OOOOO =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:519
    OOO0OOOO000O00OO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'guia_visual.png')#line:520
    O0OO000O0000000O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'materiales.png')#line:521
    O00000O0O0O00OOOO =os .path .join (app .config ['UPLOAD_FOLDER'],'pdf_casa.jpg')#line:522
    OOO0OOO00O0OOO00O =os .path .join (app .config ['UPLOAD_FOLDER'],'protocolo.jpg')#line:523
    O0O000OOOO00OOO00 =os .path .join (app .config ['UPLOAD_FOLDER'],'visualizar_video.png')#line:524
    O0000OOO00OO0OOO0 =str (request .form .to_dict ())#line:525
    O0000OOO00OO0OOO0 =adaptar_salida (O0000OOO00OO0OOO0 )#line:526
    OO00000OO0OO0OOO0 ={}#line:527
    OO00000OO0OO0OOO0 [""]=""#line:528
    if len (O0000OOO00OO0OOO0 )==0 :#line:529
        return render_template ('buscador_trauma.html',result_busqueda =OO00000OO0OO0OOO0 ,user_image4 =OO00OO0OOO0000O00 ,user_image5 =O00O0O0000O000OO0 ,user_image6 =O0O0O000O0OO00OOO ,user_image7 =O00OOOOOO000OOOOO ,user_image8 =O00000O0O0O00OOOO ,user_image9 =OOO0OOO00O0OOO00O ,user_image10 =OOO0OOOO000O00OO0 ,user_image11 =O0O000OOOO00OOO00 ,user_image12 =O0OO000O0000000O0 ,nid2 =0 )#line:530
    elif O0000OOO00OO0OOO0 !=None or "{}":#line:531
        O0O000OOO0OOO00OO =1 #line:532
        O0O000O0O0OO00O0O =await cargar_base_datos (O0000OOO00OO0OOO0 ,O0O000OOO0OOO00OO )#line:533
        O0O00OOO000000O0O =await buscar_faq (O0000OOO00OO0OOO0 ,1 )#line:534
        if O0O000O0O0OO00O0O ==None :#line:535
            if len (O0O00OOO000000O0O )==0 :#line:536
                return render_template ('buscador_trauma.html',result_busqueda =OO00000OO0OO0OOO0 ,prediction_text ="No hay resultados para tu busqueda",user_image4 =OO00OO0OOO0000O00 ,user_image5 =O00O0O0000O000OO0 ,user_image6 =O0O0O000O0OO00OOO ,user_image7 =O00OOOOOO000OOOOO ,user_image8 =O00000O0O0O00OOOO ,user_image9 =OOO0OOO00O0OOO00O ,user_image10 =OOO0OOOO000O00OO0 ,user_image11 =O0O000OOOO00OOO00 ,user_image12 =O0OO000O0000000O0 ,nid2 =0 )#line:537
            else :#line:538
                 return render_template ('buscador_trauma.html',faqs =O0O00OOO000000O0O ,faq_titulo ="Preguntas y respuestas: ",result_busqueda =OO00000OO0OO0OOO0 ,user_image4 =OO00OO0OOO0000O00 ,user_image5 =O00O0O0000O000OO0 ,user_image6 =O0O0O000O0OO00OOO ,user_image7 =O00OOOOOO000OOOOO ,user_image8 =O00000O0O0O00OOOO ,user_image9 =OOO0OOO00O0OOO00O ,user_image10 =OOO0OOOO000O00OO0 ,user_image11 =O0O000OOOO00OOO00 ,user_image12 =O0OO000O0000000O0 ,nid2 =0 )#line:539
        elif len (O0O000O0O0OO00O0O )>=1 :#line:540
            OO00O0OO000OOO00O =[]#line:541
            O0OOO00OOOOO0000O =[]#line:542
            OO00000OO0OO0OOO0 ={}#line:543
            for O0OOO00OO00OO0OO0 in O0O000O0O0OO00O0O :#line:544
                OO00O0OO000OOO00O .append (O0OOO00OO00OO0OO0 ["title"])#line:545
                O0OOO00OOOOO0000O .append (O0OOO00OO00OO0OO0 ["nid"])#line:546
            for O0OO0OO00OOOOOO00 ,O0OOO00OO00OO0OO0 in enumerate (OO00O0OO000OOO00O ):#line:547
                 OO00000OO0OO0OOO0 [O0OOO00OOOOO0000O [O0OO0OO00OOOOOO00 ]]=O0OOO00OO00OO0OO0 #line:548
            if len (O0O00OOO000000O0O )!=0 :#line:550
                return render_template ('buscador_trauma.html',faqs =O0O00OOO000000O0O ,faq_titulo ="Preguntas y respuestas: ",result_busqueda =OO00000OO0OO0OOO0 ,user_image4 =OO00OO0OOO0000O00 ,user_image5 =O00O0O0000O000OO0 ,user_image6 =O0O0O000O0OO00OOO ,user_image7 =O00OOOOOO000OOOOO ,user_image8 =O00000O0O0O00OOOO ,user_image9 =OOO0OOO00O0OOO00O ,user_image10 =OOO0OOOO000O00OO0 ,user_image11 =O0O000OOOO00OOO00 ,user_image12 =O0OO000O0000000O0 ,nid2 =0 )#line:551
            else :#line:552
                return render_template ('buscador_trauma.html',result_busqueda =OO00000OO0OO0OOO0 ,user_image4 =OO00OO0OOO0000O00 ,user_image5 =O00O0O0000O000OO0 ,user_image6 =O0O0O000O0OO00OOO ,user_image7 =O00OOOOOO000OOOOO ,user_image8 =O00000O0O0O00OOOO ,user_image9 =OOO0OOO00O0OOO00O ,user_image10 =OOO0OOOO000O00OO0 ,user_image11 =O0O000OOOO00OOO00 ,user_image12 =O0OO000O0000000O0 ,nid2 =0 )#line:553
@app .route ("/resultado_trauma",methods =['GET','POST'])#line:555
async def resultado_trauma ():#line:556
    OO0OO0O0OO0O00O00 =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:557
    OOOOO0000OO0O000O =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:558
    O00OO0OO00OO0O000 =os .path .join (app .config ['UPLOAD_FOLDER'],'guia_visual.png')#line:559
    O00O000OO0O0000O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'materiales.png')#line:560
    OOOO0OO0OO000O000 =os .path .join (app .config ['UPLOAD_FOLDER'],'pdf_casa.jpg')#line:561
    O000O0O0000O0O000 =os .path .join (app .config ['UPLOAD_FOLDER'],'protocolo.jpg')#line:562
    OOOO00OO000OOO0OO =os .path .join (app .config ['UPLOAD_FOLDER'],'visualizar_video.png')#line:563
    OO0O0OOO00OOO0OOO =request .args .get ('link')#line:564
    OOO0OO00O000O0OO0 ,OO0OOOOOO0000O0OO =await cargar_tipo (OO0O0OOO00OOO0OOO ,1 )#line:565
    O0O00O0O0OOO00O0O =OOO0OO00O000O0OO0 ['title']#line:566
    if OO0OOOOOO0000O0OO =="Intervencion":#line:568
        OO0O00OO0O0O0O0O0 ,OOO0OO0OO0O00OO00 =await cargar_caja (str (OO0O0OOO00OOO0OOO ),'Materiales - Cajas: ')#line:569
        return render_template ('intervencion_trauma.html',user_image8 =OOOO0OO0OO000O000 ,user_image9 =O000O0O0000O0O000 ,user_image10 =O00OO0OO00OO0O000 ,user_image11 =OOOO00OO000OOO0OO ,user_image12 =O00O000OO0O0000O0 ,instrumental =OO0O00OO0O0O0O0O0 ,texto_cajas =OOO0OO0OO0O00OO00 ,title =O0O00O0O0OOO00O0O ,user_image6 =OO0OO0O0OO0O00O00 ,user_image7 =OOOOO0000OO0O000O ,nid2 =OO0O0OOO00OOO0OOO )#line:570
    elif OO0OOOOOO0000O0OO =='Caja':#line:571
        O0OOOO0O000O0O00O ,OOOOO00O0OOOO00OO ,O000O0O000O00OO0O =await cargar_archivo ("ubicacion","Ubicacion: ","cajas/"+str (OO0O0OOO00OOO0OOO ))#line:572
        O0OOO00O0OOO00OO0 =await cargar_archivo ("image","Imagen: ","cajas/"+str (OO0O0OOO00OOO0OOO ))#line:573
        OO0000OO0O0O00000 ,OO00O0O000O0OO0O0 =await cargar_archivo_grande ("title_material","Material : ","cajas/"+str (OO0O0OOO00OOO0OOO ))#line:574
        return render_template ('caja_trauma.html',title =O0O00O0O0OOO00O0O ,files_instru =OO0000OO0O0O00000 ,texto_instru =OO00O0O000O0OO0O0 ,texto_ubi =O0OOOO0O000O0O00O ,file_texto_ubi =O000O0O000O00OO0O ,file_imagen =O0OOO00O0OOO00OO0 ,user_image6 =OO0OO0O0OO0O00O00 ,user_image7 =OOOOO0000OO0O000O )#line:575
    elif OO0OOOOOO0000O0OO =='Instrumental':#line:576
        OOO0OOOO0OOOOOO00 =await cargar_instrumental (OO0O0OOO00OOO0OOO ,'listado_completo_cajas/1')#line:577
        return render_template ('instrumental_trauma.html',cajas =OOO0OOOO0OOOOOO00 ,texto ='El instrumental que buscas esta presente en las siguientes cajas: ',title =O0O00O0O0OOO00O0O ,user_image6 =OO0OO0O0OO0O00O00 ,user_image7 =OOOOO0000OO0O000O )#line:578
@app .route ("/protocolos_trauma",methods =['GET','POST'])#line:580
async def protocolos_trauma ():#line:581
    OO00OO0O0OO00O00O =request .args .get ('link2')#line:582
    OO00OOOOO0OOO0OO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:583
    OOOO0000O0OO00O0O =await boton_word_ppt (1 ,"field_protocolo",OO00OO0O0OO00O00O )#line:584
    return render_template ('protocolo.html',protocolos =OOOO0000O0OO00O0O ,user_image7 =OO00OOOOO0OOO0OO0 )#line:585
@app .route ("/guia_visual_trauma",methods =['GET','POST'])#line:587
async def guia_visual_trauma ():#line:588
    O000O0OOO000O000O =request .args .get ('link2')#line:589
    O0O000OO000O00000 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:590
    OO00O0OO00O0O0OOO =await boton_word_ppt (1 ,"field_guia_visual",O000O0OOO000O000O )#line:591
    return render_template ('guia_visual.html',guia_visual =OO00O0OO00O0O0OOO ,user_image7 =O0O000OO000O00000 )#line:592
@app .route ("/pdf_casa_trauma",methods =['GET','POST'])#line:594
async def pdf_casa_trauma ():#line:595
    O0O0O00OOO0O000O0 =request .args .get ('link2')#line:596
    O00O0O000O00O00O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:597
    O00OOO0O00OOOO00O =await boton_pdf_video (1 ,"field_pdf",O0O0O00OOO0O000O0 )#line:598
    return render_template ('pdf_casa_comercial.html',user_image7 =O00O0O000O00O00O0 ,titulos =O00OOO0O00OOOO00O )#line:599
@app .route ("/videos_trauma",methods =['GET','POST'])#line:601
async def videos_trauma ():#line:602
    O0000000000O0OOOO =request .args .get ('link2')#line:603
    OOO0O0O0OOO000OOO =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:604
    OOO00O00000OOOO00 =await boton_pdf_video (1 ,"field_video",O0000000000O0OOOO )#line:605
    return render_template ('videos.html',user_image7 =OOO0O0O0OOO000OOO ,titulos =OOO00O00000OOOO00 )#line:606
@app .route ("/materiales_trauma",methods =['GET','POST'])#line:608
async def materiales_trauma ():#line:609
    OOOOO0OO00000O00O =request .args .get ('link2')#line:610
    OOO000O0OO000O0OO =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:611
    O0000OOO0OO000OO0 =await boton_materiales (1 ,OOOOO0OO00000O00O )#line:612
    if len (O0000OOO0OO000OO0 [''])==0 :#line:613
       return render_template ('materiales.html',user_image7 =OOO000O0OO000O0OO ,cajas =O0000OOO0OO000OO0 ,no_hay ="No hay materiales")#line:614
    return render_template ('materiales.html',user_image7 =OOO000O0OO000O0OO ,cajas =O0000OOO0OO000OO0 )#line:615
@app .route ("/escuchar_trauma1",methods =['GET','POST'])#line:617
async def escuchar_trauma1 ():#line:618
    OOOO000OO00OOO00O =os .path .join (app .config ['UPLOAD_FOLDER'],'guia_visual.png')#line:619
    OOO00O00O000O0OOO =os .path .join (app .config ['UPLOAD_FOLDER'],'materiales.png')#line:620
    OO0OO0000O00OOOOO =os .path .join (app .config ['UPLOAD_FOLDER'],'pdf_casa.jpg')#line:621
    OO00O00000OO0O00O =os .path .join (app .config ['UPLOAD_FOLDER'],'protocolo.jpg')#line:622
    O0O0O000O0O000OO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'visualizar_video.png')#line:623
    O00OO00OO0OO00O0O =os .path .join (app .config ['UPLOAD_FOLDER'],'micro.png')#line:624
    O0OOO000OO0OO00O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:625
    OOOOOO0OO0O000O0O =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:626
    return render_template ('escuchar_trauma1.html',nid2 =0 ,prediction_text ="Dale a `Escuchar´ y haz tu pregunta",user_image5 =O00OO00OO0OO00O0O ,user_image6 =O0OOO000OO0OO00O0 ,user_image7 =OOOOOO0OO0O000O0O ,user_image8 =OO0OO0000O00OOOOO ,user_image9 =OO00O00000OO0O00O ,user_image10 =OOOO000OO00OOO00O ,user_image11 =O0O0O000O0O000OO0 ,user_image12 =OOO00O00O000O0OOO )#line:627
@app .route ("/escuchar_trauma",methods =['GET','POST'])#line:629
async def escuchar_trauma ():#line:630
    OO00OOOOO00OO00O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'guia_visual.png')#line:631
    O00OOOOOOO0000OO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'materiales.png')#line:632
    O00000OO00OO0OO00 =os .path .join (app .config ['UPLOAD_FOLDER'],'pdf_casa.jpg')#line:633
    OOOOO0OO00000000O =os .path .join (app .config ['UPLOAD_FOLDER'],'protocolo.jpg')#line:634
    OOOOOOOO0O0O0OOOO =os .path .join (app .config ['UPLOAD_FOLDER'],'visualizar_video.png')#line:635
    OOO0O00O0OOO00O00 =os .path .join (app .config ['UPLOAD_FOLDER'],'micro.png')#line:636
    OO0OOOOOO0000000O =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:637
    OO0O0OO0O0O0OOOO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:638
    O0O0000OOOOOO00OO =takeCommand ()#line:639
    O0O0000OOOOOO00OO =str (O0O0000OOOOOO00OO ).lower ()#line:640
    O0O0000OOOOOO00OO =O0O0000OOOOOO00OO .split ()#line:641
    OOO000OOO0OO0000O ={}#line:642
    OOO000OOO0OO0000O [""]=""#line:643
    if O0O0000OOOOOO00OO [0 ]!="none":#line:644
        O0000O0O0O00OOO0O =1 #line:645
        O0000000O00OO00O0 =await cargar_base_datos (O0O0000OOOOOO00OO ,O0000O0O0O00OOO0O )#line:646
        O0O00OOO0O000O00O =await buscar_faq (O0O0000OOOOOO00OO ,0 )#line:647
        if O0000000O00OO00O0 ==None :#line:648
            if len (O0O00OOO0O000O00O )==0 :#line:649
                return render_template ('escuchar_trauma.html',nid2 =0 ,result_busqueda =OOO000OOO0OO0000O ,prediction_text ="No hay resultados para tu busqueda",user_image6 =OO0OOOOOO0000000O ,user_image7 =OO0O0OO0O0O0OOOO0 ,user_image5 =OOO0O00O0OOO00O00 ,user_image8 =O00000OO00OO0OO00 ,user_image9 =OOOOO0OO00000000O ,user_image10 =OO00OOOOO00OO00O0 ,user_image11 =OOOOOOOO0O0O0OOOO ,user_image12 =O00OOOOOOO0000OO0 )#line:650
            else :#line:651
                return render_template ('escuchar_trauma.html',nid2 =0 ,faqs =O0O00OOO0O000O00O ,faq_titulo ="Preguntas y respuestas: ",result_busqueda =OOO000OOO0OO0000O ,user_image6 =OO0OOOOOO0000000O ,user_image7 =OO0O0OO0O0O0OOOO0 ,user_image5 =OOO0O00O0OOO00O00 ,user_image8 =O00000OO00OO0OO00 ,user_image9 =OOOOO0OO00000000O ,user_image10 =OO00OOOOO00OO00O0 ,user_image11 =OOOOOOOO0O0O0OOOO ,user_image12 =O00OOOOOOO0000OO0 )#line:652
        elif len (O0000000O00OO00O0 )>=1 :#line:653
            OOOO0O000OOO00OOO =[]#line:654
            O0O000O0O0OOO0OO0 =[]#line:655
            OOO000OOO0OO0000O ={}#line:656
            for O0O0OO0OOOO000OO0 in O0000000O00OO00O0 :#line:657
                OOOO0O000OOO00OOO .append (O0O0OO0OOOO000OO0 ["title"])#line:658
                O0O000O0O0OOO0OO0 .append (O0O0OO0OOOO000OO0 ["nid"])#line:659
            for OOO00OOO00O0O0OO0 ,O0O0OO0OOOO000OO0 in enumerate (OOOO0O000OOO00OOO ):#line:660
                 OOO000OOO0OO0000O [O0O000O0O0OOO0OO0 [OOO00OOO00O0O0OO0 ]]=O0O0OO0OOOO000OO0 #line:661
            if len (O0O00OOO0O000O00O )==0 :#line:663
                return render_template ('escuchar_trauma.html',nid2 =0 ,result_busqueda =OOO000OOO0OO0000O ,user_image6 =OO0OOOOOO0000000O ,user_image7 =OO0O0OO0O0O0OOOO0 ,user_image5 =OOO0O00O0OOO00O00 ,user_image8 =O00000OO00OO0OO00 ,user_image9 =OOOOO0OO00000000O ,user_image10 =OO00OOOOO00OO00O0 ,user_image11 =OOOOOOOO0O0O0OOOO ,user_image12 =O00OOOOOOO0000OO0 )#line:664
            else :#line:665
                return render_template ('escuchar_trauma.html',nid2 =0 ,faqs =O0O00OOO0O000O00O ,faq_titulo ="Preguntas y respuestas: ",result_busqueda =OOO000OOO0OO0000O ,user_image6 =OO0OOOOOO0000000O ,user_image7 =OO0O0OO0O0O0OOOO0 ,user_image5 =OOO0O00O0OOO00O00 ,user_image8 =O00000OO00OO0OO00 ,user_image9 =OOOOO0OO00000000O ,user_image10 =OO00OOOOO00OO00O0 ,user_image11 =OOOOOOOO0O0O0OOOO ,user_image12 =O00OOOOOOO0000OO0 )#line:666
    else :#line:667
        return render_template ('escuchar_trauma.html',nid2 =0 ,result_busqueda =OOO000OOO0OO0000O ,prediction_text ="No te he entendido bien, dale al boton `Escuchar´ y repite tu pregunta",user_image5 =OOO0O00O0OOO00O00 ,user_image6 =OO0OOOOOO0000000O ,user_image7 =OO0O0OO0O0O0OOOO0 ,user_image8 =O00000OO00OO0OO00 ,user_image9 =OOOOO0OO00000000O ,user_image10 =OO00OOOOO00OO00O0 ,user_image11 =OOOOOOOO0O0O0OOOO ,user_image12 =O00OOOOOOO0000OO0 )#line:668
@app .route ("/buscador_admision",methods =['GET','POST'])#line:670
async def buscador_admision ():#line:671
    OO00O0O0O000O00OO =os .path .join (app .config ['UPLOAD_FOLDER'],'lupa.png')#line:672
    O00O000O00OO0OOO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'micro.png')#line:673
    O0OOO00OO000OOOO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:674
    OO0OO0OO00O0O0OOO =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:675
    OOOOO00OOOO0O0O00 =os .path .join (app .config ['UPLOAD_FOLDER'],'otros_img.png')#line:676
    O00O000OO000OO0OO =os .path .join (app .config ['UPLOAD_FOLDER'],'programacion_img.png')#line:677
    OOO0OOO0OOOOOO0OO =os .path .join (app .config ['UPLOAD_FOLDER'],'ambulancias_img.jpg')#line:678
    OO00OO0O0O0OOO0O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'mapa_camas_img.jpg')#line:679
    OOOOOOO0O0OOOOOOO =str (request .form .to_dict ())#line:680
    OOOOOOO0O0OOOOOOO =adaptar_salida (OOOOOOO0O0OOOOOOO )#line:681
    O0OO0O0OOO00OOO0O ={}#line:682
    O0OO0O0OOO00OOO0O [""]=""#line:683
    if len (OOOOOOO0O0OOOOOOO )==0 :#line:684
        return render_template ('buscador_admision.html',user_image8 =OO00OO0O0O0OOO0O0 ,user_image9 =OOO0OOO0OOOOOO0OO ,user_image10 =O00O000OO000OO0OO ,user_image11 =OOOOO00OOOO0O0O00 ,result_busqueda =O0OO0O0OOO00OOO0O ,prediction_text ="ya puedes hacer tu pregunta",user_image4 =OO00O0O0O000O00OO ,user_image5 =O00O000O00OO0OOO0 ,user_image6 =O0OOO00OO000OOOO0 ,user_image7 =OO0OO0OO00O0O0OOO )#line:685
    elif OOOOOOO0O0OOOOOOO !=None or "{}":#line:686
        OOOOO0O00O0O0OO0O =1621 #line:687
        OO00OO000O00O0O0O =await cargar_base_datos (OOOOOOO0O0OOOOOOO ,OOOOO0O00O0O0OO0O )#line:688
        O00O00000000O00OO =await buscar_faq (OOOOOOO0O0OOOOOOO ,1 )#line:689
        if OO00OO000O00O0O0O ==None :#line:690
            if len (O00O00000000O00OO )==0 :#line:691
                return render_template ('buscador_admision.html',user_image8 =OO00OO0O0O0OOO0O0 ,user_image9 =OOO0OOO0OOOOOO0OO ,user_image10 =O00O000OO000OO0OO ,user_image11 =OOOOO00OOOO0O0O00 ,result_busqueda =O0OO0O0OOO00OOO0O ,prediction_text ="No hay resultados para tu busqueda",user_image4 =OO00O0O0O000O00OO ,user_image5 =O00O000O00OO0OOO0 ,user_image6 =O0OOO00OO000OOOO0 ,user_image7 =OO0OO0OO00O0O0OOO )#line:692
            else :#line:693
                return render_template ('buscador_admision.html',user_image8 =OO00OO0O0O0OOO0O0 ,user_image9 =OOO0OOO0OOOOOO0OO ,user_image10 =O00O000OO000OO0OO ,user_image11 =OOOOO00OOOO0O0O00 ,faqs =O00O00000000O00OO ,faq_titulo ="Preguntas y respuestas: ",result_busqueda =O0OO0O0OOO00OOO0O ,user_image4 =OO00O0O0O000O00OO ,user_image5 =O00O000O00OO0OOO0 ,user_image6 =O0OOO00OO000OOOO0 ,user_image7 =OO0OO0OO00O0O0OOO )#line:694
        elif len (OO00OO000O00O0O0O )>=1 :#line:695
            OOOO0OOO0O0O0O0OO =[]#line:696
            OOOO000O00000OO0O =[]#line:697
            O0OO0O0OOO00OOO0O ={}#line:698
            for O00OOOOOOOOO00O0O in OO00OO000O00O0O0O :#line:699
                OOOO000O00000OO0O .append (O00OOOOOOOOO00O0O ["nid"])#line:700
                for O0O00OOOO00O00000 in OOOO000O00000OO0O :#line:701
                    O000OO00OOO00O0O0 =aiohttp .TCPConnector (ssl =True )#line:702
                    async with aiohttp .ClientSession (connector =O000OO00OOO00O0O0 )as OO00O000O0O0O000O :#line:703
                        O000OO0O00OO0O00O =await OO00O000O0O0O000O .get ('https://orva.tedcas.com/api/intervenciones/'+str (O0O00OOOO00O00000 ),auth =auth )#line:704
                        O0000OO00OO0OO000 =await O000OO0O00OO0O00O .json ()#line:705
                        O0000OO00OO0OO000 =O0000OO00OO0OO000 [0 ]#line:706
                        OO00000OO000OOOOO =O0000OO00OO0OO000 ['field_pdf']#line:707
                        OO00000OO000OOOOO =OO00000OO000OOOOO [0 ]#line:708
                        O0OO0O0OOO00OOO0O [O0000OO00OO0OO000 ['title']]="https://orva.tedcas.com/"+str (OO00000OO000OOOOO ['url'])#line:709
            if len (O00O00000000O00OO )==0 :#line:710
                return render_template ('buscador_admision.html',user_image8 =OO00OO0O0O0OOO0O0 ,user_image9 =OOO0OOO0OOOOOO0OO ,user_image10 =O00O000OO000OO0OO ,user_image11 =OOOOO00OOOO0O0O00 ,result_busqueda =O0OO0O0OOO00OOO0O ,user_image4 =OO00O0O0O000O00OO ,user_image5 =O00O000O00OO0OOO0 ,user_image6 =O0OOO00OO000OOOO0 ,user_image7 =OO0OO0OO00O0O0OOO )#line:711
            else :#line:712
                return render_template ('buscador_admision.html',faqs =O00O00000000O00OO ,faq_titulo ="Preguntas y respuestas: ",user_image8 =OO00OO0O0O0OOO0O0 ,user_image9 =OOO0OOO0OOOOOO0OO ,user_image10 =O00O000OO000OO0OO ,user_image11 =OOOOO00OOOO0O0O00 ,result_busqueda =O0OO0O0OOO00OOO0O ,user_image4 =OO00O0O0O000O00OO ,user_image5 =O00O000O00OO0OOO0 ,user_image6 =O0OOO00OO000OOOO0 ,user_image7 =OO0OO0OO00O0O0OOO )#line:713
@app .route ("/mapa_camas",methods =['GET','POST'])#line:715
async def mapa_camas ():#line:716
    OOO00OOOO00OOOO00 =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:717
    O00OOOOO000O00OOO =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:718
    OOOO0O0O00OOO0O00 ,OO00OOO000O0OOOOO ,O0OO00OO000O000O0 ,O0OOO0O0O00O00O0O =await cargar_botones_pdf_admision ()#line:719
    return render_template ('mapa_camas.html',text =OOOO0O0O00OOO0O00 ,user_image6 =OOO00OOOO00OOOO00 ,user_image7 =O00OOOOO000O00OOO )#line:720
@app .route ("/ambulancias",methods =['GET','POST'])#line:722
async def ambulancias ():#line:723
    OO0O00O0OOOOO000O =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:724
    O0O0OO00O0O0O000O =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:725
    O0O00O0000OOOOOO0 ,O00OO00OOO0000O0O ,O0OOO0OO0OOOO00OO ,OOOOO0000OO00000O =await cargar_botones_pdf_admision ()#line:726
    return render_template ('ambulancias.html',text =O00OO00OOO0000O0O ,user_image6 =OO0O00O0OOOOO000O ,user_image7 =O0O0OO00O0O0O000O )#line:727
@app .route ("/programacion_quirurgica",methods =['GET','POST'])#line:729
async def programacion_quirurgica ():#line:730
    OOOO000000O000000 =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:731
    O0OOOOO00O000O0OO =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:732
    O000OOOOOO0OOOOO0 ,O0O00OOO000O00O00 ,O00OOOOO00OOO0O00 ,OO0O0OO0O0OOO0OO0 =await cargar_botones_pdf_admision ()#line:733
    return render_template ('programacion_quirurgica.html',text =O00OOOOO00OOO0O00 ,user_image6 =OOOO000000O000000 ,user_image7 =O0OOOOO00O000O0OO )#line:734
@app .route ("/otros",methods =['GET','POST'])#line:736
async def otros ():#line:737
    OO0O0000O00OO0O0O =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:738
    O0OOOO000O0OO000O =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:739
    OO00OOO0O0OO00OO0 ,OO00OOOO000OO0OOO ,O0OO00O0000OOOO00 ,OOOO0000O0O0OO0O0 =await cargar_botones_pdf_admision ()#line:740
    return render_template ('otros.html',text =OOOO0000O0O0OO0O0 ,user_image6 =OO0O0000O00OO0O0O ,user_image7 =O0OOOO000O0OO000O )#line:741
@app .route ("/escuchar_admision1",methods =['GET','POST'])#line:743
async def escuchar_admision1 ():#line:744
    O000OO000OO00OOOO =os .path .join (app .config ['UPLOAD_FOLDER'],'otros_img.png')#line:745
    OOO0000OO0OO00OO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'programacion_img.png')#line:746
    OO000O00OOO0000O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'ambulancias_img.jpg')#line:747
    OOOOO000OOO0OO000 =os .path .join (app .config ['UPLOAD_FOLDER'],'mapa_camas_img.jpg')#line:748
    O0O0OOO000OO00OO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'micro.png')#line:749
    OO000OOOOOO00OOO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:750
    OO000OOOOOOOOOO0O =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:751
    return render_template ('escuchar_admision1.html',user_image8 =OOOOO000OOO0OO000 ,user_image9 =OO000O00OOO0000O0 ,user_image10 =OOO0000OO0OO00OO0 ,user_image11 =O000OO000OO00OOOO ,prediction_text ="Dale a `Escuchar´ y haz tu pregunta",user_image5 =O0O0OOO000OO00OO0 ,user_image6 =OO000OOOOOO00OOO0 ,user_image7 =OO000OOOOOOOOOO0O )#line:752
@app .route ("/escuchar_admision",methods =['GET','POST'])#line:754
async def escuchar_admision ():#line:755
    OO0O0O00O0000O00O =os .path .join (app .config ['UPLOAD_FOLDER'],'otros_img.png')#line:756
    O0O0O0OOOO00OO0O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'programacion_img.png')#line:757
    OO00O0O00O0OOOO0O =os .path .join (app .config ['UPLOAD_FOLDER'],'ambulancias_img.jpg')#line:758
    OO0OOOOOO000OOOO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'mapa_camas_img.jpg')#line:759
    OOO000O0000O00O0O =os .path .join (app .config ['UPLOAD_FOLDER'],'lupa.png')#line:760
    OOOO0OOO0OO00000O =os .path .join (app .config ['UPLOAD_FOLDER'],'micro.png')#line:761
    O000O0OOO00O0O00O =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:762
    OOOOO00OOO0000O0O =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:763
    O000O00OO0O000OOO =takeCommand ()#line:764
    O000O00OO0O000OOO =str (O000O00OO0O000OOO ).lower ()#line:765
    O000O00OO0O000OOO =O000O00OO0O000OOO .split ()#line:766
    OOOOO0OOO000OO00O ={}#line:767
    OOOOO0OOO000OO00O [""]=""#line:768
    if O000O00OO0O000OOO [0 ]!="none":#line:769
        O00OO0OO0000OO0OO =1621 #line:770
        O00OOOO0000O0000O =await cargar_base_datos (O000O00OO0O000OOO ,O00OO0OO0000OO0OO )#line:771
        OOO000O00O0OOOO00 =await buscar_faq (O000O00OO0O000OOO ,0 )#line:772
        if O00OOOO0000O0000O ==None :#line:773
            if len (OOO000O00O0OOOO00 )==0 :#line:774
                return render_template ('escuchar_admision.html',user_image8 =OO0OOOOOO000OOOO0 ,user_image9 =OO00O0O00O0OOOO0O ,user_image10 =O0O0O0OOOO00OO0O0 ,user_image11 =OO0O0O00O0000O00O ,result_busqueda =OOOOO0OOO000OO00O ,prediction_text ="No hay resultados para tu busqueda",user_image4 =OOO000O0000O00O0O ,user_image5 =OOOO0OOO0OO00000O ,user_image6 =O000O0OOO00O0O00O ,user_image7 =OOOOO00OOO0000O0O )#line:775
            else :#line:776
                return render_template ('escuchar_admision.html',faqs =OOO000O00O0OOOO00 ,faq_titulo ="Preguntas y respuestas: ",user_image8 =OO0OOOOOO000OOOO0 ,user_image9 =OO00O0O00O0OOOO0O ,user_image10 =O0O0O0OOOO00OO0O0 ,user_image11 =OO0O0O00O0000O00O ,result_busqueda =OOOOO0OOO000OO00O ,user_image4 =OOO000O0000O00O0O ,user_image5 =OOOO0OOO0OO00000O ,user_image6 =O000O0OOO00O0O00O ,user_image7 =OOOOO00OOO0000O0O )#line:777
        elif len (O00OOOO0000O0000O )>=1 :#line:778
            OO0OOO0OO0O00O0O0 =[]#line:779
            OOO00O00OO0O00O0O =[]#line:780
            OOOOO0OOO000OO00O ={}#line:781
            for O000O0OO0OOOOO0O0 in O00OOOO0000O0000O :#line:782
                OOO00O00OO0O00O0O .append (O000O0OO0OOOOO0O0 ["nid"])#line:783
                for OOO00O0OO0OOOOOO0 in OOO00O00OO0O00O0O :#line:784
                    O0OOOOO0O00OOO0O0 =aiohttp .TCPConnector (ssl =True )#line:785
                    async with aiohttp .ClientSession (connector =O0OOOOO0O00OOO0O0 )as OOOOO000O0OO0000O :#line:786
                        OO0000000O0000O0O =await OOOOO000O0OO0000O .get ('https://orva.tedcas.com/api/intervenciones/'+str (OOO00O0OO0OOOOOO0 ),auth =auth )#line:787
                        OOOO0OOOO0OO00OOO =await OO0000000O0000O0O .json ()#line:788
                        OOOO0OOOO0OO00OOO =OOOO0OOOO0OO00OOO [0 ]#line:789
                        OO0000O00OO0O0O0O =OOOO0OOOO0OO00OOO ['field_pdf']#line:790
                        OO0000O00OO0O0O0O =OO0000O00OO0O0O0O [0 ]#line:791
                        OOOOO0OOO000OO00O [OOOO0OOOO0OO00OOO ['title']]="https://orva.tedcas.com/"+str (OO0000O00OO0O0O0O ['url'])#line:792
            if len (OOO000O00O0OOOO00 )==0 :#line:793
                return render_template ('escuchar_admision.html',user_image8 =OO0OOOOOO000OOOO0 ,user_image9 =OO00O0O00O0OOOO0O ,user_image10 =O0O0O0OOOO00OO0O0 ,user_image11 =OO0O0O00O0000O00O ,result_busqueda =OOOOO0OOO000OO00O ,user_image4 =OOO000O0000O00O0O ,user_image5 =OOOO0OOO0OO00000O ,user_image6 =O000O0OOO00O0O00O ,user_image7 =OOOOO00OOO0000O0O )#line:794
            else :#line:795
                return render_template ('escuchar_admision.html',faqs =OOO000O00O0OOOO00 ,faq_titulo ="Preguntas y respuestas: ",user_image8 =OO0OOOOOO000OOOO0 ,user_image9 =OO00O0O00O0OOOO0O ,user_image10 =O0O0O0OOOO00OO0O0 ,user_image11 =OO0O0O00O0000O00O ,result_busqueda =OOOOO0OOO000OO00O ,user_image4 =OOO000O0000O00O0O ,user_image5 =OOOO0OOO0OO00000O ,user_image6 =O000O0OOO00O0O00O ,user_image7 =OOOOO00OOO0000O0O )#line:796
    else :#line:797
        return render_template ('escuchar_admision.html',user_image8 =OO0OOOOOO000OOOO0 ,user_image9 =OO00O0O00O0OOOO0O ,user_image10 =O0O0O0OOOO00OO0O0 ,user_image11 =OO0O0O00O0000O00O ,prediction_text ="No te he entendido bien, dale al boton `Escuchar´ y repite tu pregunta",result_busqueda =OOOOO0OOO000OO00O ,user_image4 =OOO000O0000O00O0O ,user_image5 =OOOO0OOO0OO00000O ,user_image6 =O000O0OOO00O0O00O ,user_image7 =OOOOO00OOO0000O0O )#line:798
@app .route ("/buscador_uro",methods =['GET','POST'])#line:800
async def buscador_uro ():#line:801
    O00OO0OO000OOO000 =os .path .join (app .config ['UPLOAD_FOLDER'],'lupa.png')#line:802
    O0OO0OOO00OO0000O =os .path .join (app .config ['UPLOAD_FOLDER'],'micro.png')#line:803
    OOOOO0O00OOOOOO00 =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:804
    O000O0OOOOO00OOO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:805
    OOOO0O0O00O0OOOOO =os .path .join (app .config ['UPLOAD_FOLDER'],'guia_visual.png')#line:806
    OOO00O00OO0OO0O00 =os .path .join (app .config ['UPLOAD_FOLDER'],'materiales.png')#line:807
    O0OOOOO0OOOO00OOO =os .path .join (app .config ['UPLOAD_FOLDER'],'pdf_casa.jpg')#line:808
    OO00OOO00O00O0O0O =os .path .join (app .config ['UPLOAD_FOLDER'],'protocolo.jpg')#line:809
    O00OO0000O00OOO0O =os .path .join (app .config ['UPLOAD_FOLDER'],'visualizar_video.png')#line:810
    OOOO0OO00O00OO0O0 =str (request .form .to_dict ())#line:811
    OOOO0OO00O00OO0O0 =adaptar_salida (OOOO0OO00O00OO0O0 )#line:812
    O00OO0O00OOO0OOO0 ={}#line:813
    O00OO0O00OOO0OOO0 [""]=""#line:814
    if len (OOOO0OO00O00OO0O0 )==0 :#line:815
        return render_template ('buscador_uro.html',result_busqueda =O00OO0O00OOO0OOO0 ,user_image4 =O00OO0OO000OOO000 ,user_image5 =O0OO0OOO00OO0000O ,user_image6 =OOOOO0O00OOOOOO00 ,user_image7 =O000O0OOOOO00OOO0 ,user_image8 =O0OOOOO0OOOO00OOO ,user_image9 =OO00OOO00O00O0O0O ,user_image10 =OOOO0O0O00O0OOOOO ,user_image11 =O00OO0000O00OOO0O ,user_image12 =OOO00O00OO0OO0O00 ,nid2 =0 )#line:816
    elif OOOO0OO00O00OO0O0 !=None or "{}":#line:817
        O00OOO0OOOOOO0O0O =1620 #line:818
        O00OO0000OO0OOO0O =await cargar_base_datos (OOOO0OO00O00OO0O0 ,O00OOO0OOOOOO0O0O )#line:819
        O0OO0OO0OO00OO0OO =await buscar_faq (OOOO0OO00O00OO0O0 ,1 )#line:820
        if O00OO0000OO0OOO0O ==None :#line:821
            if len (O0OO0OO0OO00OO0OO )==0 :#line:822
                return render_template ('buscador_uro.html',result_busqueda =O00OO0O00OOO0OOO0 ,prediction_text ="No hay resultados para tu busqueda",user_image4 =O00OO0OO000OOO000 ,user_image5 =O0OO0OOO00OO0000O ,user_image6 =OOOOO0O00OOOOOO00 ,user_image7 =O000O0OOOOO00OOO0 ,user_image8 =O0OOOOO0OOOO00OOO ,user_image9 =OO00OOO00O00O0O0O ,user_image10 =OOOO0O0O00O0OOOOO ,user_image11 =O00OO0000O00OOO0O ,user_image12 =OOO00O00OO0OO0O00 ,nid2 =0 )#line:823
            else :#line:824
                 return render_template ('buscador_uro.html',faqs =O0OO0OO0OO00OO0OO ,faq_titulo ="Preguntas y respuestas: ",result_busqueda =O00OO0O00OOO0OOO0 ,user_image4 =O00OO0OO000OOO000 ,user_image5 =O0OO0OOO00OO0000O ,user_image6 =OOOOO0O00OOOOOO00 ,user_image7 =O000O0OOOOO00OOO0 ,user_image8 =O0OOOOO0OOOO00OOO ,user_image9 =OO00OOO00O00O0O0O ,user_image10 =OOOO0O0O00O0OOOOO ,user_image11 =O00OO0000O00OOO0O ,user_image12 =OOO00O00OO0OO0O00 ,nid2 =0 )#line:825
        elif len (O00OO0000OO0OOO0O )>=1 :#line:826
            O0OOOOOO0OO0000O0 =[]#line:827
            OOOOOOOOOOOO0O0OO =[]#line:828
            O00OO0O00OOO0OOO0 ={}#line:829
            for OOOOOOOO0O0OOOOO0 in O00OO0000OO0OOO0O :#line:830
                O0OOOOOO0OO0000O0 .append (OOOOOOOO0O0OOOOO0 ["title"])#line:831
                OOOOOOOOOOOO0O0OO .append (OOOOOOOO0O0OOOOO0 ["nid"])#line:832
            for O0OO0OO0O0O000O00 ,OOOOOOOO0O0OOOOO0 in enumerate (O0OOOOOO0OO0000O0 ):#line:833
                 O00OO0O00OOO0OOO0 [OOOOOOOOOOOO0O0OO [O0OO0OO0O0O000O00 ]]=OOOOOOOO0O0OOOOO0 #line:834
            if len (O0OO0OO0OO00OO0OO )!=0 :#line:835
                return render_template ('buscador_uro.html',faqs =O0OO0OO0OO00OO0OO ,faq_titulo ="Preguntas y respuestas: ",result_busqueda =O00OO0O00OOO0OOO0 ,user_image4 =O00OO0OO000OOO000 ,user_image5 =O0OO0OOO00OO0000O ,user_image6 =OOOOO0O00OOOOOO00 ,user_image7 =O000O0OOOOO00OOO0 ,user_image8 =O0OOOOO0OOOO00OOO ,user_image9 =OO00OOO00O00O0O0O ,user_image10 =OOOO0O0O00O0OOOOO ,user_image11 =O00OO0000O00OOO0O ,user_image12 =OOO00O00OO0OO0O00 ,nid2 =0 )#line:836
            else :#line:837
                return render_template ('buscador_uro.html',result_busqueda =O00OO0O00OOO0OOO0 ,user_image4 =O00OO0OO000OOO000 ,user_image5 =O0OO0OOO00OO0000O ,user_image6 =OOOOO0O00OOOOOO00 ,user_image7 =O000O0OOOOO00OOO0 ,user_image8 =O0OOOOO0OOOO00OOO ,user_image9 =OO00OOO00O00O0O0O ,user_image10 =OOOO0O0O00O0OOOOO ,user_image11 =O00OO0000O00OOO0O ,user_image12 =OOO00O00OO0OO0O00 ,nid2 =0 )#line:838
@app .route ("/resultado_uro",methods =['GET','POST'])#line:840
async def resultado_uro ():#line:841
    O0OOOO00O0OOO0OO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:842
    OO0OO00OO0OOO000O =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:843
    OO00O00OO00O000OO =os .path .join (app .config ['UPLOAD_FOLDER'],'guia_visual.png')#line:844
    O0OO0O00OOOOOOO0O =os .path .join (app .config ['UPLOAD_FOLDER'],'materiales.png')#line:845
    O0OOO0O00O0OO0O0O =os .path .join (app .config ['UPLOAD_FOLDER'],'pdf_casa.jpg')#line:846
    OOO0000O00O0O0O0O =os .path .join (app .config ['UPLOAD_FOLDER'],'protocolo.jpg')#line:847
    O0OO0000O0O000000 =os .path .join (app .config ['UPLOAD_FOLDER'],'visualizar_video.png')#line:848
    OO000000O0OO000O0 =request .args .get ('link')#line:849
    O0OOOOOOO0000OO00 ,O00O0O00OOO0OO000 =await cargar_tipo (OO000000O0OO000O0 ,1620 )#line:850
    OOOO0OO0OOOOOO0OO =O0OOOOOOO0000OO00 ['title']#line:851
    if O00O0O00OOO0OO000 =="Intervencion":#line:852
        print ("hola1")#line:853
        O0OO000OO0O0O0OOO ,OOO0OO0000O0OOO00 =await cargar_caja (str (OO000000O0OO000O0 ),'Materiales - Cajas: ')#line:854
        return render_template ('intervencion_uro.html',user_image8 =O0OOO0O00O0OO0O0O ,user_image9 =OOO0000O00O0O0O0O ,user_image10 =OO00O00OO00O000OO ,user_image11 =O0OO0000O0O000000 ,user_image12 =O0OO0O00OOOOOOO0O ,instrumental =O0OO000OO0O0O0OOO ,texto_cajas =OOO0OO0000O0OOO00 ,title =OOOO0OO0OOOOOO0OO ,user_image6 =O0OOOO00O0OOO0OO0 ,user_image7 =OO0OO00OO0OOO000O ,nid2 =OO000000O0OO000O0 )#line:855
    elif O00O0O00OOO0OO000 =='Caja':#line:856
        OO00OO0O0OOOO00O0 ,O0O00OOO00O0OOO0O ,O0O00000O0OO0O0O0 =await cargar_archivo ("ubicacion","Ubicacion: ","cajas/"+str (OO000000O0OO000O0 ))#line:857
        OOO0OOO000OO0O0O0 =await cargar_archivo ("image","Imagen: ","cajas/"+str (OO000000O0OO000O0 ))#line:858
        OO0OO0OOO0000O00O ,OOO0O000O0O0O000O =await cargar_archivo_grande ("title_material","Material : ","cajas/"+str (OO000000O0OO000O0 ))#line:859
        return render_template ('caja_trauma.html',title =OOOO0OO0OOOOOO0OO ,files_instru =OO0OO0OOO0000O00O ,texto_instru =OOO0O000O0O0O000O ,texto_ubi =OO00OO0O0OOOO00O0 ,file_texto_ubi =O0O00000O0OO0O0O0 ,file_imagen =OOO0OOO000OO0O0O0 ,user_image6 =O0OOOO00O0OOO0OO0 ,user_image7 =OO0OO00OO0OOO000O )#line:860
    elif O00O0O00OOO0OO000 =='Instrumental':#line:861
        print ("hola2")#line:862
        OOO00OO00000OO000 =await cargar_instrumental (OO000000O0OO000O0 ,'listado_completo_cajas/1620')#line:863
        return render_template ('instrumental_uro.html',cajas =OOO00OO00000OO000 ,texto ='El instrumental que buscas esta presente en las siguientes cajas: ',title =OOOO0OO0OOOOOO0OO ,user_image6 =O0OOOO00O0OOO0OO0 ,user_image7 =OO0OO00OO0OOO000O )#line:864
@app .route ("/protocolos_uro",methods =['GET','POST'])#line:866
async def protocolos_uro ():#line:867
    O0OO0O0OOO0OOOO00 =request .args .get ('link2')#line:868
    OO0OOO0O0OOOO0O00 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:869
    OOO0O00O000OOOO00 =await boton_word_ppt (1620 ,"field_protocolo",O0OO0O0OOO0OOOO00 )#line:870
    return render_template ('protocolo.html',protocolos =OOO0O00O000OOOO00 ,user_image7 =OO0OOO0O0OOOO0O00 )#line:871
@app .route ("/guia_visual_uro",methods =['GET','POST'])#line:873
async def guia_visual_uro ():#line:874
    OO0OOOOOOO0OO000O =request .args .get ('link2')#line:875
    O0OO0O00O00OO00OO =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:876
    O0OOO0OOO00O00O00 =await boton_word_ppt (1620 ,"field_guia_visual",OO0OOOOOOO0OO000O )#line:877
    return render_template ('guia_visual.html',guia_visual =O0OOO0OOO00O00O00 ,user_image7 =O0OO0O00O00OO00OO )#line:878
@app .route ("/pdf_casa_uro",methods =['GET','POST'])#line:880
async def pdf_casa_uro ():#line:881
    O00O0OO000OO0000O =request .args .get ('link2')#line:882
    OO00O0OOO00000OO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:883
    OO00000O000OOOO00 =await boton_pdf_video (1620 ,"field_pdf",O00O0OO000OO0000O )#line:884
    return render_template ('pdf_casa_comercial.html',user_image7 =OO00O0OOO00000OO0 ,titulos =OO00000O000OOOO00 )#line:885
@app .route ("/videos_uro",methods =['GET','POST'])#line:887
async def videos_uro ():#line:888
    OO00O0OOO00OO0OOO =request .args .get ('link2')#line:889
    O0OO0OO0O0OOO00O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:890
    O000O00000OOO0OOO =await boton_pdf_video (1620 ,"field_video",OO00O0OOO00OO0OOO )#line:891
    return render_template ('videos.html',user_image7 =O0OO0OO0O0OOO00O0 ,titulos =O000O00000OOO0OOO )#line:892
@app .route ("/materiales_uro",methods =['GET','POST'])#line:894
async def materiales_uro ():#line:895
    O000OO0OO0OOO0O00 =request .args .get ('link2')#line:896
    OOOOO0OO000O0OOOO =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:897
    O000O0O0O0000O0OO =await boton_materiales (1620 ,O000OO0OO0OOO0O00 )#line:898
    if len (O000O0O0O0000O0OO [''])==0 :#line:899
       return render_template ('materiales_uro.html',user_image7 =OOOOO0OO000O0OOOO ,cajas =O000O0O0O0000O0OO ,no_hay ="No hay materiales")#line:900
    return render_template ('materiales_uro.html',user_image7 =OOOOO0OO000O0OOOO ,cajas =O000O0O0O0000O0OO )#line:901
@app .route ("/escuchar_uro1",methods =['GET','POST'])#line:903
async def escuchar_uro1 ():#line:904
    O0OOO0OOO0O000000 =os .path .join (app .config ['UPLOAD_FOLDER'],'guia_visual.png')#line:905
    OO0OO00O00O000OOO =os .path .join (app .config ['UPLOAD_FOLDER'],'materiales.png')#line:906
    OO00O0OOO00OO0000 =os .path .join (app .config ['UPLOAD_FOLDER'],'pdf_casa.jpg')#line:907
    OO0O0OOOO000O0O0O =os .path .join (app .config ['UPLOAD_FOLDER'],'protocolo.jpg')#line:908
    O000O00OO0OOO0O00 =os .path .join (app .config ['UPLOAD_FOLDER'],'visualizar_video.png')#line:909
    O00O00OOOOO0O0OO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'micro.png')#line:910
    O0OO00O0OO00O000O =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:911
    O00OO0O000OOO0O00 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:912
    return render_template ('escuchar_uro1.html',nid2 =0 ,prediction_text ="Dale a `Escuchar´ y haz tu pregunta",user_image5 =O00O00OOOOO0O0OO0 ,user_image6 =O0OO00O0OO00O000O ,user_image7 =O00OO0O000OOO0O00 ,user_image8 =OO00O0OOO00OO0000 ,user_image9 =OO0O0OOOO000O0O0O ,user_image10 =O0OOO0OOO0O000000 ,user_image11 =O000O00OO0OOO0O00 ,user_image12 =OO0OO00O00O000OOO )#line:913
@app .route ("/escuchar_uro",methods =['GET','POST'])#line:915
async def escuchar_uro ():#line:916
    O0OOOOOOOO00000O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'guia_visual.png')#line:917
    O0000O000O0O000O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'materiales.png')#line:918
    O0O000OO00000OO0O =os .path .join (app .config ['UPLOAD_FOLDER'],'pdf_casa.jpg')#line:919
    OOO00000OOO00000O =os .path .join (app .config ['UPLOAD_FOLDER'],'protocolo.jpg')#line:920
    O0O00O0000OOOOO0O =os .path .join (app .config ['UPLOAD_FOLDER'],'visualizar_video.png')#line:921
    O0O0OO000OO000OOO =os .path .join (app .config ['UPLOAD_FOLDER'],'micro.png')#line:922
    OO000O0O00O0O00OO =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:923
    O00OOO0O0O000O0O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:924
    O0O0OOOOO00O0OO00 =takeCommand ()#line:925
    O0O0OOOOO00O0OO00 =str (O0O0OOOOO00O0OO00 ).lower ()#line:926
    O0O0OOOOO00O0OO00 =O0O0OOOOO00O0OO00 .split ()#line:927
    OO0O000O000O0OOOO ={}#line:928
    OO0O000O000O0OOOO [""]=""#line:929
    if O0O0OOOOO00O0OO00 [0 ]!="none":#line:930
        O000OOO0OO0O0O000 =1620 #line:931
        O00OO00O000O0OOO0 =await cargar_base_datos (O0O0OOOOO00O0OO00 ,O000OOO0OO0O0O000 )#line:932
        O00O0O0OO00000OOO =await buscar_faq (O0O0OOOOO00O0OO00 ,0 )#line:933
        if O00OO00O000O0OOO0 ==None :#line:934
            if len (O00O0O0OO00000OOO )==0 :#line:935
                return render_template ('escuchar_uro.html',nid2 =0 ,result_busqueda =OO0O000O000O0OOOO ,prediction_text ="No hay resultados para tu busqueda",user_image6 =OO000O0O00O0O00OO ,user_image7 =O00OOO0O0O000O0O0 ,user_image5 =O0O0OO000OO000OOO ,user_image8 =O0O000OO00000OO0O ,user_image9 =OOO00000OOO00000O ,user_image10 =O0OOOOOOOO00000O0 ,user_image11 =O0O00O0000OOOOO0O ,user_image12 =O0000O000O0O000O0 )#line:936
            else :#line:937
                return render_template ('escuchar_uro.html',nid2 =0 ,faqs =O00O0O0OO00000OOO ,faq_titulo ="Preguntas y respuestas: ",result_busqueda =OO0O000O000O0OOOO ,user_image6 =OO000O0O00O0O00OO ,user_image7 =O00OOO0O0O000O0O0 ,user_image5 =O0O0OO000OO000OOO ,user_image8 =O0O000OO00000OO0O ,user_image9 =OOO00000OOO00000O ,user_image10 =O0OOOOOOOO00000O0 ,user_image11 =O0O00O0000OOOOO0O ,user_image12 =O0000O000O0O000O0 )#line:938
        elif len (O00OO00O000O0OOO0 )>=1 :#line:939
            O0OOOO00000O0OO00 =[]#line:940
            OO0OOOOOOO00O00O0 =[]#line:941
            OO0O000O000O0OOOO ={}#line:942
            for O00O0OOO0O0OOO0O0 in O00OO00O000O0OOO0 :#line:943
                O0OOOO00000O0OO00 .append (O00O0OOO0O0OOO0O0 ["title"])#line:944
                OO0OOOOOOO00O00O0 .append (O00O0OOO0O0OOO0O0 ["nid"])#line:945
            for O0O0000O00000OO00 ,O00O0OOO0O0OOO0O0 in enumerate (O0OOOO00000O0OO00 ):#line:946
                 OO0O000O000O0OOOO [OO0OOOOOOO00O00O0 [O0O0000O00000OO00 ]]=O00O0OOO0O0OOO0O0 #line:947
            if len (O00O0O0OO00000OOO )==0 :#line:949
                return render_template ('escuchar_uro.html',nid2 =0 ,result_busqueda =OO0O000O000O0OOOO ,user_image6 =OO000O0O00O0O00OO ,user_image7 =O00OOO0O0O000O0O0 ,user_image5 =O0O0OO000OO000OOO ,user_image8 =O0O000OO00000OO0O ,user_image9 =OOO00000OOO00000O ,user_image10 =O0OOOOOOOO00000O0 ,user_image11 =O0O00O0000OOOOO0O ,user_image12 =O0000O000O0O000O0 )#line:950
            else :#line:951
                return render_template ('escuchar_uro.html',nid2 =0 ,faqs =O00O0O0OO00000OOO ,faq_titulo ="Preguntas y respuestas: ",result_busqueda =OO0O000O000O0OOOO ,user_image6 =OO000O0O00O0O00OO ,user_image7 =O00OOO0O0O000O0O0 ,user_image5 =O0O0OO000OO000OOO ,user_image8 =O0O000OO00000OO0O ,user_image9 =OOO00000OOO00000O ,user_image10 =O0OOOOOOOO00000O0 ,user_image11 =O0O00O0000OOOOO0O ,user_image12 =O0000O000O0O000O0 )#line:952
    else :#line:953
        return render_template ('escuchar_uro.html',nid2 =0 ,result_busqueda =OO0O000O000O0OOOO ,prediction_text ="No te he entendido bien, dale al boton `Escuchar´ y repite tu pregunta",user_image5 =O0O0OO000OO000OOO ,user_image6 =OO000O0O00O0O00OO ,user_image7 =O00OOO0O0O000O0O0 ,user_image8 =O0O000OO00000OO0O ,user_image9 =OOO00000OOO00000O ,user_image10 =O0OOOOOOOO00000O0 ,user_image11 =O0O00O0000OOOOO0O ,user_image12 =O0000O000O0O000O0 )#line:954
@app .route ("/ajustes")#line:956
async def ajustes ():#line:957
    O00O0OO0OOO00OO00 =os .path .join (app .config ['UPLOAD_FOLDER'],'estrella.png')#line:958
    return render_template ('ajustes.html',user_image7 =O00O0OO0OOO00OO00 )#line:959
if __name__ =="__main__":#line:961
    app .run ()#line:962
