from pynput import keyboard
import keyboard as myKeyboard
import datetime
from pynput.keyboard import Controller
import clipboard
# The key combinations to check
COMBINATIONS = [
    {keyboard.Key.ctrl_l, keyboard.KeyCode(char='1')},
]


myController =  Controller()
# The currently active modifiers
current = set() 
tnow = datetime.datetime.now()
tcounter = 0

def on_press(key):
    if any([key in comb for comb in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in comb) for comb in COMBINATIONS):
            global tnow
            global tcounter
            tcounter += 1
            if datetime.datetime.now() - tnow < datetime.timedelta(seconds=1):
                if tcounter > 1:
                    tcounter = 0
                    myText = ""
                    myText = clipboard.paste()
                    myArray = ""
                    myArray = myText.split()
                    temp = ""
                    temp = myArray[0]
                    if temp == "backInsert" :
                        backInsert()
                    elif temp == "backDelete" :
                        backDelete()
                    elif temp == "backUpdate" :
                        backUpdate()
            else:
                tnow = datetime.datetime.now()
     
    if key == keyboard.Key.esc:
        listener.stop()


def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass

def backDelete():
    print('delete')
    myText = clipboard.paste()
    myArray = myText.split()
    myText = myArray[1]
    text = """public function """+myText+"""(Request $r){ 
       
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
    

def backInsert():
    print('insert')
    myText = clipboard.paste()
    myArray = myText.split()
    myArray.pop(0)
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




def backUpdate():
    print('update')
    myText = clipboard.paste()
    myArray = myText.split()
    myArray.pop(0)
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
    $obj = {first}::find({myArray[0]});
    """

    findItem += """
    $obj->fill([
        """
        
    for i in myArray :
        findItem += f"""'{i}' => ${i} ,"""+"""
       """
    
    findItem += """
    ]);
        
    return [
        '1' => true ,
        '2' => 'inserted successfully'
        ];
    
}"""



    text = """public function postUpdate"""+first+"""(Request $r){ 
       """+paramets+myIf+"""
       """+findItem
    myKeyboard.write(text)





    

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()