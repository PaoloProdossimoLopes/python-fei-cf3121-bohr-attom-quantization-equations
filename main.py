import math

PLANK_JS = 6.63e-34
PLANK_EV = 4.13e-15
VELOCIDADE_LUZ = 3e8
CARGA_ELEMENTAR = 1.6e-19
PERMISSIVIDADE_VACUO = 8.854e12
MASSA_ATOMO_HIDROGENIO = 1.66e24

def main():
    _alunos()
    _operacoes()

def _alunos():
    print("""
----------------------------------
:::::::::::: Alunos ::::::::::::::
----------------------------------
Paolo Prodossimo Lopes - 22.222.052-7
Felipe da Rocha Pinheiro - 22.222.059-2
Fernando Ferreira Sanches - 22.222.054-3
Gustavo Sesoko Lemos - 22.123.064-2
    """)

def _opcoes():
    print("""
---------------------------------
:::::::::::: OPÇÕES ::::::::::::::
----------------------------------
1 - (n) Numero quantico
2 - (ni e nf) Numero quantico final e inicial
3 - (ni ou nf e ffoton ou λfotonAbs) Numero quantico inicial ou final + frequencia do 
    foton ou comprimento de onda do foton absorvido
4 - (ni ou nf e ffoton ou λfotonEmi) Numero quantico inicial ou final + frequencia do 
    foton ou comprimento de onda do foton emitido
0 - Sair
    """)

def _operacoes():
    while True:
        _opcoes()

        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            numero_quantico = float(input('Informe o numero quantico: '))

            rn = (numero_quantico * numero_quantico) * 5.29e-11
            vn = (2.187e6 / numero_quantico)
            kn = abs(_calculandoEfoton(numero_quantico))
            un = -27.2 / (numero_quantico * numero_quantico)
            en = _calculandoEfoton(numero_quantico)
            λn = PLANK_JS / (MASSA_ATOMO_HIDROGENIO * vn)

            print('rn - Raio da orbita: {:.2e} [m]'.format(rn))
            print('Vn - Velocidade: {:.2e} [m/s]'.format(vn))
            print('Kn - Energia cinetica: {:.2e} [eV]'.format(kn))
            print('Un - Energia potencial: {:.2e} [eV]'.format(un))
            print('En - Energia total: {:.2e} [eV]'.format(en))
            print('λn - Comprimento de onda do eletron: {:.2e} [m]'.format(λn))

        elif escolha == '2':
            numero_quantico_inicial = float(input('Informe o numero quantico incial: '))
            numero_quantico_final = float(input('Informe o numero quantico final: '))

            e_foton = _calculandoΔEFoton(numero_quantico_inicial, numero_quantico_final)
            λ_foton = (PLANK_EV * VELOCIDADE_LUZ) / e_foton
            f_foton = e_foton / PLANK_EV
            
            print('Efoton - Enegia do foton: {:.2f} [eV]'.format(e_foton))
            print('λfoton - Comprimento de onda do foton: {:.2e} [m]'.format(λ_foton))
            print('Ffoton - Frequencia do foton: {:2e} [Hz]'.format(f_foton))

        elif escolha == '3':
            _calulo_n_resultante(evento=_absorver, tipo_evento="Absorvido/a")

        elif escolha == '4':
            _calulo_n_resultante(evento=_emitir, tipo_evento="Emitido/a")

        elif escolha == '0':
            print('👋🏽 Finalizando o programa ....')
            break

        else:
            print('❌ Opção invalida tente ecolher outra opção')
            continue

def _calculandoEfoton(numero_quantico):
    return -13.6/(numero_quantico*numero_quantico)

def _calculandoΔEFoton(n_inicial, n_final):
    e_foton_inicial = _calculandoEfoton(n_inicial)
    e_foton_final = _calculandoEfoton(n_final)
    return e_foton_final - e_foton_inicial

def _calculandoNFinal(n, energia_evento, evento):
    energia_n = _calculandoEfoton(float(n))
    energia_resultante = evento(energia_n, energia_evento)
    return math.sqrt(abs(13.6/energia_resultante))

def _entradaEhValida(valor):
    return not valor == ''

def _absorver(inicial, final):
    return inicial + final

def _emitir(inicial, final):
    return inicial - final

def _calulo_n_resultante(evento, tipo_evento):
    n_inicial = input('Numero quantico inicial (opcional): ')
    n_final = input('Numero quantico final (opcional): ')

    frequencia_foton = input('Frequencia do foton {} (opcional): '.format(tipo_evento))
    lambda_foton = input('Comprimento de onda {} (opcional): '.format(tipo_evento))

    energia_evento = 0.0
    if _entradaEhValida(lambda_foton):
        energia_evento = _calculando_energia_evento_por_λ_foton(lambda_foton)
    elif _entradaEhValida(frequencia_foton):
        energia_evento = _calculando_energia_evento_por_frequencia_foton(frequencia_foton)
    else:
        print('❌ Quantidade minima de parametros invalida!')
        return 

    if _entradaEhValida(n_inicial):
        resultado_n_final = _calculandoNFinal(n_inicial, energia_evento, evento)
        print('n_final - numero quantico final: {:.2f}'.format(resultado_n_final))
        print('n_final - numero quantico final: {:d}'.format(round(resultado_n_final)))
        return
    elif _entradaEhValida(n_final):
        resultado_n_inicial = _calculandoNFinal(n_final, energia_evento, evento)
        print('n_inicial - numero quantico inicial: {:.2f}'.format(resultado_n_inicial))
        print('n_inicial - numero quantico inicial: {:d}'.format(round(resultado_n_inicial)))
        return
    else:
        print('❌ Algo inesperado occorreu tente novamente!')
        return
    
def _calculando_energia_evento_por_λ_foton(λ):
    return (PLANK_EV * VELOCIDADE_LUZ) / float(λ)

def _calculando_energia_evento_por_frequencia_foton(frequencia):
    return PLANK_EV * float(frequencia)

if __name__ == '__main__':
    main()