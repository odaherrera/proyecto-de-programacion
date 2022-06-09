
# Online Python - IDE, Editor, Compiler, Interpreter
billetes = [1,5,10,20,50,100]
monto_de_retiro = int(input('--> '))

def operaciones(monto_de_retiro):
    result = []
    for b in billetes:
        if b == monto_de_retiro:
            print('un billete de',b)
            exit()
        cant_de_billetes_retiro = monto_de_retiro//b
        if cant_de_billetes_retiro<0:
           break
        if cant_de_billetes_retiro !=0:
          result.append([cant_de_billetes_retiro,b])
          
        ordenado = sorted(result)
    for c in ordenado:
        cant = c[0]
        billete = c[1]
        print(cant ,'de billete de',billete)
        dinero_falta = monto_de_retiro-(cant*billete)
        if dinero_falta>0:
           operaciones(dinero_falta)
        else:
           exit()
           
operaciones(monto_de_retiro)
