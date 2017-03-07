from functions_lib import * 

a = pd.read_csv("dado.csv")
listaNomeDado=["Ceara", "Minas Gerais", "Rio de Janeiro", "Parana", "Brazil"]
condicao = input("O que deseja observar: \nHistograma \nBoxplot\nMedidas_Resumo\nOu deseja sair? \n" )
condicao = condicao.upper()

while condicao != "SAIR":
    if condicao == "BOXPLOT":
        ifs(condicao, boxplot, a, listaNomeDado)
        plt.show()
    elif condicao == "HISTOGRAMA":
        ifs(condicao, histograma, a, listaNomeDado)
        plt.show()
    elif condicao == 'MEDIDAS RESUMO':
        ifs(condicao, describe, a, listaNomeDado)
    else:
        print("alternativa incorreta")
    condicao = input("O que deseja observar: \nHistograma \nBoxplot\nMedidas_Resumo\nOu deseja sair?\n" )
    condicao = condicao.upper()    
    