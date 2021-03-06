#! /usr/bin/python3
import re, os, sys, json, readline
import atexit
sys.path.append(os.path.join(sys.path[0],'modules'))

import config as C
from Func import *
import Command_Autocomplete as AutoCmpt
import _set_, push, _print_, pop, delete, save, load


if __name__ == "__main__":
    try:
        f = open('./modules/EnvVars.json')
        s = f.read()
        f.close()
        
        _ = json.loads(s)
        C.EnvVar = _
    except:
        print('Error on Reading Envvars.json\nSet to Default.')
    
    AutoCmpt.init()
    
    while True: 
        C.CMD = AutoCmpt.getCMD()
        if not C.CMD: pass # 입력이 공백이거나, 정의된 명령어가 아닐 때.
        elif re.match('print.*',C.CMD) : _print_.init()
        elif re.match('push .+', C.CMD): push.push()
        elif re.match('pop.*', C.CMD) : pop.pop()
        elif re.match('set .+', C.CMD) : _set_._set_()
        elif re.match('delete .+', C.CMD) : delete.init()
        elif re.match('save.*', C.CMD) : save.init()
        elif re.match('load.*', C.CMD) : load.init()
        elif C.CMD == 'clear': # 화면 초기화.
            if os.name == 'nt': os.system('cls')
            elif os.name == 'posix': os.system('clear')
        elif C.CMD == 'quit' : break
        else : print('Syntax Error.')