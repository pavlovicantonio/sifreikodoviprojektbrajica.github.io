brajica = {
    'a': '⠁',
    'b': '⠃', 
    'c': '⠉',
    'd': '⠙', 
    'e': '⠑',
    'f': '⠋',
    'g': '⠛', 
    'h': '⠓', 
    'i': '⠊', 
    'j': '⠚',
    'k': '⠅', 
    'l': '⠇', 
    'm': '⠍', 
    'n': '⠝', 
    'o': '⠕',
    'p': '⠏', 
    'q': '⠟', 
    'r': '⠗', 
    's': '⠎', 
    't': '⠞',
    'u': '⠥', 
    'v': '⠧', 
    'w': '⠺',
    'x': '⠭', 
    'y': '⠽',
    'z': '⠵'
}

def input_u_brajicu(tekst):
    brail = ''
    for tekst in tekst.lower():
        brail += brajica.get(tekst, tekst)
        brail +=' ' #ovdje smo ubacili whitespace čisto da bude pregledniji output
                    #iako white space nebi smio biti u brajici prije kraja riječi
    return brail

unos = input("Unesite tekst koji želite prebaciti u brajicu:")
print(input_u_brajicu(unos))