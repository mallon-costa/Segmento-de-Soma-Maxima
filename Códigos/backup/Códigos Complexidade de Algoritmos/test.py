from pynput.keyboard import Key, Listener 
"""
def show(key): 
    
    if key == Key.tab: 
        print("good") 
          
    if key != Key.tab: 
        print("try again") 
          
    if key == Key.delete:  
        return False
with Listener(on_press = show) as listener: 
    listener.join() 
"""
x = 'True'
def show(key):
    print("Digite dois números: ")
    a = int(input())
    b = int(input())
    print("A soma é: " +str(a+b))

    print("Tecle ENTER para continuar")
    if key == Key.enter: 
        print("good") 
    
with Listener(on_press = show) as listener:
    listener.join()

