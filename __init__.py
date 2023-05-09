"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")
Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json
Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")
Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)
Para obtener la Opcion seleccionada:
    opcion = GetParams("option")
Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    pip install <package> -t .
"""
import os
import sys
from subprocess import Popen, PIPE
import traceback
import ctypes

GetParams = GetParams #pylint: disable=undefined-variable,self-assigning-variable
SetVar = SetVar #pylint: disable=undefined-variable,self-assigning-variable
PrintException = PrintException #pylint: disable=undefined-variable,self-assigning-variable


# Add the libs folder to the system path
base_path = tmp_global_obj["basepath"]
cur_path = os.path.join(base_path, 'modules', 'dll_reader', 'libs')

cur_path_x64 = os.path.join(cur_path, 'Windows' + os.sep +  'x64' + os.sep)
cur_path_x86 = os.path.join(cur_path, 'Windows' + os.sep +  'x86' + os.sep)

if sys.maxsize > 2**32 and cur_path_x64 not in sys.path:
        sys.path.append(cur_path_x64)
        dumpbin = os.path.join(cur_path_x64, 'dumpbin.exe')
if sys.maxsize > 32 and cur_path_x86 not in sys.path:
        sys.path.append(cur_path_x86)
        dumpbin = os.path.join(cur_path_x86, 'dumpbin.exe')
        
        
types = {
    "bool": ctypes.c_bool,
    "int": ctypes.c_int,
    "float": ctypes.c_float,
    "double": ctypes.c_double,
    "str": ctypes.c_char
}

module = GetParams("module")

if module == "get_functions":
    dll_path = GetParams("dll_path")
    result = GetParams("result")
    
    try:
        response = Popen(f"{dumpbin} {dll_path} /exports", stdout=PIPE, stdin=PIPE, stderr=PIPE).communicate()
        response = response[0].decode().split("name")
        response = response[2].split("\r\n")
        print(response)
        functions = []
        for r in response:
            r_ = r.split()
            func = r_[3] if len(r_)>3 else ""
            if func != "":
                functions.append(func)
        SetVar(result, functions)
    except Exception as e:
        traceback.print_exc()
        SetVar(result, False)
        raise e
    
    
if module == "execute_function":
    dll_path = GetParams("dll_path")
    func = GetParams("function")
    params = GetParams("parameters")
    restype = GetParams("restype")
    result = GetParams("result")
    
    try:
        dll = ctypes.cdll.LoadLibrary(dll_path)
        my_function = getattr(dll, func)
        if restype:
            my_function.restype = types.get(restype)
        
        if not isinstance(params, list):
            params = params.split(",")
        
        func_res = my_function(*params)
        
        SetVar(result, func_res)
    except Exception as e:
        SetVar(result, "")
        raise e