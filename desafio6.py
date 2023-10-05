resul = 10

rodada = 1
tentativas = 5
while ( rodada <= tentativas):
    print(f" tentativa {rodada} de {tentativas}")
    num = int(input("insira o valor:"))
    if num == resul:
        print("acertou")
        break
    elif num < resul:
        print("numero menor")
    else:
      print:("numero maior")
      
    rodada += 1    
    