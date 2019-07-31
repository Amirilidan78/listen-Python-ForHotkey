import system_hotkey  
import keyboard as myKeyboard
import time
import requests 
import easygui
import clipboard

def userName():
    myKeyboard.write("Amirilidan78")
    clipboard.copy("Amirilidan78")
def password():
    myKeyboard.write("Amir23334152")
    clipboard.copy("Amir23334152")
def hardPassword():
    myKeyboard.write("7b4bcd795ce5c2da26c3d36a04f52442")
    clipboard.copy("7b4bcd795ce5c2da26c3d36a04f52442")
def email():
    myKeyboard.write("Amirilidan78@gmail.com")
    clipboard.copy("Amirilidan78@gmail.com")
def q():
    myKeyboard.write("php artisan serv")
    clipboard.copy("php artisan serv")
def w():
    myKeyboard.write("php artisan cache:clear")
    clipboard.copy("php artisan cache:clear")
def vru1():
    requests.post('http://hotspot.vru.ac.ir/login', 
    data = {
        'username':'bm97175002',
        'password':'qwe123',
        'dst':'',
        'popup':'true'  
        })
    easygui.msgbox("request sent", title="bm97175002")
def vru2():
    requests.post('http://hotspot.vru.ac.ir/login', 
    data = {
        'username':'bm96149035',
        'password':'3040500341',
        'dst':'',
        'popup':'true'  
        })
    easygui.msgbox("request sent", title="bm97175002")
def vru3():
    requests.post('http://hotspot.vru.ac.ir/login', 
    data = {
        'username':'tbasoft',
        'password':'1371',
        'dst':'',
        'popup':'true'  
        })
    easygui.msgbox("request sent", title="bm97175002")


def PhpUpdate():
    myText = clipboard.paste()
    myArray = myText.split()
    first = myArray[0]
    myArray.pop(0)
    last = myArray[len(myArray)-1]

    paramets = """
    """
    for i in myArray :
        paramets += "$"  
        paramets += i 
        paramets += " = $r->" 
        paramets += i 
        paramets += ";" 
        paramets += """
    """ 
    
    myIf = """
    if (
    """
    for i in myArray:
        myIf+="!$"
        myIf+=i
        if last == i :
            pass
        else :
            myIf+="||"
    myIf += """
    ){"""
    myIf += """
        
        return [
                '1' => false ,
                '2' => 'please fill fields'
            ];
    }
"""
    
    findItem = f"""
    $obj = {first}::find(${myArray[0]});
    """
    
    myArray.pop(0)
    findItem += """
    $obj->fill([
        """
        
    for i in myArray :
        findItem += f"""'{i}' => ${i} ,"""+"""
       """
    
    findItem += """
    ]);

    
    $obj->save();

    return [
        '1' => true ,
        '2' => 'inserted successfully'
    ];
    
}"""



    text = """public function postUpdate"""+first+"""(Request $r){ 
       """+paramets+myIf+"""
       """+findItem
       
    myKeyboard.write(text)

def PhpInsert():
    myText = clipboard.paste()
    myArray = myText.split()
    first = myArray[0]
    myArray.pop(0)
    last = myArray[len(myArray)-1]

    paramets = """
    """     
    for i in myArray :
        paramets += "$"  
        paramets += i 
        paramets += " = $r->" 
        paramets += i 
        paramets += ";" 
        paramets += """
    """ 
    
    myIf = """
    if (
    """     
    for i in myArray:
        myIf+="!$"
        myIf+=i
        if last == i :
            pass
        else :
            myIf+="||"
    myIf += """
    ){"""
    myIf += """
        
        return [
                '1' => false ,
                '2' => 'please fill fields'
        ];
    }
"""
    

    createNew = """
    $new = """+first+"""::create([
        """
        
    for i in myArray :
        createNew += f"""'{i}' => ${i} ,"""+"""
       """
    
    createNew += """
    ]);
        
    return [
        '1' => true ,
        '2' => 'inserted successfully'
    ];
    
}"""



    text = """public function postInsert"""+first+"""(Request $r){ 
       """+paramets+myIf+"""
       """+createNew
    myKeyboard.write(text)



def PhpDelete():
    myText = clipboard.paste()
    myArray = myText.split()
    myText = myArray[0]
    text = """public function postDelete"""+myText+"""(Request $r){ 
       
        if(
            !$r->id 
        ){
            return ['1' =>false , '2' =>"error"];
        }
        

        """+myText+""".find($r->id)->delete();
        
        return ['1' =>true , '2' =>"succcess"];
               
}
            """ 
    myKeyboard.write(text)

myKeyboard.add_hotkey('alt+shift+1', userName)
myKeyboard.add_hotkey('alt+shift+2', password)
myKeyboard.add_hotkey('alt+shift+3', hardPassword)
myKeyboard.add_hotkey('alt+shift+4', email)
myKeyboard.add_hotkey('alt+shift+q', q)
myKeyboard.add_hotkey('alt+shift+w', w)
myKeyboard.add_hotkey('control+1', PhpInsert)
myKeyboard.add_hotkey('control+2', PhpUpdate)
myKeyboard.add_hotkey('control+3', PhpDelete)
myKeyboard.wait()