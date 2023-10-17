from flask import Flask ,render_template ,request ,jsonify #line:1
import pandas as pd #line:2
import numpy as np #line:3
import xlrd2 as xlrd #line:4
import unicodedata #line:5
import spacy #line:6
import inflect #line:7
#nlp =spacy .load ("es_dep_news_trf")#line:8
nlp =spacy .load ("es_core_news_sm")#line:8
from inflector import Inflector ,Spanish #line:9
inflector =Inflector (Spanish )#line:10
import speech_recognition as sr #line:11
import os #line:12
import requests #line:13
from requests .auth import HTTPBasicAuth #line:14
import asyncio #line:15
import aiohttp #line:16
auth =aiohttp .BasicAuth ('1234','API')#line:18
base_url ='https://orva.tedcas.com/api/'#line:19
async def buscar_faq (O0000O0OO000000OO ,O0OOO0OO0O00O00O0 ):#line:21
    OO00O0O00OOO0O000 ="preguntas_qh_tags2.xlsx"#line:22
    O00OOOO000OOO00O0 =pd .read_excel (OO00O0O00OOO0O000 ,engine ="openpyxl")#line:23
    O00000OO00000000O =0 #line:24
    OO0O0OOOO0OO00OO0 =O0000O0OO000000OO #line:25
    O0000OOOO0OO00O00 =[]#line:26
    print ("result"+str (OO0O0OOOO0OO00OO0 ))#line:27
    for OO0O0OOOOO0O0O0O0 ,O0OOOO000O0O000O0 in O00OOOO000OOO00O0 .iterrows ():#line:28
        OOOOO00O00OO0O0OO =O00OOOO000OOO00O0 .loc [OO0O0OOOOO0O0O0O0 ,'TAGS2']#line:29
        OOOOO00O00OO0O0OO =OOOOO00O00OO0O0OO .split (",")#line:30
        O0000OOOO0OO00O00 .append (OOOOO00O00OO0O0OO )#line:31
    OOO00O0OOOO00OO00 =[]#line:32
    OOOOO00O00OO0O0OO =[]#line:33
    for O0O000OO00O000O00 ,O000OOO0000OOO0OO in enumerate (OO0O0OOOO0OO00OO0 ):#line:34
        OO0O0OOOO0OO00OO0 [O0O000OO00O000O00 ]=inflector .singularize (str (O000OOO0000OOO0OO ))#line:35
    OO00O00OO00O00OOO =np .zeros (len (O00OOOO000OOO00O0 .index ),dtype =int )#line:36
    for OOOO00O0000000O00 ,O0OOOO000O0O000O0 in enumerate (O0000OOOO0OO00O00 ):#line:37
        OO0OOO0O0OOOOOO0O =[]#line:38
        for O000OOO0000OOO0OO in O0OOOO000O0O000O0 :#line:39
            if O0OOO0OO0O00O00O0 ==0 :#line:40
                if O000OOO0000OOO0OO !=[]:#line:41
                    O00000OO00000000O =0 #line:42
                    for O00O00OO0O0O0O0O0 in range (100 ):#line:43
                        O00O00OO0O0O0O0O0 =O00O00OO0O0O0O0O0 /10 #line:44
                        O00O00OO0O0O0O0O0 =str (O00O00OO0O0O0O0O0 )#line:45
                        if O000OOO0000OOO0OO ==O00O00OO0O0O0O0O0 :#line:46
                            O00O00OO0O0O0O0O0 =O00O00OO0O0O0O0O0 .split (".")#line:47
                            OO0OOO0O0OOOOOO0O .append (O00O00OO0O0O0O0O0 [0 ])#line:48
                            OO0OOO0O0OOOOOO0O .append ("con")#line:49
                            OO0OOO0O0OOOOOO0O .append (O00O00OO0O0O0O0O0 [1 ])#line:50
                            O00000OO00000000O =O00000OO00000000O +1 #line:51
                    if O00000OO00000000O ==0 :#line:52
                        OO0OOO0O0OOOOOO0O .append (O000OOO0000OOO0OO )#line:53
            if O0OOO0OO0O00O00O0 ==1 :#line:54
                OO0OOO0O0OOOOOO0O .append (O000OOO0000OOO0OO )#line:55
        OOO00O0OOOO00OO00 .append (OO0OOO0O0OOOOOO0O )#line:56
        for OOOO0OOOO0OO0O0OO in OO0O0OOOO0OO00OO0 :#line:57
            for O00OOOOO0000O0000 ,O000OOO0000OOO0OO in enumerate (OOO00O0OOOO00OO00 [OOOO00O0000000O00 ]):#line:58
                            if str (OOOO0OOOO0OO0O0OO )=="maya":#line:59
                                OOOO0OOOO0OO0O0OO ="malla"#line:60
                            if str (OOOO0OOOO0OO0O0OO )=="pilos"or str (OOOO0OOOO0OO0O0OO )=="pilo":#line:61
                                OOOO0OOOO0OO0O0OO ="philo"#line:62
                            if str (OOOO0OOOO0OO0O0OO )=="filos"or str (OOOO0OOOO0OO0O0OO )=="filo":#line:63
                                OOOO0OOOO0OO0O0OO ="philo"#line:64
                            if str (OOOO0OOOO0OO0O0OO )=="sinces"or str (OOOO0OOOO0OO0O0OO )=="sinc":#line:65
                                OOOO0OOOO0OO0O0OO ="synthe"#line:66
                            if str (OOOO0OOOO0OO0O0OO )=="sintes"or str (OOOO0OOOO0OO0O0OO )=="sint":#line:67
                                OOOO0OOOO0OO0O0OO ="synthe"#line:68
                            if str (OOOO0OOOO0OO0O0OO )=="axos"or str (OOOO0OOOO0OO0O0OO )=="axo":#line:69
                                OOOO0OOOO0OO0O0OO ="axso"#line:70
                            if str (OOOO0OOOO0OO0O0OO )=="uno":#line:71
                                OOOO0OOOO0OO0O0OO ="1"#line:72
                            if str (OOOO0OOOO0OO0O0OO )=="dos"or str (OOOO0OOOO0OO0O0OO )=="do":#line:73
                                OOOO0OOOO0OO0O0OO ="2"#line:74
                            if str (OOOO0OOOO0OO0O0OO )=="tres"or str (OOOO0OOOO0OO0O0OO )=="tr":#line:75
                                OOOO0OOOO0OO0O0OO ="3"#line:76
                            if str (OOOO0OOOO0OO0O0OO )=="cuatro":#line:77
                                OOOO0OOOO0OO0O0OO ="4"#line:78
                            if str (OOOO0OOOO0OO0O0OO )=="cinco":#line:79
                                OOOO0OOOO0OO0O0OO ="5"#line:80
                            if str (OOOO0OOOO0OO0O0OO )=="seis"or str (OOOO0OOOO0OO0O0OO )=="sei":#line:81
                                OOOO0OOOO0OO0O0OO ="6"#line:82
                            if str (OOOO0OOOO0OO0O0OO )=="siete":#line:83
                                OOOO0OOOO0OO0O0OO ="7"#line:84
                            if str (OOOO0OOOO0OO0O0OO )=="ocho":#line:85
                                OOOO0OOOO0OO0O0OO ="8"#line:86
                            if str (OOOO0OOOO0OO0O0OO )=="nueve":#line:87
                                OOOO0OOOO0OO0O0OO ="9"#line:88
                            if str (OOOO0OOOO0OO0O0OO )=="cero":#line:89
                                OOOO0OOOO0OO0O0OO ="0"#line:90
                            if str (OOOO0OOOO0OO0O0OO )=="veintiuno":#line:91
                                OOOO0OOOO0OO0O0OO ="21"#line:92
                            if str (OOOO0OOOO0OO0O0OO )=="veinte":#line:93
                                OOOO0OOOO0OO0O0OO ="20"#line:94
                            if str (OOOO0OOOO0OO0O0OO )=="veintidos"or str (OOOO0OOOO0OO0O0OO )=="veintido":#line:95
                                OOOO0OOOO0OO0O0OO ="22"#line:96
                            if str (OOOO0OOOO0OO0O0OO )=="veintitres"or str (OOOO0OOOO0OO0O0OO )=="veintitre":#line:97
                                OOOO0OOOO0OO0O0OO ="23"#line:98
                            if str (OOOO0OOOO0OO0O0OO )=="veinticuatro":#line:99
                                OOOO0OOOO0OO0O0OO ="24"#line:100
                            if str (OOOO0OOOO0OO0O0OO )=="veinticinco":#line:101
                                OOOO0OOOO0OO0O0OO ="25"#line:102
                            if str (OOOO0OOOO0OO0O0OO )=="veintiseis"or str (OOOO0OOOO0OO0O0OO )=="veintisei":#line:103
                                OOOO0OOOO0OO0O0OO ="26"#line:104
                            if str (OOOO0OOOO0OO0O0OO )=="veintisiete":#line:105
                                OOOO0OOOO0OO0O0OO ="27"#line:106
                            if str (OOOO0OOOO0OO0O0OO )=="veintiocho":#line:107
                                OOOO0OOOO0OO0O0OO ="28"#line:108
                            if str (OOOO0OOOO0OO0O0OO )=="veintinueve":#line:109
                                OOOO0OOOO0OO0O0OO ="29"#line:110
                            if str (OOOO0OOOO0OO0O0OO )=="treinta":#line:111
                                OOOO0OOOO0OO0O0OO ="30"#line:112
                            if str (remove_accents (O000OOO0000OOO0OO )).lower ()==str (remove_accents (OOOO0OOOO0OO0O0OO )).lower ():#line:113
                                OO00O00OO00O00OOO [OOOO00O0000000O00 ]=OO00O00OO00O00OOO [OOOO00O0000000O00 ]+1 #line:114
                                OOO00O0OOOO00OO00 [OOOO00O0000000O00 ].pop (O00OOOOO0000O0000 )#line:115
        O00O00000000OOO0O =np .argwhere (OO00O00OO00O00OOO ==np .amax (OO00O00OO00O00OOO ))#line:117
        OOOO0000OOO0OO00O =[]#line:118
        OOO0OO000OO0O0OOO ={}#line:119
        O00OOOO000OOO00O0 =xlrd .open_workbook (OO00O0O00OOO0O000 )#line:120
        O00OOOO000OOO00O0 =O00OOOO000OOO00O0 .sheet_by_index (0 )#line:121
        if not np .all (OO00O00OO00O00OOO ==0 ):#line:122
            for O0O0OOOO00OOO0O00 in O00O00000000OOO0O :#line:123
                OO000O0O0O000OO0O =O00OOOO000OOO00O0 .cell (int (O0O0OOOO00OOO0O00 )+1 ,3 )#line:124
                O00O0000OO0000O0O =O00OOOO000OOO00O0 .cell (int (O0O0OOOO00OOO0O00 )+1 ,4 )#line:125
                OO000O0O0O000OO0O =str (OO000O0O0O000OO0O )#line:126
                O00O0000OO0000O0O =str (O00O0000OO0000O0O )#line:127
                OO000O0O0O000OO0O =OO000O0O0O000OO0O .split ("'")#line:128
                O00O0000OO0000O0O =O00O0000OO0000O0O .split ("'")#line:129
                OOOO0000OOO0OO00O .append (f" {OO000O0O0O000OO0O[1]} {O00O0000OO0000O0O[1]} ")#line:130
    return OOOO0000OOO0OO00O #line:131
async def boton_pdf_video (OO0OO0OOO0O0O0OO0 ,OO00O00O00000OO00 ,O00OO0O000OO0OO0O ):#line:133
    O00O0OOOOO0OO0O00 =aiohttp .TCPConnector (ssl =True )#line:134
    async with aiohttp .ClientSession (connector =O00O0OOOOO0OO0O00 )as O0O0OOOO00O000O00 :#line:135
        O0O00000OO0OOO000 =await O0O0OOOO00O000O00 .get (f'{base_url}all-content/{OO0OO0OOO0O0O0OO0}',auth =auth )#line:136
        O0OOOO000000O00OO =await O0O00000OO0OOO000 .json ()#line:137
        OO0O0000O0O0OO0OO =[]#line:139
        OOOO0OO00O000O000 ={}#line:140
        if O00OO0O000OO0OO0O =="0":#line:142
            for OO00OOO000OO0000O in O0OOOO000000O00OO :#line:143
                if OO00OOO000OO0000O ['type']=="Intervencion":#line:144
                    OO0O0000O0O0OO0OO .append (OO00OOO000OO0000O ['nid'])#line:145
        else :#line:146
            OO0O0000O0O0OO0OO .append (O00OO0O000OO0OO0O )#line:147
        for OO0OOO0000O000000 in OO0O0000O0O0OO0OO :#line:149
            OO0O00O00O00OOO0O =await O0O0OOOO00O000O00 .get (f'{base_url}intervenciones/{OO0OOO0000O000000}',auth =auth )#line:150
            O0OOO0OOO0O000000 =await OO0O00O00O00OOO0O .json ()#line:151
            O0OOO0OOO0O000000 =O0OOO0OOO0O000000 [0 ]#line:152
            O0O0OO0OOOOO0000O ={}#line:153
            if OO00O00O00000OO00 in O0OOO0OOO0O000000 :#line:155
                OO00000OO00OO0O0O =O0OOO0OOO0O000000 [OO00O00O00000OO00 ]#line:156
                for OOO0OO00O0O00OOO0 in OO00000OO00OO0O0O :#line:157
                    if OO00O00O00000OO00 =='field_pdf':#line:158
                        O0O0OO0OOOOO0000O [OOO0OO00O0O00OOO0 ['descripcion']]="https://orva.tedcas.com/"+str (OOO0OO00O0O00OOO0 ['url'])#line:159
                    if OO00O00O00000OO00 =='field_video':#line:160
                        O0O0OO0OOOOO0000O [OOO0OO00O0O00OOO0 ['descripcion']]=str (OOO0OO00O0O00OOO0 ['url'])#line:161
                OOOO0OO00O000O000 [O0OOO0OOO0O000000 ['title']]=O0O0OO0OOOOO0000O #line:163
            else :#line:164
                if O00OO0O000OO0OO0O =='0':#line:165
                    O00OO0O000OO0OO0O ='0'#line:166
                else :#line:167
                    print ("nid dentro del if "+str (O00OO0O000OO0OO0O ))#line:168
                    O0O0OO0OOOOO0000O ["No hay archivos"]=""#line:169
                    OOOO0OO00O000O000 ["No hay archivos"]=O0O0OO0OOOOO0000O #line:170
        return OOOO0OO00O000O000 #line:172
async def boton_word_ppt (O0OOO00OOO0000O00 ,OOO0OO00O0O0OOO0O ,OO0OO0OO0O00000OO ):#line:174
    OOOO000O0OO0OO000 =aiohttp .TCPConnector (ssl =True )#line:175
    async with aiohttp .ClientSession (connector =OOOO000O0OO0OO000 )as OO0000000O000O00O :#line:176
        OOOOOOO00OOO0O0OO =await OO0000000O000O00O .get (f'{base_url}all-content/{O0OOO00OOO0000O00}',auth =auth )#line:177
        O0O0OOO0O00O0O000 =await OOOOOOO00OOO0O0OO .json ()#line:178
        O0000OO00O000O000 =[]#line:180
        OO0OOO0O0OOOOO0OO ={}#line:181
        if OO0OO0OO0O00000OO =='0':#line:183
            for OO0OOOOOOOOOO00OO in O0O0OOO0O00O0O000 :#line:184
                if OO0OOOOOOOOOO00OO ['type']=="Intervencion":#line:185
                    O0000OO00O000O000 .append (OO0OOOOOOOOOO00OO ['nid'])#line:186
        else :#line:187
            O0000OO00O000O000 .append (OO0OO0OO0O00000OO )#line:188
        for OOO0OOO000O000OO0 in O0000OO00O000O000 :#line:190
            O00O000OOOOOOO00O =await OO0000000O000O00O .get (f'{base_url}intervenciones/{OOO0OOO000O000OO0}',auth =auth )#line:191
            OOO0O0OOOOOO00O00 =await O00O000OOOOOOO00O .json ()#line:192
            OOO0O0OOOOOO00O00 =OOO0O0OOOOOO00O00 [0 ]#line:193
            if len (OOO0O0OOOOOO00O00 [OOO0OO00O0O0OOO0O ])!=0 :#line:194
                OO0OOO0O0OOOOO0OO [OOO0O0OOOOOO00O00 ['title']]="https://orva.tedcas.com/"+str (OOO0O0OOOOOO00O00 [OOO0OO00O0O0OOO0O ])#line:195
            if len (OOO0O0OOOOOO00O00 [OOO0OO00O0O0OOO0O ])==0 and OO0OO0OO0O00000OO !='0':#line:196
                OO0OOO0O0OOOOO0OO ["No hay archivos"]=""#line:197
        return OO0OOO0O0OOOOO0OO #line:199
async def boton_materiales (O00O000OO0O00O000 ,O00OO0OOO00O000OO ):#line:201
    O0O0O0OOOOOOO0O0O =aiohttp .TCPConnector (ssl =True )#line:202
    async with aiohttp .ClientSession (connector =O0O0O0OOOOOOO0O0O )as O0O0OO000O0O00O0O :#line:203
        OOO0OO0O000O0OO00 ={}#line:204
        if O00OO0OOO00O000OO =='0':#line:206
            O0OO000OOO0OO0OOO =await O0O0OO000O0O00O0O .get (f'{base_url}listado_completo_cajas/{O00O000OO0O00O000}',auth =auth )#line:207
            O00O00OO00O0000O0 =await O0OO000OOO0OO0OOO .json ()#line:208
            for OO0OO0OOOOOO0OO00 in O00O00OO00O0000O0 :#line:209
                OOO0OO0O000O0OO00 [OO0OO0OOOOOO0OO00 ['title']]=OO0OO0OOOOOO0OO00 ['nid']#line:210
            OOO0OO0O000O0OO00 ['']="si hay"#line:211
        else :#line:212
            O0OO000OOO0OO0OOO =await O0O0OO000O0O00O0O .get (f'{base_url}intervenciones/{O00OO0OOO00O000OO}',auth =auth )#line:213
            O00O00OO00O0000O0 =await O0OO000OOO0OO0OOO .json ()#line:214
            O00O00OO00O0000O0 =O00O00OO00O0000O0 [0 ]#line:215
            if 'field_cajas'in O00O00OO00O0000O0 :#line:216
                O00O00OO00O0000O0 =O00O00OO00O0000O0 ['field_cajas']#line:217
                for OO0OO0OOOOOO0OO00 in O00O00OO00O0000O0 :#line:218
                    OOO0OO0O000O0OO00 [OO0OO0OOOOOO0OO00 ['caja']]=OO0OO0OOOOOO0OO00 ['id']#line:219
                OOO0OO0O000O0OO00 ['']="si hay"#line:220
            else :#line:221
                if O00OO0OOO00O000OO !=0 :#line:222
                    OOO0OO0O000O0OO00 ['']=""#line:223
        return OOO0OO0O000O0OO00 #line:224
async def cargar_base_datos (OOOOO0O0O0O0O0O00 ,OO00O0OO0O0O00O00 ):#line:226
    O00O0OOOO0O0O00OO =None #line:227
    OO0O00OO000O0O0O0 =[]#line:228
    O000O0O00O0O0OO00 =aiohttp .TCPConnector (ssl =True )#line:229
    async with aiohttp .ClientSession (connector =O000O0O00O0O0OO00 )as O00OO0OO00O0OO00O :#line:230
        O0O00OOOO0000OOOO =await O00OO0OO00O0OO00O .get ('https://orva.tedcas.com/api/all-content/'+str (OO00O0OO0O0O00O00 ),auth =auth )#line:231
        O000O0O0OO0000000 =await O0O00OOOO0000OOOO .json ()#line:232
        OO00OO0OO0OO00OO0 =np .zeros (len (O000O0O0OO0000000 ),dtype =int )#line:233
        OOO0OO00O0OOOOO00 =[]#line:234
        for O0OO0O0000OOOOOO0 in OOOOO0O0O0O0O0O00 :#line:235
            O0O0O0OO0OO000OO0 =0 #line:236
            for O0000OO00O0O000O0 in range (100 ):#line:237
                O0000OO00O0O000O0 =O0000OO00O0O000O0 /10 #line:238
                if O0OO0O0000OOOOOO0 ==str (O0000OO00O0O000O0 ):#line:239
                    O0OO0O0000OOOOOO0 =str (O0000OO00O0O000O0 ).split ('.')#line:240
                    OOO0OO00O0OOOOO00 .append (O0OO0O0000OOOOOO0 )#line:241
                    O0O0O0OO0OO000OO0 =O0O0O0OO0OO000OO0 +1 #line:242
            if O0OO0O0000OOOOOO0 =='con':#line:243
                O0O0O0OO0OO000OO0 =O0O0O0OO0OO000OO0 +1 #line:244
            if O0O0O0OO0OO000OO0 ==0 :#line:245
                OOO0OO00O0OOOOO00 .append (O0OO0O0000OOOOOO0 )#line:246
        for O0OOO0OOO0O000O00 in range (len (O000O0O0OO0000000 )):#line:247
            O0OOOO000000O0OOO =0 #line:248
            OOOO000OO0O00O0O0 =O000O0O0OO0000000 [O0OOO0OOO0O000O00 ]#line:249
            OOOO0O0O0000OOOOO =str (OOOO000OO0O00O0O0 ['title']).lower ()#line:250
            OOOO0O0O0000OOOOO =remove_accents (OOOO0O0O0000OOOOO )#line:251
            OOOO0O0O0000OOOOO =OOOO0O0O0000OOOOO .split (' ')#line:252
            for OOOO0O0OO000O0OO0 ,OO0O000O00000OOO0 in enumerate (OOOO0O0O0000OOOOO ):#line:253
                for OOOO00OOOOO0OOOOO ,O0OOO00O00OO000O0 in enumerate (OOOO0O0O0000OOOOO ):#line:254
                    if OOOO00OOOOO0OOOOO !=OOOO0O0OO000O0OO0 :#line:255
                        if OO0O000O00000OOO0 ==O0OOO00O00OO000O0 :#line:256
                            OOOO0O0O0000OOOOO .pop (OOOO00OOOOO0OOOOO )#line:257
            for OOOO0O0OO000O0OO0 ,OO0O000O00000OOO0 in enumerate (OOOO0O0O0000OOOOO ):#line:258
                for O0000OO00O0O000O0 in range (100 ):#line:259
                    O0000OO00O0O000O0 =O0000OO00O0O000O0 /10 #line:260
                    if OO0O000O00000OOO0 ==str (O0000OO00O0O000O0 ):#line:261
                        OO0O000O00000OOO0 =str (O0000OO00O0O000O0 ).split ('.')#line:262
                        OOOO0O0O0000OOOOO .append (OO0O000O00000OOO0 )#line:263
                for OOO00O0O0OOO00000 in OOO0OO00O0OOOOO00 :#line:264
                            if OOO00O0O0OOO00000 =="maya":#line:265
                                OOO00O0O0OOO00000 ="malla"#line:266
                            if OOO00O0O0OOO00000 =="pilos"or OOO00O0O0OOO00000 =="pilo":#line:267
                                OOO00O0O0OOO00000 ="philo"#line:268
                            if OOO00O0O0OOO00000 =="filos"or OOO00O0O0OOO00000 =="filo":#line:269
                                OOO00O0O0OOO00000 ="philo"#line:270
                            if OOO00O0O0OOO00000 =="sinces"or OOO00O0O0OOO00000 =="sinc":#line:271
                                OOO00O0O0OOO00000 ="synthe"#line:272
                            if OOO00O0O0OOO00000 =="sintes"or OOO00O0O0OOO00000 =="sint":#line:273
                                OOO00O0O0OOO00000 ="synthe"#line:274
                            if OOO00O0O0OOO00000 =="axos"or OOO00O0O0OOO00000 =="axo":#line:275
                                OOO00O0O0OOO00000 ="axso"#line:276
                            if OOO00O0O0OOO00000 =="uno":#line:277
                                OOO00O0O0OOO00000 =1 #line:278
                            if OOO00O0O0OOO00000 =="dos"or OOO00O0O0OOO00000 =="do":#line:279
                                OOO00O0O0OOO00000 =2 #line:280
                            if OOO00O0O0OOO00000 =="tres"or OOO00O0O0OOO00000 =="tr":#line:281
                                OOO00O0O0OOO00000 =3 #line:282
                            if OOO00O0O0OOO00000 =="cuatro":#line:283
                                OOO00O0O0OOO00000 =4 #line:284
                            if OOO00O0O0OOO00000 =="cinco":#line:285
                                OOO00O0O0OOO00000 =5 #line:286
                            if OOO00O0O0OOO00000 =="seis"or OOO00O0O0OOO00000 =="sei":#line:287
                                OOO00O0O0OOO00000 =6 #line:288
                            if OOO00O0O0OOO00000 =="siete":#line:289
                                OOO00O0O0OOO00000 =7 #line:290
                            if OOO00O0O0OOO00000 =="ocho":#line:291
                                OOO00O0O0OOO00000 =8 #line:292
                            if OOO00O0O0OOO00000 =="nueve":#line:293
                                OOO00O0O0OOO00000 =9 #line:294
                            if OOO00O0O0OOO00000 =="cero":#line:295
                                OOO00O0O0OOO00000 =0 #line:296
                            if OOO00O0O0OOO00000 =="veintiuno":#line:297
                                OOO00O0O0OOO00000 ="21"#line:298
                            if OOO00O0O0OOO00000 =="veinte":#line:299
                                OOO00O0O0OOO00000 ="20"#line:300
                            if OOO00O0O0OOO00000 =="veintidos"or OOO00O0O0OOO00000 =="veintido":#line:301
                                OOO00O0O0OOO00000 ="22"#line:302
                            if OOO00O0O0OOO00000 =="veintitres"or OOO00O0O0OOO00000 =="veintitre":#line:303
                                OOO00O0O0OOO00000 ="23"#line:304
                            if OOO00O0O0OOO00000 =="veinticuatro":#line:305
                                OOO00O0O0OOO00000 ="24"#line:306
                            if OOO00O0O0OOO00000 =="veinticinco":#line:307
                                OOO00O0O0OOO00000 ="25"#line:308
                            if OOO00O0O0OOO00000 =="veintiseis"or OOO00O0O0OOO00000 =="veintisei":#line:309
                                OOO00O0O0OOO00000 ="26"#line:310
                            if OOO00O0O0OOO00000 =="veintisiete":#line:311
                                OOO00O0O0OOO00000 ="27"#line:312
                            if OOO00O0O0OOO00000 =="veintiocho":#line:313
                                OOO00O0O0OOO00000 ="28"#line:314
                            if OOO00O0O0OOO00000 =="veintinueve":#line:315
                                OOO00O0O0OOO00000 ="29"#line:316
                            if OOO00O0O0OOO00000 =="treinta":#line:317
                                OOO00O0O0OOO00000 ="30"#line:318
                            if type (OOO00O0O0OOO00000 )==int and type (O00O0OOOO0O0O00OO )==int :#line:319
                                O0000OO00O0O000O0 =str (O00O0OOOO0O0O00OO )+'.'+str (OOO00O0O0OOO00000 )#line:320
                                OOO00O0O0OOO00000 =O0000OO00O0O000O0 .split ('.')#line:321
                            O00O0OOOO0O0O00OO =OOO00O0O0OOO00000 #line:322
                            OOO00O0O0OOO00000 =inflector .singularize (str (OOO00O0O0OOO00000 ))#line:323
                            OO0O000O00000OOO0 =inflector .singularize (str (OO0O000O00000OOO0 ))#line:324
                            OOO00O0O0OOO00000 =remove_accents (OOO00O0O0OOO00000 )#line:325
                            if OO0O000O00000OOO0 ==OOO00O0O0OOO00000 :#line:326
                                O0OOOO000000O0OOO =O0OOOO000000O0OOO +1 #line:327
            OO00OO0OO0OO00OO0 [O0OOO0OOO0O000O00 ]=O0OOOO000000O0OOO #line:328
        OOOOOOOO00OO00O00 =np .argwhere (OO00OO0OO0OO00OO0 ==np .amax (OO00OO0OO0OO00OO0 ))#line:329
        for O0OOO0OOO0O000O00 in OOOOOOOO00OO00O00 :#line:330
            OO0O00OO000O0O0O0 .append (O000O0O0OO0000000 [int (O0OOO0OOO0O000O00 )])#line:331
        if np .all (OO00OO0OO0OO00OO0 ==0 ):#line:332
            OO0O00OO000O0O0O0 =None #line:333
    return OO0O00OO000O0O0O0 #line:334
async def cargar_tipo (O000000OO000O0OO0 ,OOO0OOO000O000O0O ):#line:336
    O0O0OO0O00OOO0OOO =aiohttp .TCPConnector (ssl =True )#line:337
    async with aiohttp .ClientSession (connector =O0O0OO0O00OOO0OOO )as OOO0OOOO00OO0000O :#line:338
        OOO0OO0O0OOO0OO00 =await OOO0OOOO00OO0000O .get (f'{base_url}all-content/{OOO0OOO000O000O0O}',auth =auth )#line:339
        OO0O00O0OOO0OOO00 =await OOO0OO0O0OOO0OO00 .json ()#line:340
        OOO0000OOOOOO00OO =None #line:341
        O00OO00OOO0OO0000 =None #line:342
        for OOOOOO0O0OOOOO0O0 in OO0O00O0OOO0OOO00 :#line:343
            if O000000OO000O0OO0 ==OOOOOO0O0OOOOO0O0 ["nid"]:#line:344
                OOO0000OOOOOO00OO =OOOOOO0O0OOOOO0O0 ["type"]#line:345
                O00OO00OOO0OO0000 =OOOOOO0O0OOOOO0O0 #line:346
                break #line:347
    return O00OO00OOO0OO0000 ,OOO0000OOOOOO00OO #line:348
async def cargar_archivo (O0OOO0OOO00OOOOOO ,O0O0O0O0OOOO00000 ,OO0OO0000OOOO0O0O ):#line:350
    O0OO0OOO00OOO0O0O =[]#line:351
    O00O0OO000OOO0OO0 =aiohttp .TCPConnector (ssl =True )#line:352
    async with aiohttp .ClientSession (connector =O00O0OO000OOO0OO0 )as O000O0O0000OOO000 :#line:353
        O000OO0O0O00OO0O0 =await O000O0O0000OOO000 .get ('https://orva.tedcas.com/api/'+str (OO0OO0000OOOO0O0O ),auth =auth )#line:354
        OO00O0000O0OOOOOO =await O000OO0O0O00OO0O0 .json ()#line:355
        OO00O0000O0OOOOOO =OO00O0000O0OOOOOO [0 ]#line:356
        O000OOOO0OOOOO00O ="field_"+str (O0OOO0OOO00OOOOOO )#line:357
        OOOO00OO0O00OO0O0 =OO00O0000O0OOOOOO [O000OOOO0OOOOO00O ]#line:358
        if O000OOOO0OOOOO00O =="field_image":#line:359
            OO00O0000O0OOOOOO =OO00O0000O0OOOOOO ['field_image']#line:360
            OO00O0000O0OOOOOO =OO00O0000O0OOOOOO .split (',')#line:361
            OO00O0000O0OOOOOO =[O0OO0OO00O00OO0O0 .replace (' ','')for O0OO0OO00O00OO0O0 in OO00O0000O0OOOOOO ]#line:362
            for O00000OO00O0O0O00 in OO00O0000O0OOOOOO :#line:363
                 O0OO0OOO00OOO0O0O .append ("https://orva.tedcas.com/"+str (O00000OO00O0O0O00 ))#line:364
            print (O0OO0OOO00OOO0O0O )#line:365
            return O0OO0OOO00OOO0O0O #line:366
        if len (OOOO00OO0O00OO0O0 )==0 :#line:367
             O0O0O0O0OO0O0O0O0 ="No hay archivos subidos"#line:368
             O0OO0OOO00OOO0O0O ="https://quirohelp.onrender.com/especialidad"#line:369
        elif type (OOOO00OO0O00OO0O0 )==str :#line:370
             O0OO0OOO00OOO0O0O ="https://orva.tedcas.com/"+str (OOOO00OO0O00OO0O0 )#line:371
             O0O0O0O0OO0O0O0O0 =OOOO00OO0O00OO0O0 #line:372
        elif type (OOOO00OO0O00OO0O0 )==list :#line:373
            for O0OOOO00O00OO00OO ,OO00O0000O0OO0OOO in OOOO00OO0O00OO0O0 :#line:374
                O0OO0OOO00OOO0O0O [O0OOOO00O00OO00OO ]="https://orva.tedcas.com/"+str (OO00O0000O0OO0OOO )#line:375
                O0O0O0O0OO0O0O0O0 =OOOO00OO0O00OO0O0 #line:376
        return O0O0O0O0OOOO00000 ,O0OO0OOO00OOO0O0O ,O0O0O0O0OO0O0O0O0 #line:377
async def cargar_archivo_grande (OO0OOO0OOOO0000O0 ,O0OO0OOOOOO0O0OOO ,OOOOOOOO000000O0O ):#line:379
    OO0OOO0000OO0O00O =aiohttp .TCPConnector (ssl =True )#line:380
    async with aiohttp .ClientSession (connector =OO0OOO0000OO0O00O )as O0O000OOOO00OOO0O :#line:381
        O0O0O000OOO000O00 =await O0O000OOOO00OOO0O .get ('https://orva.tedcas.com/api/'+str (OOOOOOOO000000O0O ),auth =auth )#line:382
        OO00O000OOO0000OO =await O0O0O000OOO000O00 .json ()#line:383
        OOO0O0OO0O00OO00O ={}#line:384
        if OO0OOO0OOOO0000O0 =='title_material':#line:385
            for O00O0O0OOOO0O0O00 in OO00O000OOO0000OO :#line:386
                  OOO0O0OO0O00OO00O [O00O0O0OOOO0O0O00 [OO0OOO0OOOO0000O0 ]]=(O00O0O0OOOO0O0O00 [OO0OOO0OOOO0000O0 ])#line:387
            return OOO0O0OO0O00OO00O ,O0OO0OOOOOO0O0OOO #line:388
        OO00O000OOO0000OO =OO00O000OOO0000OO [0 ]#line:389
        OOO0O00OOOO00OO00 ="field_"+str (OO0OOO0OOOO0000O0 )#line:390
        OOO0O00OOOO00OO00 =OO00O000OOO0000OO [OOO0O00OOOO00OO00 ]#line:391
        if len (OOO0O00OOOO00OO00 )==0 :#line:392
             OOO0O0OO0O00OO00O ["No hay archivos"]="https://quirohelp.onrender.com/especialidad"#line:393
        else :#line:394
            for O00O0O0OOOO0O0O00 in OOO0O00OOOO00OO00 :#line:395
                OOO0O0OO0O00OO00O [O00O0O0OOOO0O0O00 ['descripcion']]="https://orva.tedcas.com/"+str (O00O0O0OOOO0O0O00 ['url'])#line:396
        return O0OO0OOOOOO0O0OOO ,OOO0O0OO0O00OO00O #line:397
async def cargar_caja (O00000O0O0O000O0O ,OO0OO0O000O0O00O0 ):#line:399
    OOOO000O000OO0000 ={}#line:400
    O00O0OOOOOOO000OO =aiohttp .TCPConnector (ssl =True )#line:401
    async with aiohttp .ClientSession (connector =O00O0OOOOOOO000OO )as O00000O0O0OOO0OOO :#line:402
        O0000O000O0OOO000 =await O00000O0O0OOO0OOO .get (f'{base_url}intervenciones/{O00000O0O0O000O0O}',auth =auth )#line:403
        O0O00OO0000O0OOO0 =await O0000O000O0OOO000 .json ()#line:404
        O0O00OO0000O0OOO0 =O0O00OO0000O0OOO0 [0 ]#line:405
    if 'field_cajas'in O0O00OO0000O0OOO0 :#line:406
        O0O00OO0000O0OOO0 =O0O00OO0000O0OOO0 ['field_cajas']#line:407
        for OOO00OO0OO0O0OOOO in O0O00OO0000O0OOO0 :#line:408
            OOOO000O000OO0000 [OOO00OO0OO0O0OOOO ['id']]=OOO00OO0OO0O0OOOO ['caja']#line:409
    else :#line:410
        OOOO000O000OO0000 [str (O00000O0O0O000O0O )]="No hay archivos"#line:411
    return OOOO000O000OO0000 ,OO0OO0O000O0O00O0 #line:412
async def cargar_instrumental (OO00O0O0OOO0OOO0O ,OOO0OOOOO00O00OOO ):#line:414
    OO00O0000000OOO0O ={}#line:415
    OO00000000O0OOO00 =aiohttp .TCPConnector (ssl =True )#line:416
    async with aiohttp .ClientSession (connector =OO00000000O0OOO00 )as OO00O000OO0OOO0OO :#line:417
        OO000OOO0OO0O0000 =await OO00O000OO0OOO0OO .get ('https://orva.tedcas.com/api/'+str (OOO0OOOOO00O00OOO ),auth =auth )#line:418
        O00OOOOO00OOOOO0O =await OO000OOO0OO0O0000 .json ()#line:419
        for O0O0O0000OOO0O0O0 in O00OOOOO00OOOOO0O :#line:420
         if 'instrumental'in O0O0O0000OOO0O0O0 :#line:421
            for O000000O0OO0OO00O in O0O0O0000OOO0O0O0 ['instrumental']:#line:422
                if O000000O0OO0OO00O ['id']==OO00O0O0OOO0OOO0O :#line:423
                    OO00O0000000OOO0O [O0O0O0000OOO0O0O0 ['nid']]=O0O0O0000OOO0O0O0 ['title']#line:424
    return OO00O0000000OOO0O #line:425
async def cargar_botones_pdf_admision ():#line:427
    O00OO0O0O0O0O0OOO ={}#line:428
    OO00O0OOO00000OO0 ={}#line:429
    O0OOOO00OOOO0O00O ={}#line:430
    O0000O000O0000OOO ={}#line:431
    O000OO00OOOO0O00O =aiohttp .TCPConnector (ssl =True )#line:432
    async with aiohttp .ClientSession (connector =O000OO00OOOO0O00O )as OO0OO0000OOO000O0 :#line:433
        OO0O0OOO0O000OOOO =await OO0OO0000OOO000O0 .get ('https://orva.tedcas.com/api/all-content/1621',auth =auth )#line:434
        OO0OO000O00000000 =await OO0O0OOO0O000OOOO .json ()#line:435
        for OO0OO0OOOO00O0OO0 in OO0OO000O00000000 :#line:436
            OO00OOO0OOO0OO0O0 =await OO0OO0000OOO000O0 .get ('https://orva.tedcas.com/api/intervenciones/'+str (OO0OO0OOOO00O0OO0 ['nid']),auth =auth )#line:437
            OO0O0O00O00000000 =await OO00OOO0OOO0OO0O0 .json ()#line:438
            OO0O0O00O00000000 =OO0O0O00O00000000 [0 ]#line:439
            O000O0O000OO0OO00 =OO0O0O00O00000000 ['field_pdf']#line:440
            O000O0O000OO0OO00 =O000O0O000OO0OO00 [0 ]#line:441
            if OO0O0O00O00000000 ['field_tecnica']=="Mapa de camas":#line:442
                O00OO0O0O0O0O0OOO [OO0O0O00O00000000 ['title']]="https://orva.tedcas.com/"+str (O000O0O000OO0OO00 ['url'])#line:443
            elif OO0O0O00O00000000 ['field_tecnica']=="Ambulancias":#line:444
                OO00O0OOO00000OO0 [OO0O0O00O00000000 ['title']]="https://orva.tedcas.com/"+str (O000O0O000OO0OO00 ['url'])#line:445
            elif OO0O0O00O00000000 ['field_tecnica']=="Programación quirúrgica":#line:446
                O0OOOO00OOOO0O00O [OO0O0O00O00000000 ['title']]="https://orva.tedcas.com/"+str (O000O0O000OO0OO00 ['url'])#line:447
            elif OO0O0O00O00000000 ['field_tecnica']=="Otros":#line:448
                O0000O000O0000OOO [OO0O0O00O00000000 ['title']]="https://orva.tedcas.com/"+str (O000O0O000OO0OO00 ['url'])#line:449
    return O00OO0O0O0O0O0OOO ,OO00O0OOO00000OO0 ,O0OOOO00OOOO0O00O ,O0000O000O0000OOO #line:450
def remove_accents (OO000OO0O0000O000 ):#line:452
    OO0O0000O0O0O00OO =unicodedata .normalize ('NFKD',OO000OO0O0000O000 )#line:453
    return u"".join ([OOOOO0O000O0O0OOO for OOOOO0O000O0O0OOO in OO0O0000O0O0O00OO if not unicodedata .combining (OOOOO0O000O0O0OOO )])#line:454
def adaptar_salida (O0O0O000000000000 ):#line:456
    OO00O0O0O00OO0OOO =[]#line:457
    O0O0O000000000000 =str (O0O0O000000000000 ).lower ()#line:458
    O0O0O000000000000 =O0O0O000000000000 .split ("}")#line:459
    O0O0O000000000000 =O0O0O000000000000 [0 ].split (":")#line:460
    if len (O0O0O000000000000 )>=2 :#line:461
        O0OOOO0OOO000OO0O =O0O0O000000000000 [1 ].split ("'")#line:462
        OO00O0O0O00OO0OOO =O0OOOO0OOO000OO0O [1 ].split ()#line:463
    return OO00O0O0O00OO0OOO #line:464
def takeCommand ():#line:466
    OO0OO00OO0OOOO00O =sr .Recognizer ()#line:467
    with sr .Microphone ()as OOO00O0O0OOO0OOO0 :#line:468
        print ("Listening...")#line:469
        OO0OO00OO0OOOO00O .pause_threshold =1 #line:470
        OO00OO00OO0OOO0OO =OO0OO00OO0OOOO00O .adjust_for_ambient_noise (OOO00O0O0OOO0OOO0 )#line:471
        OO00OO00OO0OOO0OO =OO0OO00OO0OOOO00O .listen (OOO00O0O0OOO0OOO0 )#line:472
    try :#line:473
        print ("Recognizing...")#line:474
        OOO0OOO000O00O00O =OO0OO00OO0OOOO00O .recognize_google (OO00OO00OO0OOO0OO ,language ='es-ES')#line:475
        print (f"User said: {OOO0OOO000O00O00O}\n")#line:476
    except Exception as O00O0OOO0O0OOO00O :#line:477
        print (O00O0OOO0O0OOO00O )#line:478
        print ("Unable to Recognize your voice.")#line:479
        return "none"#line:480
    return OOO0OOO000O00O00O #line:481
app =Flask (__name__ )#line:483
app .config ['SECRET_KEY']='mysecretkey'#line:484
IMG_FOLDER =os .path .join ('static','IMG')#line:486
app .config ['UPLOAD_FOLDER']=IMG_FOLDER #line:487
@app .route ("/")#line:489
async def hello ():#line:490
    O0OO00OO0O000O0O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'trauma.jpeg')#line:491
    OO0O00OOO0O0OOO0O =os .path .join (app .config ['UPLOAD_FOLDER'],'uro.jpeg')#line:492
    O0O0OO00OO0O0O0OO =os .path .join (app .config ['UPLOAD_FOLDER'],'adm.jpeg')#line:493
    O00O0O0OOOO0OO0OO =os .path .join (app .config ['UPLOAD_FOLDER'],'tijerass.png')#line:494
    return render_template ('especialidad.html',user_image0 =O00O0O0OOOO0OO0OO ,user_image1 =O0OO00OO0O000O0O0 ,user_image2 =OO0O00OOO0O0OOO0O ,user_image3 =O0O0OO00OO0O0O0OO )#line:495
@app .route ("/especialidad")#line:497
async def especialidad ():#line:498
    O00OO0O0OO0OO0O0O =os .path .join (app .config ['UPLOAD_FOLDER'],'trauma.jpeg')#line:499
    OOOO000O00O00OOO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'uro.jpeg')#line:500
    OO000OOOOOO00O000 =os .path .join (app .config ['UPLOAD_FOLDER'],'adm.jpeg')#line:501
    OO0O0000OOOO0000O =os .path .join (app .config ['UPLOAD_FOLDER'],'tijerass.png')#line:502
    return render_template ('especialidad.html',user_image0 =OO0O0000OOOO0000O ,user_image1 =O00OO0O0OO0OO0O0O ,user_image2 =OOOO000O00O00OOO0 ,user_image3 =OO000OOOOOO00O000 )#line:503
@app .route ("/seleccion_trauma",methods =['GET','POST'])#line:505
async def seleccion_trauma ():#line:506
    OO0OO00O0000OO000 =os .path .join (app .config ['UPLOAD_FOLDER'],'lupa.png')#line:507
    OO00OO000OO0OOO00 =os .path .join (app .config ['UPLOAD_FOLDER'],'micro.png')#line:508
    O0OOO0OOOOOOOO0O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:509
    O0OOOO0O0OOOOOO0O =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:510
    return render_template ('seleccion_trauma.html',user_image4 =OO0OO00O0000OO000 ,user_image5 =OO00OO000OO0OOO00 ,user_image6 =O0OOO0OOOOOOOO0O0 ,user_image7 =O0OOOO0O0OOOOOO0O )#line:511
@app .route ("/buscador_trauma",methods =['GET','POST'])#line:513
async def buscador_trauma ():#line:514
    O00O0OOOO0O000OOO =os .path .join (app .config ['UPLOAD_FOLDER'],'lupa.png')#line:515
    O0OO00O0O0OOOO000 =os .path .join (app .config ['UPLOAD_FOLDER'],'micro.png')#line:516
    OOO00O0OO0O00O0OO =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:517
    OOOOOOOO0O00OOO00 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:518
    O0OO00O000OO0OO00 =os .path .join (app .config ['UPLOAD_FOLDER'],'guia_visual.png')#line:519
    OO0O00000OO0O000O =os .path .join (app .config ['UPLOAD_FOLDER'],'materiales.png')#line:520
    O000OOO0OOO00O000 =os .path .join (app .config ['UPLOAD_FOLDER'],'pdf_casa.jpg')#line:521
    OO00O0OOOOO0OO000 =os .path .join (app .config ['UPLOAD_FOLDER'],'protocolo.jpg')#line:522
    OO0OO00OO0000OOO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'visualizar_video.png')#line:523
    OOO00OO00OOO00OOO =str (request .form .to_dict ())#line:524
    OOO00OO00OOO00OOO =adaptar_salida (OOO00OO00OOO00OOO )#line:525
    O0OOO0OOOOO000O00 ={}#line:526
    O0OOO0OOOOO000O00 [""]=""#line:527
    if len (OOO00OO00OOO00OOO )==0 :#line:528
        return render_template ('buscador_trauma.html',result_busqueda =O0OOO0OOOOO000O00 ,user_image4 =O00O0OOOO0O000OOO ,user_image5 =O0OO00O0O0OOOO000 ,user_image6 =OOO00O0OO0O00O0OO ,user_image7 =OOOOOOOO0O00OOO00 ,user_image8 =O000OOO0OOO00O000 ,user_image9 =OO00O0OOOOO0OO000 ,user_image10 =O0OO00O000OO0OO00 ,user_image11 =OO0OO00OO0000OOO0 ,user_image12 =OO0O00000OO0O000O ,nid2 =0 )#line:529
    elif OOO00OO00OOO00OOO !=None or "{}":#line:530
        OOOOO0O000O0O00O0 =1 #line:531
        O0OO00OO0OO00OOOO =await cargar_base_datos (OOO00OO00OOO00OOO ,OOOOO0O000O0O00O0 )#line:532
        OOOO0O0O0OOO00OOO =await buscar_faq (OOO00OO00OOO00OOO ,1 )#line:533
        if O0OO00OO0OO00OOOO ==None :#line:534
            if len (OOOO0O0O0OOO00OOO )==0 :#line:535
                return render_template ('buscador_trauma.html',result_busqueda =O0OOO0OOOOO000O00 ,prediction_text ="No hay resultados para tu busqueda",user_image4 =O00O0OOOO0O000OOO ,user_image5 =O0OO00O0O0OOOO000 ,user_image6 =OOO00O0OO0O00O0OO ,user_image7 =OOOOOOOO0O00OOO00 ,user_image8 =O000OOO0OOO00O000 ,user_image9 =OO00O0OOOOO0OO000 ,user_image10 =O0OO00O000OO0OO00 ,user_image11 =OO0OO00OO0000OOO0 ,user_image12 =OO0O00000OO0O000O ,nid2 =0 )#line:536
            else :#line:537
                 return render_template ('buscador_trauma.html',faqs =OOOO0O0O0OOO00OOO ,faq_titulo ="Preguntas y respuestas: ",result_busqueda =O0OOO0OOOOO000O00 ,user_image4 =O00O0OOOO0O000OOO ,user_image5 =O0OO00O0O0OOOO000 ,user_image6 =OOO00O0OO0O00O0OO ,user_image7 =OOOOOOOO0O00OOO00 ,user_image8 =O000OOO0OOO00O000 ,user_image9 =OO00O0OOOOO0OO000 ,user_image10 =O0OO00O000OO0OO00 ,user_image11 =OO0OO00OO0000OOO0 ,user_image12 =OO0O00000OO0O000O ,nid2 =0 )#line:538
        elif len (O0OO00OO0OO00OOOO )>=1 :#line:539
            OOOOOO0OO0OOOOO00 =[]#line:540
            OOO00OO0000000O00 =[]#line:541
            O0OOO0OOOOO000O00 ={}#line:542
            for O0O00000OO0O0000O in O0OO00OO0OO00OOOO :#line:543
                OOOOOO0OO0OOOOO00 .append (O0O00000OO0O0000O ["title"])#line:544
                OOO00OO0000000O00 .append (O0O00000OO0O0000O ["nid"])#line:545
            for O0O00O000OOO0OO00 ,O0O00000OO0O0000O in enumerate (OOOOOO0OO0OOOOO00 ):#line:546
                 O0OOO0OOOOO000O00 [OOO00OO0000000O00 [O0O00O000OOO0OO00 ]]=O0O00000OO0O0000O #line:547
            if len (OOOO0O0O0OOO00OOO )!=0 :#line:549
                return render_template ('buscador_trauma.html',faqs =OOOO0O0O0OOO00OOO ,faq_titulo ="Preguntas y respuestas: ",result_busqueda =O0OOO0OOOOO000O00 ,user_image4 =O00O0OOOO0O000OOO ,user_image5 =O0OO00O0O0OOOO000 ,user_image6 =OOO00O0OO0O00O0OO ,user_image7 =OOOOOOOO0O00OOO00 ,user_image8 =O000OOO0OOO00O000 ,user_image9 =OO00O0OOOOO0OO000 ,user_image10 =O0OO00O000OO0OO00 ,user_image11 =OO0OO00OO0000OOO0 ,user_image12 =OO0O00000OO0O000O ,nid2 =0 )#line:550
            else :#line:551
                return render_template ('buscador_trauma.html',result_busqueda =O0OOO0OOOOO000O00 ,user_image4 =O00O0OOOO0O000OOO ,user_image5 =O0OO00O0O0OOOO000 ,user_image6 =OOO00O0OO0O00O0OO ,user_image7 =OOOOOOOO0O00OOO00 ,user_image8 =O000OOO0OOO00O000 ,user_image9 =OO00O0OOOOO0OO000 ,user_image10 =O0OO00O000OO0OO00 ,user_image11 =OO0OO00OO0000OOO0 ,user_image12 =OO0O00000OO0O000O ,nid2 =0 )#line:552
@app .route ("/resultado_trauma",methods =['GET','POST'])#line:554
async def resultado_trauma ():#line:555
    O000OOO000OO0OOO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:556
    OOO0O00O000O0OO00 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:557
    O0000OO0O0O0OO00O =os .path .join (app .config ['UPLOAD_FOLDER'],'guia_visual.png')#line:558
    O0O00O00O00OO00O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'materiales.png')#line:559
    O00O00O0O0OOO00OO =os .path .join (app .config ['UPLOAD_FOLDER'],'pdf_casa.jpg')#line:560
    O000O00OO000O0OOO =os .path .join (app .config ['UPLOAD_FOLDER'],'protocolo.jpg')#line:561
    O0OO0OOO0O0000OO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'visualizar_video.png')#line:562
    O0OOO0OO0OOOOOO0O =request .args .get ('link')#line:563
    OOO00OO000OOOO00O ,OOOOOO0O0OO00O00O =await cargar_tipo (O0OOO0OO0OOOOOO0O ,1 )#line:564
    O0O0OO0OOO0O00O0O =OOO00OO000OOOO00O ['title']#line:565
    if OOOOOO0O0OO00O00O =="Intervencion":#line:567
        OOO0000000OO0OOO0 ,O0OO0OOO00O0000OO =await cargar_caja (str (O0OOO0OO0OOOOOO0O ),'Materiales - Cajas: ')#line:568
        return render_template ('intervencion_trauma.html',user_image8 =O00O00O0O0OOO00OO ,user_image9 =O000O00OO000O0OOO ,user_image10 =O0000OO0O0O0OO00O ,user_image11 =O0OO0OOO0O0000OO0 ,user_image12 =O0O00O00O00OO00O0 ,instrumental =OOO0000000OO0OOO0 ,texto_cajas =O0OO0OOO00O0000OO ,title =O0O0OO0OOO0O00O0O ,user_image6 =O000OOO000OO0OOO0 ,user_image7 =OOO0O00O000O0OO00 ,nid2 =O0OOO0OO0OOOOOO0O )#line:569
    elif OOOOOO0O0OO00O00O =='Caja':#line:570
        OOO0OOO000OOO0O00 ,O000OOO0000O0O000 ,OOOO00OOOO000000O =await cargar_archivo ("ubicacion","Ubicacion: ","cajas/"+str (O0OOO0OO0OOOOOO0O ))#line:571
        O00000OOOO00O0O0O =await cargar_archivo ("image","Imagen: ","cajas/"+str (O0OOO0OO0OOOOOO0O ))#line:572
        O00OO0O0OO00O0OOO ,OO0OOO0OOO0OOOOO0 =await cargar_archivo_grande ("title_material","Material : ","cajas/"+str (O0OOO0OO0OOOOOO0O ))#line:573
        return render_template ('caja_trauma.html',title =O0O0OO0OOO0O00O0O ,files_instru =O00OO0O0OO00O0OOO ,texto_instru =OO0OOO0OOO0OOOOO0 ,texto_ubi =OOO0OOO000OOO0O00 ,file_texto_ubi =OOOO00OOOO000000O ,file_imagen =O00000OOOO00O0O0O ,user_image6 =O000OOO000OO0OOO0 ,user_image7 =OOO0O00O000O0OO00 )#line:574
    elif OOOOOO0O0OO00O00O =='Instrumental':#line:575
        OO000O0OOOO0O00OO =await cargar_instrumental (O0OOO0OO0OOOOOO0O ,'listado_completo_cajas/1')#line:576
        return render_template ('instrumental_trauma.html',cajas =OO000O0OOOO0O00OO ,texto ='El instrumental que buscas esta presente en las siguientes cajas: ',title =O0O0OO0OOO0O00O0O ,user_image6 =O000OOO000OO0OOO0 ,user_image7 =OOO0O00O000O0OO00 )#line:577
@app .route ("/protocolos_trauma",methods =['GET','POST'])#line:579
async def protocolos_trauma ():#line:580
    OOO00OOOOO00O0OO0 =request .args .get ('link2')#line:581
    O0O0OO00000O00O00 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:582
    O000OOO000OO00O00 =await boton_word_ppt (1 ,"field_protocolo",OOO00OOOOO00O0OO0 )#line:583
    return render_template ('protocolo.html',protocolos =O000OOO000OO00O00 ,user_image7 =O0O0OO00000O00O00 )#line:584
@app .route ("/guia_visual_trauma",methods =['GET','POST'])#line:586
async def guia_visual_trauma ():#line:587
    O0O0OO0O0O0OO0O0O =request .args .get ('link2')#line:588
    OOOO0O0O00000O000 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:589
    O0OO00O00O0OO0OOO =await boton_word_ppt (1 ,"field_guia_visual",O0O0OO0O0O0OO0O0O )#line:590
    return render_template ('guia_visual.html',guia_visual =O0OO00O00O0OO0OOO ,user_image7 =OOOO0O0O00000O000 )#line:591
@app .route ("/pdf_casa_trauma",methods =['GET','POST'])#line:593
async def pdf_casa_trauma ():#line:594
    OOOOOO0OOOOOO000O =request .args .get ('link2')#line:595
    O0OO0O0OOO000OO0O =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:596
    O000O0OO000O000O0 =await boton_pdf_video (1 ,"field_pdf",OOOOOO0OOOOOO000O )#line:597
    return render_template ('pdf_casa_comercial.html',user_image7 =O0OO0O0OOO000OO0O ,titulos =O000O0OO000O000O0 )#line:598
@app .route ("/videos_trauma",methods =['GET','POST'])#line:600
async def videos_trauma ():#line:601
    O0OO0OO00O00O0OO0 =request .args .get ('link2')#line:602
    OOOOO0OOOOOO0OOOO =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:603
    O0OOOO0000OO000O0 =await boton_pdf_video (1 ,"field_video",O0OO0OO00O00O0OO0 )#line:604
    return render_template ('videos.html',user_image7 =OOOOO0OOOOOO0OOOO ,titulos =O0OOOO0000OO000O0 )#line:605
@app .route ("/materiales_trauma",methods =['GET','POST'])#line:607
async def materiales_trauma ():#line:608
    OOOO0000000O00O0O =request .args .get ('link2')#line:609
    OO00O000OO0OOOOOO =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:610
    O0O0O0OO0OOOOOO0O =await boton_materiales (1 ,OOOO0000000O00O0O )#line:611
    if len (O0O0O0OO0OOOOOO0O [''])==0 :#line:612
       return render_template ('materiales.html',user_image7 =OO00O000OO0OOOOOO ,cajas =O0O0O0OO0OOOOOO0O ,no_hay ="No hay materiales")#line:613
    return render_template ('materiales.html',user_image7 =OO00O000OO0OOOOOO ,cajas =O0O0O0OO0OOOOOO0O )#line:614
@app .route ("/escuchar_trauma1",methods =['GET','POST'])#line:616
async def escuchar_trauma1 ():#line:617
    OOO000O0O00OOO00O =os .path .join (app .config ['UPLOAD_FOLDER'],'guia_visual.png')#line:618
    O00OO00OO0O00O000 =os .path .join (app .config ['UPLOAD_FOLDER'],'materiales.png')#line:619
    O0O0OOOOOO0OOO00O =os .path .join (app .config ['UPLOAD_FOLDER'],'pdf_casa.jpg')#line:620
    O00OO0OO000O0000O =os .path .join (app .config ['UPLOAD_FOLDER'],'protocolo.jpg')#line:621
    OO00OO000O0OO0O0O =os .path .join (app .config ['UPLOAD_FOLDER'],'visualizar_video.png')#line:622
    OO000O0OO0000O0OO =os .path .join (app .config ['UPLOAD_FOLDER'],'micro.png')#line:623
    OO0000OO00OO00000 =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:624
    O0O0000OOOO0O00OO =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:625
    return render_template ('escuchar_trauma1.html',nid2 =0 ,prediction_text ="Dale a `Escuchar´ y haz tu pregunta",user_image5 =OO000O0OO0000O0OO ,user_image6 =OO0000OO00OO00000 ,user_image7 =O0O0000OOOO0O00OO ,user_image8 =O0O0OOOOOO0OOO00O ,user_image9 =O00OO0OO000O0000O ,user_image10 =OOO000O0O00OOO00O ,user_image11 =OO00OO000O0OO0O0O ,user_image12 =O00OO00OO0O00O000 )#line:626
@app .route ("/escuchar_trauma",methods =['GET','POST'])#line:628
async def escuchar_trauma ():#line:629
    O00OOO0OOOOO0O0OO =os .path .join (app .config ['UPLOAD_FOLDER'],'guia_visual.png')#line:630
    OO0O000OOOO0OOOO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'materiales.png')#line:631
    OOO0OOOO0000O0OOO =os .path .join (app .config ['UPLOAD_FOLDER'],'pdf_casa.jpg')#line:632
    O0000000O0O0O00OO =os .path .join (app .config ['UPLOAD_FOLDER'],'protocolo.jpg')#line:633
    OOO00000O0000OO00 =os .path .join (app .config ['UPLOAD_FOLDER'],'visualizar_video.png')#line:634
    O0OO0O0OO00000000 =os .path .join (app .config ['UPLOAD_FOLDER'],'micro.png')#line:635
    OO00000OOOOO000OO =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:636
    OO0O0000OO0O00O00 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:637
    OOO000OOOO000O000 =takeCommand ()#line:638
    OOO000OOOO000O000 =str (OOO000OOOO000O000 ).lower ()#line:639
    OOO000OOOO000O000 =OOO000OOOO000O000 .split ()#line:640
    OO00000O0O00OO000 ={}#line:641
    OO00000O0O00OO000 [""]=""#line:642
    if OOO000OOOO000O000 [0 ]!="none":#line:643
        O000O0OO00OOOOO00 =1 #line:644
        O0OO0O00OOO00OO00 =await cargar_base_datos (OOO000OOOO000O000 ,O000O0OO00OOOOO00 )#line:645
        O00OO00OO000OOO0O =await buscar_faq (OOO000OOOO000O000 ,0 )#line:646
        if O0OO0O00OOO00OO00 ==None :#line:647
            if len (O00OO00OO000OOO0O )==0 :#line:648
                return render_template ('escuchar_trauma.html',nid2 =0 ,result_busqueda =OO00000O0O00OO000 ,prediction_text ="No hay resultados para tu busqueda",user_image6 =OO00000OOOOO000OO ,user_image7 =OO0O0000OO0O00O00 ,user_image5 =O0OO0O0OO00000000 ,user_image8 =OOO0OOOO0000O0OOO ,user_image9 =O0000000O0O0O00OO ,user_image10 =O00OOO0OOOOO0O0OO ,user_image11 =OOO00000O0000OO00 ,user_image12 =OO0O000OOOO0OOOO0 )#line:649
            else :#line:650
                return render_template ('escuchar_trauma.html',nid2 =0 ,faqs =O00OO00OO000OOO0O ,faq_titulo ="Preguntas y respuestas: ",result_busqueda =OO00000O0O00OO000 ,user_image6 =OO00000OOOOO000OO ,user_image7 =OO0O0000OO0O00O00 ,user_image5 =O0OO0O0OO00000000 ,user_image8 =OOO0OOOO0000O0OOO ,user_image9 =O0000000O0O0O00OO ,user_image10 =O00OOO0OOOOO0O0OO ,user_image11 =OOO00000O0000OO00 ,user_image12 =OO0O000OOOO0OOOO0 )#line:651
        elif len (O0OO0O00OOO00OO00 )>=1 :#line:652
            OOOOO00000O000OO0 =[]#line:653
            O0000000O0000OO0O =[]#line:654
            OO00000O0O00OO000 ={}#line:655
            for O0O0OO0OO0OO00000 in O0OO0O00OOO00OO00 :#line:656
                OOOOO00000O000OO0 .append (O0O0OO0OO0OO00000 ["title"])#line:657
                O0000000O0000OO0O .append (O0O0OO0OO0OO00000 ["nid"])#line:658
            for OO0O0OO00O0OOO0O0 ,O0O0OO0OO0OO00000 in enumerate (OOOOO00000O000OO0 ):#line:659
                 OO00000O0O00OO000 [O0000000O0000OO0O [OO0O0OO00O0OOO0O0 ]]=O0O0OO0OO0OO00000 #line:660
            if len (O00OO00OO000OOO0O )==0 :#line:662
                return render_template ('escuchar_trauma.html',nid2 =0 ,result_busqueda =OO00000O0O00OO000 ,user_image6 =OO00000OOOOO000OO ,user_image7 =OO0O0000OO0O00O00 ,user_image5 =O0OO0O0OO00000000 ,user_image8 =OOO0OOOO0000O0OOO ,user_image9 =O0000000O0O0O00OO ,user_image10 =O00OOO0OOOOO0O0OO ,user_image11 =OOO00000O0000OO00 ,user_image12 =OO0O000OOOO0OOOO0 )#line:663
            else :#line:664
                return render_template ('escuchar_trauma.html',nid2 =0 ,faqs =O00OO00OO000OOO0O ,faq_titulo ="Preguntas y respuestas: ",result_busqueda =OO00000O0O00OO000 ,user_image6 =OO00000OOOOO000OO ,user_image7 =OO0O0000OO0O00O00 ,user_image5 =O0OO0O0OO00000000 ,user_image8 =OOO0OOOO0000O0OOO ,user_image9 =O0000000O0O0O00OO ,user_image10 =O00OOO0OOOOO0O0OO ,user_image11 =OOO00000O0000OO00 ,user_image12 =OO0O000OOOO0OOOO0 )#line:665
    else :#line:666
        return render_template ('escuchar_trauma.html',nid2 =0 ,result_busqueda =OO00000O0O00OO000 ,prediction_text ="No te he entendido bien, dale al boton `Escuchar´ y repite tu pregunta",user_image5 =O0OO0O0OO00000000 ,user_image6 =OO00000OOOOO000OO ,user_image7 =OO0O0000OO0O00O00 ,user_image8 =OOO0OOOO0000O0OOO ,user_image9 =O0000000O0O0O00OO ,user_image10 =O00OOO0OOOOO0O0OO ,user_image11 =OOO00000O0000OO00 ,user_image12 =OO0O000OOOO0OOOO0 )#line:667
@app .route ("/buscador_admision",methods =['GET','POST'])#line:669
async def buscador_admision ():#line:670
    OOO000O00OOOO0OOO =os .path .join (app .config ['UPLOAD_FOLDER'],'lupa.png')#line:671
    OO0OOO00OOOOOOO0O =os .path .join (app .config ['UPLOAD_FOLDER'],'micro.png')#line:672
    O00OOOO00OO0O00OO =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:673
    OOOO0O0000O00O0OO =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:674
    OO00000OOOOOO0000 =os .path .join (app .config ['UPLOAD_FOLDER'],'otros_img.png')#line:675
    O0O000000OO000OO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'programacion_img.png')#line:676
    O0OO0OOO000O000O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'ambulancias_img.jpg')#line:677
    O0O0O0OOO000O0O00 =os .path .join (app .config ['UPLOAD_FOLDER'],'mapa_camas_img.jpg')#line:678
    O000O0O000O0000O0 =str (request .form .to_dict ())#line:679
    O000O0O000O0000O0 =adaptar_salida (O000O0O000O0000O0 )#line:680
    O0000OOOOOOO00O0O ={}#line:681
    O0000OOOOOOO00O0O [""]=""#line:682
    if len (O000O0O000O0000O0 )==0 :#line:683
        return render_template ('buscador_admision.html',user_image8 =O0O0O0OOO000O0O00 ,user_image9 =O0OO0OOO000O000O0 ,user_image10 =O0O000000OO000OO0 ,user_image11 =OO00000OOOOOO0000 ,result_busqueda =O0000OOOOOOO00O0O ,prediction_text ="ya puedes hacer tu pregunta",user_image4 =OOO000O00OOOO0OOO ,user_image5 =OO0OOO00OOOOOOO0O ,user_image6 =O00OOOO00OO0O00OO ,user_image7 =OOOO0O0000O00O0OO )#line:684
    elif O000O0O000O0000O0 !=None or "{}":#line:685
        OO0000OO0000OO0O0 =1621 #line:686
        OO0OOOOOOO00OOO00 =await cargar_base_datos (O000O0O000O0000O0 ,OO0000OO0000OO0O0 )#line:687
        OO0O000000OO0O0O0 =await buscar_faq (O000O0O000O0000O0 ,1 )#line:688
        if OO0OOOOOOO00OOO00 ==None :#line:689
            if len (OO0O000000OO0O0O0 )==0 :#line:690
                return render_template ('buscador_admision.html',user_image8 =O0O0O0OOO000O0O00 ,user_image9 =O0OO0OOO000O000O0 ,user_image10 =O0O000000OO000OO0 ,user_image11 =OO00000OOOOOO0000 ,result_busqueda =O0000OOOOOOO00O0O ,prediction_text ="No hay resultados para tu busqueda",user_image4 =OOO000O00OOOO0OOO ,user_image5 =OO0OOO00OOOOOOO0O ,user_image6 =O00OOOO00OO0O00OO ,user_image7 =OOOO0O0000O00O0OO )#line:691
            else :#line:692
                return render_template ('buscador_admision.html',user_image8 =O0O0O0OOO000O0O00 ,user_image9 =O0OO0OOO000O000O0 ,user_image10 =O0O000000OO000OO0 ,user_image11 =OO00000OOOOOO0000 ,faqs =OO0O000000OO0O0O0 ,faq_titulo ="Preguntas y respuestas: ",result_busqueda =O0000OOOOOOO00O0O ,user_image4 =OOO000O00OOOO0OOO ,user_image5 =OO0OOO00OOOOOOO0O ,user_image6 =O00OOOO00OO0O00OO ,user_image7 =OOOO0O0000O00O0OO )#line:693
        elif len (OO0OOOOOOO00OOO00 )>=1 :#line:694
            OOOOOO00OOO0OO000 =[]#line:695
            O00O00000OOOO00OO =[]#line:696
            O0000OOOOOOO00O0O ={}#line:697
            for OOO00O0O00O000000 in OO0OOOOOOO00OOO00 :#line:698
                O00O00000OOOO00OO .append (OOO00O0O00O000000 ["nid"])#line:699
                for OOO0O0OO000O00O0O in O00O00000OOOO00OO :#line:700
                    OO000O0O0OOOOOO00 =aiohttp .TCPConnector (ssl =True )#line:701
                    async with aiohttp .ClientSession (connector =OO000O0O0OOOOOO00 )as O0O00O0OOO00000O0 :#line:702
                        O0O0000O0O0OOOO00 =await O0O00O0OOO00000O0 .get ('https://orva.tedcas.com/api/intervenciones/'+str (OOO0O0OO000O00O0O ),auth =auth )#line:703
                        O0O0O0OOOO0O0O000 =await O0O0000O0O0OOOO00 .json ()#line:704
                        O0O0O0OOOO0O0O000 =O0O0O0OOOO0O0O000 [0 ]#line:705
                        O00O00O0OO0OO000O =O0O0O0OOOO0O0O000 ['field_pdf']#line:706
                        O00O00O0OO0OO000O =O00O00O0OO0OO000O [0 ]#line:707
                        O0000OOOOOOO00O0O [O0O0O0OOOO0O0O000 ['title']]="https://orva.tedcas.com/"+str (O00O00O0OO0OO000O ['url'])#line:708
            if len (OO0O000000OO0O0O0 )==0 :#line:709
                return render_template ('buscador_admision.html',user_image8 =O0O0O0OOO000O0O00 ,user_image9 =O0OO0OOO000O000O0 ,user_image10 =O0O000000OO000OO0 ,user_image11 =OO00000OOOOOO0000 ,result_busqueda =O0000OOOOOOO00O0O ,user_image4 =OOO000O00OOOO0OOO ,user_image5 =OO0OOO00OOOOOOO0O ,user_image6 =O00OOOO00OO0O00OO ,user_image7 =OOOO0O0000O00O0OO )#line:710
            else :#line:711
                return render_template ('buscador_admision.html',faqs =OO0O000000OO0O0O0 ,faq_titulo ="Preguntas y respuestas: ",user_image8 =O0O0O0OOO000O0O00 ,user_image9 =O0OO0OOO000O000O0 ,user_image10 =O0O000000OO000OO0 ,user_image11 =OO00000OOOOOO0000 ,result_busqueda =O0000OOOOOOO00O0O ,user_image4 =OOO000O00OOOO0OOO ,user_image5 =OO0OOO00OOOOOOO0O ,user_image6 =O00OOOO00OO0O00OO ,user_image7 =OOOO0O0000O00O0OO )#line:712
@app .route ("/mapa_camas",methods =['GET','POST'])#line:714
async def mapa_camas ():#line:715
    O0O00OOO0000000O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:716
    O000O0OO0O00OOO00 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:717
    O00O0O000O000OOOO ,O0000OO0O00O0OO00 ,OOOOOOO0000O0OO00 ,OOOO0O0O00OOO0OO0 =await cargar_botones_pdf_admision ()#line:718
    return render_template ('mapa_camas.html',text =O00O0O000O000OOOO ,user_image6 =O0O00OOO0000000O0 ,user_image7 =O000O0OO0O00OOO00 )#line:719
@app .route ("/ambulancias",methods =['GET','POST'])#line:721
async def ambulancias ():#line:722
    OOO00OOOOO0000000 =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:723
    OOOOO0O00O0O0O00O =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:724
    OOO00O0O0OO0O00OO ,O0OO0O0000O00OOO0 ,OOO0OOO00OO0OOOO0 ,OOO00OO00000O0OO0 =await cargar_botones_pdf_admision ()#line:725
    return render_template ('ambulancias.html',text =O0OO0O0000O00OOO0 ,user_image6 =OOO00OOOOO0000000 ,user_image7 =OOOOO0O00O0O0O00O )#line:726
@app .route ("/programacion_quirurgica",methods =['GET','POST'])#line:728
async def programacion_quirurgica ():#line:729
    OO00O000O0OO000O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:730
    O00O0O0O0OO00OOO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:731
    O00OO0O0OOO00OOO0 ,O0O000OO0O0O000O0 ,OOO0OO00OOOOO00OO ,O00OOO0OO000O0O00 =await cargar_botones_pdf_admision ()#line:732
    return render_template ('programacion_quirurgica.html',text =OOO0OO00OOOOO00OO ,user_image6 =OO00O000O0OO000O0 ,user_image7 =O00O0O0O0OO00OOO0 )#line:733
@app .route ("/otros",methods =['GET','POST'])#line:735
async def otros ():#line:736
    OOO0OOOO00O00000O =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:737
    O0OOO0O0000OO0000 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:738
    O00OOOO000OOOOO00 ,O00OOO00OO0O0OO00 ,O0O0OO0O0O0000OO0 ,O0OOO0000OOOOO000 =await cargar_botones_pdf_admision ()#line:739
    return render_template ('otros.html',text =O0OOO0000OOOOO000 ,user_image6 =OOO0OOOO00O00000O ,user_image7 =O0OOO0O0000OO0000 )#line:740
@app .route ("/escuchar_admision1",methods =['GET','POST'])#line:742
async def escuchar_admision1 ():#line:743
    O00OOOOO00OOO00OO =os .path .join (app .config ['UPLOAD_FOLDER'],'otros_img.png')#line:744
    O0OOOO00O0O0O000O =os .path .join (app .config ['UPLOAD_FOLDER'],'programacion_img.png')#line:745
    OO0OOOOOO000O00O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'ambulancias_img.jpg')#line:746
    OO000OOO000OOOOOO =os .path .join (app .config ['UPLOAD_FOLDER'],'mapa_camas_img.jpg')#line:747
    O0O000OOOO00OO0OO =os .path .join (app .config ['UPLOAD_FOLDER'],'micro.png')#line:748
    OOOOO0O0OO000O000 =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:749
    O0O0O00OO000OOO0O =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:750
    return render_template ('escuchar_admision1.html',user_image8 =OO000OOO000OOOOOO ,user_image9 =OO0OOOOOO000O00O0 ,user_image10 =O0OOOO00O0O0O000O ,user_image11 =O00OOOOO00OOO00OO ,prediction_text ="Dale a `Escuchar´ y haz tu pregunta",user_image5 =O0O000OOOO00OO0OO ,user_image6 =OOOOO0O0OO000O000 ,user_image7 =O0O0O00OO000OOO0O )#line:751
@app .route ("/escuchar_admision",methods =['GET','POST'])#line:753
async def escuchar_admision ():#line:754
    OO000O0000O0OOOOO =os .path .join (app .config ['UPLOAD_FOLDER'],'otros_img.png')#line:755
    O00OO000OO0OOO000 =os .path .join (app .config ['UPLOAD_FOLDER'],'programacion_img.png')#line:756
    OO00O00OO0OOO0000 =os .path .join (app .config ['UPLOAD_FOLDER'],'ambulancias_img.jpg')#line:757
    OOO0000O0OOOO0OOO =os .path .join (app .config ['UPLOAD_FOLDER'],'mapa_camas_img.jpg')#line:758
    O000000000O000OO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'lupa.png')#line:759
    O0OO0O0OOO000O000 =os .path .join (app .config ['UPLOAD_FOLDER'],'micro.png')#line:760
    OOO0O00O0O000OOOO =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:761
    OOOO0OOO0OO0OOOO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:762
    OO00OOOO00O0O0OOO =takeCommand ()#line:763
    OO00OOOO00O0O0OOO =str (OO00OOOO00O0O0OOO ).lower ()#line:764
    OO00OOOO00O0O0OOO =OO00OOOO00O0O0OOO .split ()#line:765
    O0O00000OOO0OO0O0 ={}#line:766
    O0O00000OOO0OO0O0 [""]=""#line:767
    if OO00OOOO00O0O0OOO [0 ]!="none":#line:768
        OOO0000O0OO00OO00 =1621 #line:769
        O0OO00OOO0OO0O000 =await cargar_base_datos (OO00OOOO00O0O0OOO ,OOO0000O0OO00OO00 )#line:770
        O000O0O0O0OO00OOO =await buscar_faq (OO00OOOO00O0O0OOO ,0 )#line:771
        if O0OO00OOO0OO0O000 ==None :#line:772
            if len (O000O0O0O0OO00OOO )==0 :#line:773
                return render_template ('escuchar_admision.html',user_image8 =OOO0000O0OOOO0OOO ,user_image9 =OO00O00OO0OOO0000 ,user_image10 =O00OO000OO0OOO000 ,user_image11 =OO000O0000O0OOOOO ,result_busqueda =O0O00000OOO0OO0O0 ,prediction_text ="No hay resultados para tu busqueda",user_image4 =O000000000O000OO0 ,user_image5 =O0OO0O0OOO000O000 ,user_image6 =OOO0O00O0O000OOOO ,user_image7 =OOOO0OOO0OO0OOOO0 )#line:774
            else :#line:775
                return render_template ('escuchar_admision.html',faqs =O000O0O0O0OO00OOO ,faq_titulo ="Preguntas y respuestas: ",user_image8 =OOO0000O0OOOO0OOO ,user_image9 =OO00O00OO0OOO0000 ,user_image10 =O00OO000OO0OOO000 ,user_image11 =OO000O0000O0OOOOO ,result_busqueda =O0O00000OOO0OO0O0 ,user_image4 =O000000000O000OO0 ,user_image5 =O0OO0O0OOO000O000 ,user_image6 =OOO0O00O0O000OOOO ,user_image7 =OOOO0OOO0OO0OOOO0 )#line:776
        elif len (O0OO00OOO0OO0O000 )>=1 :#line:777
            OO00O000OOO0OOO0O =[]#line:778
            O0000O0000OOO0000 =[]#line:779
            O0O00000OOO0OO0O0 ={}#line:780
            for OOOOOOOOOOOO00OOO in O0OO00OOO0OO0O000 :#line:781
                O0000O0000OOO0000 .append (OOOOOOOOOOOO00OOO ["nid"])#line:782
                for O0O000OOOO0000OOO in O0000O0000OOO0000 :#line:783
                    OO0O0OO000O00000O =aiohttp .TCPConnector (ssl =True )#line:784
                    async with aiohttp .ClientSession (connector =OO0O0OO000O00000O )as OO00OO0OO0OOOOOO0 :#line:785
                        O00000OO0000000OO =await OO00OO0OO0OOOOOO0 .get ('https://orva.tedcas.com/api/intervenciones/'+str (O0O000OOOO0000OOO ),auth =auth )#line:786
                        O0OO0OOOO0O0000O0 =await O00000OO0000000OO .json ()#line:787
                        O0OO0OOOO0O0000O0 =O0OO0OOOO0O0000O0 [0 ]#line:788
                        OOOOOO0OOO00O0O0O =O0OO0OOOO0O0000O0 ['field_pdf']#line:789
                        OOOOOO0OOO00O0O0O =OOOOOO0OOO00O0O0O [0 ]#line:790
                        O0O00000OOO0OO0O0 [O0OO0OOOO0O0000O0 ['title']]="https://orva.tedcas.com/"+str (OOOOOO0OOO00O0O0O ['url'])#line:791
            if len (O000O0O0O0OO00OOO )==0 :#line:792
                return render_template ('escuchar_admision.html',user_image8 =OOO0000O0OOOO0OOO ,user_image9 =OO00O00OO0OOO0000 ,user_image10 =O00OO000OO0OOO000 ,user_image11 =OO000O0000O0OOOOO ,result_busqueda =O0O00000OOO0OO0O0 ,user_image4 =O000000000O000OO0 ,user_image5 =O0OO0O0OOO000O000 ,user_image6 =OOO0O00O0O000OOOO ,user_image7 =OOOO0OOO0OO0OOOO0 )#line:793
            else :#line:794
                return render_template ('escuchar_admision.html',faqs =O000O0O0O0OO00OOO ,faq_titulo ="Preguntas y respuestas: ",user_image8 =OOO0000O0OOOO0OOO ,user_image9 =OO00O00OO0OOO0000 ,user_image10 =O00OO000OO0OOO000 ,user_image11 =OO000O0000O0OOOOO ,result_busqueda =O0O00000OOO0OO0O0 ,user_image4 =O000000000O000OO0 ,user_image5 =O0OO0O0OOO000O000 ,user_image6 =OOO0O00O0O000OOOO ,user_image7 =OOOO0OOO0OO0OOOO0 )#line:795
    else :#line:796
        return render_template ('escuchar_admision.html',user_image8 =OOO0000O0OOOO0OOO ,user_image9 =OO00O00OO0OOO0000 ,user_image10 =O00OO000OO0OOO000 ,user_image11 =OO000O0000O0OOOOO ,prediction_text ="No te he entendido bien, dale al boton `Escuchar´ y repite tu pregunta",result_busqueda =O0O00000OOO0OO0O0 ,user_image4 =O000000000O000OO0 ,user_image5 =O0OO0O0OOO000O000 ,user_image6 =OOO0O00O0O000OOOO ,user_image7 =OOOO0OOO0OO0OOOO0 )#line:797
@app .route ("/buscador_uro",methods =['GET','POST'])#line:799
async def buscador_uro ():#line:800
    O0O00OOO0OO0OOO00 =os .path .join (app .config ['UPLOAD_FOLDER'],'lupa.png')#line:801
    OOO000OO0OOO0O00O =os .path .join (app .config ['UPLOAD_FOLDER'],'micro.png')#line:802
    OO0O0O000O000O000 =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:803
    OO00O00O00O0OOO0O =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:804
    OO0000000OO0OO000 =os .path .join (app .config ['UPLOAD_FOLDER'],'guia_visual.png')#line:805
    O00O000O00OO0O0O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'materiales.png')#line:806
    OO0000O0OO00OOOOO =os .path .join (app .config ['UPLOAD_FOLDER'],'pdf_casa.jpg')#line:807
    OOO0OO0OO000OO0O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'protocolo.jpg')#line:808
    O00O000O000O0OO0O =os .path .join (app .config ['UPLOAD_FOLDER'],'visualizar_video.png')#line:809
    O0OOO000OO00OO0OO =str (request .form .to_dict ())#line:810
    O0OOO000OO00OO0OO =adaptar_salida (O0OOO000OO00OO0OO )#line:811
    O0OOO0O0000OO0OOO ={}#line:812
    O0OOO0O0000OO0OOO [""]=""#line:813
    if len (O0OOO000OO00OO0OO )==0 :#line:814
        return render_template ('buscador_uro.html',result_busqueda =O0OOO0O0000OO0OOO ,user_image4 =O0O00OOO0OO0OOO00 ,user_image5 =OOO000OO0OOO0O00O ,user_image6 =OO0O0O000O000O000 ,user_image7 =OO00O00O00O0OOO0O ,user_image8 =OO0000O0OO00OOOOO ,user_image9 =OOO0OO0OO000OO0O0 ,user_image10 =OO0000000OO0OO000 ,user_image11 =O00O000O000O0OO0O ,user_image12 =O00O000O00OO0O0O0 ,nid2 =0 )#line:815
    elif O0OOO000OO00OO0OO !=None or "{}":#line:816
        OO0OO0OOOO000OO0O =1620 #line:817
        OOO000O0000000O00 =await cargar_base_datos (O0OOO000OO00OO0OO ,OO0OO0OOOO000OO0O )#line:818
        OO0O00OOO0O000O0O =await buscar_faq (O0OOO000OO00OO0OO ,1 )#line:819
        if OOO000O0000000O00 ==None :#line:820
            if len (OO0O00OOO0O000O0O )==0 :#line:821
                return render_template ('buscador_uro.html',result_busqueda =O0OOO0O0000OO0OOO ,prediction_text ="No hay resultados para tu busqueda",user_image4 =O0O00OOO0OO0OOO00 ,user_image5 =OOO000OO0OOO0O00O ,user_image6 =OO0O0O000O000O000 ,user_image7 =OO00O00O00O0OOO0O ,user_image8 =OO0000O0OO00OOOOO ,user_image9 =OOO0OO0OO000OO0O0 ,user_image10 =OO0000000OO0OO000 ,user_image11 =O00O000O000O0OO0O ,user_image12 =O00O000O00OO0O0O0 ,nid2 =0 )#line:822
            else :#line:823
                 return render_template ('buscador_uro.html',faqs =OO0O00OOO0O000O0O ,faq_titulo ="Preguntas y respuestas: ",result_busqueda =O0OOO0O0000OO0OOO ,user_image4 =O0O00OOO0OO0OOO00 ,user_image5 =OOO000OO0OOO0O00O ,user_image6 =OO0O0O000O000O000 ,user_image7 =OO00O00O00O0OOO0O ,user_image8 =OO0000O0OO00OOOOO ,user_image9 =OOO0OO0OO000OO0O0 ,user_image10 =OO0000000OO0OO000 ,user_image11 =O00O000O000O0OO0O ,user_image12 =O00O000O00OO0O0O0 ,nid2 =0 )#line:824
        elif len (OOO000O0000000O00 )>=1 :#line:825
            OOO0OO0O000O00OO0 =[]#line:826
            OO000O0OOOOOOO000 =[]#line:827
            O0OOO0O0000OO0OOO ={}#line:828
            for OO0OO0000OO00OO00 in OOO000O0000000O00 :#line:829
                OOO0OO0O000O00OO0 .append (OO0OO0000OO00OO00 ["title"])#line:830
                OO000O0OOOOOOO000 .append (OO0OO0000OO00OO00 ["nid"])#line:831
            for OO0000O0O0OO0000O ,OO0OO0000OO00OO00 in enumerate (OOO0OO0O000O00OO0 ):#line:832
                 O0OOO0O0000OO0OOO [OO000O0OOOOOOO000 [OO0000O0O0OO0000O ]]=OO0OO0000OO00OO00 #line:833
            if len (OO0O00OOO0O000O0O )!=0 :#line:834
                return render_template ('buscador_uro.html',faqs =OO0O00OOO0O000O0O ,faq_titulo ="Preguntas y respuestas: ",result_busqueda =O0OOO0O0000OO0OOO ,user_image4 =O0O00OOO0OO0OOO00 ,user_image5 =OOO000OO0OOO0O00O ,user_image6 =OO0O0O000O000O000 ,user_image7 =OO00O00O00O0OOO0O ,user_image8 =OO0000O0OO00OOOOO ,user_image9 =OOO0OO0OO000OO0O0 ,user_image10 =OO0000000OO0OO000 ,user_image11 =O00O000O000O0OO0O ,user_image12 =O00O000O00OO0O0O0 ,nid2 =0 )#line:835
            else :#line:836
                return render_template ('buscador_uro.html',result_busqueda =O0OOO0O0000OO0OOO ,user_image4 =O0O00OOO0OO0OOO00 ,user_image5 =OOO000OO0OOO0O00O ,user_image6 =OO0O0O000O000O000 ,user_image7 =OO00O00O00O0OOO0O ,user_image8 =OO0000O0OO00OOOOO ,user_image9 =OOO0OO0OO000OO0O0 ,user_image10 =OO0000000OO0OO000 ,user_image11 =O00O000O000O0OO0O ,user_image12 =O00O000O00OO0O0O0 ,nid2 =0 )#line:837
@app .route ("/resultado_uro",methods =['GET','POST'])#line:839
async def resultado_uro ():#line:840
    OOO0O0O0OO0O0O00O =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:841
    O0000OO0OOO0O0000 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:842
    O000O000OO00O00O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'guia_visual.png')#line:843
    OO0O0OOOO000OO00O =os .path .join (app .config ['UPLOAD_FOLDER'],'materiales.png')#line:844
    O00OO00O000OO0O00 =os .path .join (app .config ['UPLOAD_FOLDER'],'pdf_casa.jpg')#line:845
    OO000OO00O000OOO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'protocolo.jpg')#line:846
    OO0OOO0O0O0OO0OOO =os .path .join (app .config ['UPLOAD_FOLDER'],'visualizar_video.png')#line:847
    OO000OO0O0OOO000O =request .args .get ('link')#line:848
    OO0O0O000OO0O0OOO ,OOO00OO0OO00O00O0 =await cargar_tipo (OO000OO0O0OOO000O ,1620 )#line:849
    OOO00OO00OOOOOO0O =OO0O0O000OO0O0OOO ['title']#line:850
    if OOO00OO0OO00O00O0 =="Intervencion":#line:851
        print ("hola1")#line:852
        OO000000OOOO0O0OO ,O0OO000000OOOOOOO =await cargar_caja (str (OO000OO0O0OOO000O ),'Materiales - Cajas: ')#line:853
        return render_template ('intervencion_uro.html',user_image8 =O00OO00O000OO0O00 ,user_image9 =OO000OO00O000OOO0 ,user_image10 =O000O000OO00O00O0 ,user_image11 =OO0OOO0O0O0OO0OOO ,user_image12 =OO0O0OOOO000OO00O ,instrumental =OO000000OOOO0O0OO ,texto_cajas =O0OO000000OOOOOOO ,title =OOO00OO00OOOOOO0O ,user_image6 =OOO0O0O0OO0O0O00O ,user_image7 =O0000OO0OOO0O0000 ,nid2 =OO000OO0O0OOO000O )#line:854
    elif OOO00OO0OO00O00O0 =='Caja':#line:855
        O0OO0000O0O0OOO0O ,O0OOOO00O00OO0O00 ,OO0O0O0OO0OO0OOO0 =await cargar_archivo ("ubicacion","Ubicacion: ","cajas/"+str (OO000OO0O0OOO000O ))#line:856
        OOO0O000O0O00OOO0 =await cargar_archivo ("image","Imagen: ","cajas/"+str (OO000OO0O0OOO000O ))#line:857
        O00O0OO00OO00OO00 ,O0O00OO00OO00000O =await cargar_archivo_grande ("title_material","Material : ","cajas/"+str (OO000OO0O0OOO000O ))#line:858
        return render_template ('caja_trauma.html',title =OOO00OO00OOOOOO0O ,files_instru =O00O0OO00OO00OO00 ,texto_instru =O0O00OO00OO00000O ,texto_ubi =O0OO0000O0O0OOO0O ,file_texto_ubi =OO0O0O0OO0OO0OOO0 ,file_imagen =OOO0O000O0O00OOO0 ,user_image6 =OOO0O0O0OO0O0O00O ,user_image7 =O0000OO0OOO0O0000 )#line:859
    elif OOO00OO0OO00O00O0 =='Instrumental':#line:860
        print ("hola2")#line:861
        OO0OO000OOOOO00OO =await cargar_instrumental (OO000OO0O0OOO000O ,'listado_completo_cajas/1620')#line:862
        return render_template ('instrumental_uro.html',cajas =OO0OO000OOOOO00OO ,texto ='El instrumental que buscas esta presente en las siguientes cajas: ',title =OOO00OO00OOOOOO0O ,user_image6 =OOO0O0O0OO0O0O00O ,user_image7 =O0000OO0OOO0O0000 )#line:863
@app .route ("/protocolos_uro",methods =['GET','POST'])#line:865
async def protocolos_uro ():#line:866
    OOOO0OOO0O00000OO =request .args .get ('link2')#line:867
    O00O0O0O0O0O0OO00 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:868
    OOOO00O0O0O0O000O =await boton_word_ppt (1620 ,"field_protocolo",OOOO0OOO0O00000OO )#line:869
    return render_template ('protocolo.html',protocolos =OOOO00O0O0O0O000O ,user_image7 =O00O0O0O0O0O0OO00 )#line:870
@app .route ("/guia_visual_uro",methods =['GET','POST'])#line:872
async def guia_visual_uro ():#line:873
    OO000O000O00OOOOO =request .args .get ('link2')#line:874
    O0O00OOO0O0OO0000 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:875
    OOOO00OO00OOO000O =await boton_word_ppt (1620 ,"field_guia_visual",OO000O000O00OOOOO )#line:876
    return render_template ('guia_visual.html',guia_visual =OOOO00OO00OOO000O ,user_image7 =O0O00OOO0O0OO0000 )#line:877
@app .route ("/pdf_casa_uro",methods =['GET','POST'])#line:879
async def pdf_casa_uro ():#line:880
    O00O00O00O00O0O0O =request .args .get ('link2')#line:881
    OOOO0OO00OO0OOOOO =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:882
    OOO0OO0O00OOO00OO =await boton_pdf_video (1620 ,"field_pdf",O00O00O00O00O0O0O )#line:883
    return render_template ('pdf_casa_comercial.html',user_image7 =OOOO0OO00OO0OOOOO ,titulos =OOO0OO0O00OOO00OO )#line:884
@app .route ("/videos_uro",methods =['GET','POST'])#line:886
async def videos_uro ():#line:887
    O0O0OOOOOOOO0OO00 =request .args .get ('link2')#line:888
    OOO0OOO000OO00O00 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:889
    OOOO00OO0OOOOOOOO =await boton_pdf_video (1620 ,"field_video",O0O0OOOOOOOO0OO00 )#line:890
    return render_template ('videos.html',user_image7 =OOO0OOO000OO00O00 ,titulos =OOOO00OO0OOOOOOOO )#line:891
@app .route ("/materiales_uro",methods =['GET','POST'])#line:893
async def materiales_uro ():#line:894
    OO00OOOOOOO000OO0 =request .args .get ('link2')#line:895
    OO000O00OOO00OOOO =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:896
    OOO0OO0OO0OOO000O =await boton_materiales (1620 ,OO00OOOOOOO000OO0 )#line:897
    if len (OOO0OO0OO0OOO000O [''])==0 :#line:898
       return render_template ('materiales_uro.html',user_image7 =OO000O00OOO00OOOO ,cajas =OOO0OO0OO0OOO000O ,no_hay ="No hay materiales")#line:899
    return render_template ('materiales_uro.html',user_image7 =OO000O00OOO00OOOO ,cajas =OOO0OO0OO0OOO000O )#line:900
@app .route ("/escuchar_uro1",methods =['GET','POST'])#line:902
async def escuchar_uro1 ():#line:903
    O00000O0OO000O00O =os .path .join (app .config ['UPLOAD_FOLDER'],'guia_visual.png')#line:904
    O00OO0OOOOO0O0OO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'materiales.png')#line:905
    O00OO0OO00OOO000O =os .path .join (app .config ['UPLOAD_FOLDER'],'pdf_casa.jpg')#line:906
    OOOOO000000O00O00 =os .path .join (app .config ['UPLOAD_FOLDER'],'protocolo.jpg')#line:907
    OOOOOOO0OO00O00O0 =os .path .join (app .config ['UPLOAD_FOLDER'],'visualizar_video.png')#line:908
    O00O000O0000O0OO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'micro.png')#line:909
    O0O0O000O00000O0O =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:910
    O00OOOO0OO0O0O000 =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:911
    return render_template ('escuchar_uro1.html',nid2 =0 ,prediction_text ="Dale a `Escuchar´ y haz tu pregunta",user_image5 =O00O000O0000O0OO0 ,user_image6 =O0O0O000O00000O0O ,user_image7 =O00OOOO0OO0O0O000 ,user_image8 =O00OO0OO00OOO000O ,user_image9 =OOOOO000000O00O00 ,user_image10 =O00000O0OO000O00O ,user_image11 =OOOOOOO0OO00O00O0 ,user_image12 =O00OO0OOOOO0O0OO0 )#line:912
@app .route ("/escuchar_uro",methods =['GET','POST'])#line:914
async def escuchar_uro ():#line:915
    OOO000OOO0000O000 =os .path .join (app .config ['UPLOAD_FOLDER'],'guia_visual.png')#line:916
    O00OO0O000OOO000O =os .path .join (app .config ['UPLOAD_FOLDER'],'materiales.png')#line:917
    O0OOO0OO0O0OOO0OO =os .path .join (app .config ['UPLOAD_FOLDER'],'pdf_casa.jpg')#line:918
    OOO000OOO00OO0000 =os .path .join (app .config ['UPLOAD_FOLDER'],'protocolo.jpg')#line:919
    O00O0O0O0OO0O0OO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'visualizar_video.png')#line:920
    OO000O0OO0O000OO0 =os .path .join (app .config ['UPLOAD_FOLDER'],'micro.png')#line:921
    OOOOO00OO00000O0O =os .path .join (app .config ['UPLOAD_FOLDER'],'ajustes.png')#line:922
    OOOOO000O00OO0OOO =os .path .join (app .config ['UPLOAD_FOLDER'],'flecha.png')#line:923
    OOO00OO000OO00O0O =takeCommand ()#line:924
    OOO00OO000OO00O0O =str (OOO00OO000OO00O0O ).lower ()#line:925
    OOO00OO000OO00O0O =OOO00OO000OO00O0O .split ()#line:926
    O00000O0OO0O00O00 ={}#line:927
    O00000O0OO0O00O00 [""]=""#line:928
    if OOO00OO000OO00O0O [0 ]!="none":#line:929
        OOOO0O000OO0O00OO =1620 #line:930
        OOOOOOOO0O0OO00O0 =await cargar_base_datos (OOO00OO000OO00O0O ,OOOO0O000OO0O00OO )#line:931
        O0OO000OO00O0000O =await buscar_faq (OOO00OO000OO00O0O ,0 )#line:932
        if OOOOOOOO0O0OO00O0 ==None :#line:933
            if len (O0OO000OO00O0000O )==0 :#line:934
                return render_template ('escuchar_uro.html',nid2 =0 ,result_busqueda =O00000O0OO0O00O00 ,prediction_text ="No hay resultados para tu busqueda",user_image6 =OOOOO00OO00000O0O ,user_image7 =OOOOO000O00OO0OOO ,user_image5 =OO000O0OO0O000OO0 ,user_image8 =O0OOO0OO0O0OOO0OO ,user_image9 =OOO000OOO00OO0000 ,user_image10 =OOO000OOO0000O000 ,user_image11 =O00O0O0O0OO0O0OO0 ,user_image12 =O00OO0O000OOO000O )#line:935
            else :#line:936
                return render_template ('escuchar_uro.html',nid2 =0 ,faqs =O0OO000OO00O0000O ,faq_titulo ="Preguntas y respuestas: ",result_busqueda =O00000O0OO0O00O00 ,user_image6 =OOOOO00OO00000O0O ,user_image7 =OOOOO000O00OO0OOO ,user_image5 =OO000O0OO0O000OO0 ,user_image8 =O0OOO0OO0O0OOO0OO ,user_image9 =OOO000OOO00OO0000 ,user_image10 =OOO000OOO0000O000 ,user_image11 =O00O0O0O0OO0O0OO0 ,user_image12 =O00OO0O000OOO000O )#line:937
        elif len (OOOOOOOO0O0OO00O0 )>=1 :#line:938
            O0OO00OO00OO0O0O0 =[]#line:939
            O0OOO0O0O00OOOO00 =[]#line:940
            O00000O0OO0O00O00 ={}#line:941
            for OOOO0OO0OOOOO0000 in OOOOOOOO0O0OO00O0 :#line:942
                O0OO00OO00OO0O0O0 .append (OOOO0OO0OOOOO0000 ["title"])#line:943
                O0OOO0O0O00OOOO00 .append (OOOO0OO0OOOOO0000 ["nid"])#line:944
            for OOOOO0O0O0OOO0OO0 ,OOOO0OO0OOOOO0000 in enumerate (O0OO00OO00OO0O0O0 ):#line:945
                 O00000O0OO0O00O00 [O0OOO0O0O00OOOO00 [OOOOO0O0O0OOO0OO0 ]]=OOOO0OO0OOOOO0000 #line:946
            if len (O0OO000OO00O0000O )==0 :#line:948
                return render_template ('escuchar_uro.html',nid2 =0 ,result_busqueda =O00000O0OO0O00O00 ,user_image6 =OOOOO00OO00000O0O ,user_image7 =OOOOO000O00OO0OOO ,user_image5 =OO000O0OO0O000OO0 ,user_image8 =O0OOO0OO0O0OOO0OO ,user_image9 =OOO000OOO00OO0000 ,user_image10 =OOO000OOO0000O000 ,user_image11 =O00O0O0O0OO0O0OO0 ,user_image12 =O00OO0O000OOO000O )#line:949
            else :#line:950
                return render_template ('escuchar_uro.html',nid2 =0 ,faqs =O0OO000OO00O0000O ,faq_titulo ="Preguntas y respuestas: ",result_busqueda =O00000O0OO0O00O00 ,user_image6 =OOOOO00OO00000O0O ,user_image7 =OOOOO000O00OO0OOO ,user_image5 =OO000O0OO0O000OO0 ,user_image8 =O0OOO0OO0O0OOO0OO ,user_image9 =OOO000OOO00OO0000 ,user_image10 =OOO000OOO0000O000 ,user_image11 =O00O0O0O0OO0O0OO0 ,user_image12 =O00OO0O000OOO000O )#line:951
    else :#line:952
        return render_template ('escuchar_uro.html',nid2 =0 ,result_busqueda =O00000O0OO0O00O00 ,prediction_text ="No te he entendido bien, dale al boton `Escuchar´ y repite tu pregunta",user_image5 =OO000O0OO0O000OO0 ,user_image6 =OOOOO00OO00000O0O ,user_image7 =OOOOO000O00OO0OOO ,user_image8 =O0OOO0OO0O0OOO0OO ,user_image9 =OOO000OOO00OO0000 ,user_image10 =OOO000OOO0000O000 ,user_image11 =O00O0O0O0OO0O0OO0 ,user_image12 =O00OO0O000OOO000O )#line:953
@app .route ("/ajustes")#line:955
async def ajustes ():#line:956
    OOO0OOOOO0OOO0O00 =os .path .join (app .config ['UPLOAD_FOLDER'],'estrella.png')#line:957
    return render_template ('ajustes.html',user_image7 =OOO0OOOOO0OOO0O00 )#line:958
if __name__ =="__main__":#line:960
    app .run ()#host='0.0.0.0', port=10000, debug=True)#line:961
