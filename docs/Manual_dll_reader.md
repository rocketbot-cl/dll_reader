


# dll_reader
  
Read and call functions from DLL filess  

  
*Read this in other languages: [English](Manual_dll_reader.md), [Português](Manual_dll_reader.pr.md), [Español](Manual_dll_reader.es.md)*  

  
![banner](imgs/Banner_dll_reader.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Get functions from dll file
  
Get the available functions of a dll file. Currently available for Windows; must have Visual Studio installed.
|Parameters|Description|example|
| --- | --- | --- |
|Path to 'dumpbin.exe'|Path to 'dumpbin.exe' in Visual Studio folder.|C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\bin\Hostx64\x64\dumpbin.exe|
|Path to dll file|Path to the dll file to read.|C:\Users\user\Desktop\file.dll|
|Assign result to variable|Assign connection result to variable.|result|

### Execute function
  
Execute a function from a dll file.
|Parameters|Description|example|
| --- | --- | --- |
|Path to dll file|Path to the dll file to read.|C:\Users\user\Desktop\file.dll|
|Function|Nome da função a executar.|sum|
|Parameters|List of parameters to pass to the function.|[2, 2]|
|Result type|Select the type of variable to receive from the execution of the function.|Integer|
|Assign result to variable|Assign result of the query to a variable.|result|
