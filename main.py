from encriptador import encriptador
import argparse

# multiplicar diferencia xor

# falta la funcionalidad de python main.py encriptar multiplicar 10 => 60.. para cada caso


def main():
    # print(encriptador.encriptar(1,"xor"))
    
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-f','--function', help='Funcion de cifrar o descifrar', required=True)
    parser.add_argument('-n','--number', help='Número a utilizar en funcion f', required=True)
    parser.add_argument('-a','--algorithm', help='Algoritmo que utliza la funcion f', required=True)
    args = vars(parser.parse_args())

    
    if args["function"] == "cifrar":
        print(encriptador.encriptar(float(args["number"]), args["algorithm"])) 
    if args["function"] == "descifrar":
        print(encriptador.desencriptar(float(args["number"]), args["algorithm"]))
    raise Exception('La función '+ args["function"] + ' no exite, por favor ingrese los nombres cifrar y descifrar')
    

if __name__ == "__main__":
    main()