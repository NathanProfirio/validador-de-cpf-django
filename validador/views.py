from django.shortcuts import render
from django.http import HttpResponse 


def consulta_cpf(request):
    resposta = None

    if request.method == "GET":
        return render(request, 'consulta.html')
    elif request.method == "POST":
        cpf_do_usuario = request.POST.get("cpf")
        
    
        if not cpf_do_usuario.isdigit():
            resposta = 'Por favor, digite apenas números.'
            return render(request, 'consulta.html',{'resposta': resposta})
        
        if len(cpf_do_usuario) != 11:
            resposta = 'O CPF deve conter exatamente 11 números.'
            return render(request, 'consulta.html',{'resposta': resposta})
        
        #Verifica se o usuário digitos somente numeros iguais
        if cpf_do_usuario == cpf_do_usuario[0] * len(cpf_do_usuario):
            resposta = "Você inseriu um CPF inválido composto apenas por números repetidos."
            return render(request, 'consulta.html',{'resposta': resposta})
        
        #criação das variaveis usadas durante a validação do cpf
        contador_regressivo = 10
        contador_das_repeticoes = 0
        soma_primeiros_digitos = 0
        soma_segundo_digito = 0
        cpf_formatado = ""

        #calcular o primeiro digito verificado
        for primeiro in cpf_do_usuario[:9]:
            soma_primeiros_digitos += int(primeiro) * contador_regressivo
            contador_regressivo -= 1
            
        mult_resto_divisao = (soma_primeiros_digitos * 10) % 11

        if mult_resto_divisao > 9:
            primeiro_digito = 0
        else:
            primeiro_digito = mult_resto_divisao

        #Calcular o segundo codigo verificado
        contador_regressivo = 11
        for segundo in cpf_do_usuario[:10]:
            soma_segundo_digito += int(segundo) * contador_regressivo
            contador_regressivo -= 1
            mult_resto_divisao = (soma_segundo_digito * 10) % 11

        if mult_resto_divisao > 9:
            segundo_digito = 0
        else:
            segundo_digito = mult_resto_divisao

        #Formata o numero digitado pelo usuário para o padrão do cpf 000.000.000-00
        for formatacao in cpf_do_usuario:
            if contador_das_repeticoes == 2:
                formatacao += "."
                contador_das_repeticoes += 1
            if contador_das_repeticoes == 6:
                formatacao += "."
                contador_das_repeticoes += 1
            if contador_das_repeticoes  == 10:
                formatacao += "-"
                contador_das_repeticoes += 1
            cpf_formatado += formatacao
            contador_das_repeticoes += 1

        #verifica e mostra se o cpf digitado e valido ou não 
        if str(primeiro_digito) == cpf_do_usuario[9] and str(segundo_digito) == cpf_do_usuario[10]:
            print(f"O cpf {cpf_formatado} e valido")
            resposta = f'O cpf {cpf_formatado} e valido'

        else:
            print(f"O cpf {cpf_formatado} e invalido")
            resposta = f'O cpf {cpf_formatado} e invalido'
        
    return render(request, 'consulta.html',{'resposta': resposta, 'cpf_formatado': cpf_formatado})            
        
            
        

