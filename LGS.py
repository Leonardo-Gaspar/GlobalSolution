class Sistema:
    def __init__(self):
        self.cadastro = None
        self.cliente = []
        self.empresa = []
        self.prestador = {}
        self.corretor = {}
        self.suporte = {}
    def cadastrar_paciente(self):
        print("\n--- Cadastro ---")
        nome = input("Nome do paciente: ")
        email = input("Email do paciente: ")
        rg = input("RG do paciente: ")
        cpf = input("CPF do paciente: ")
        telefone = input("Telefone do paciente: ")
        data_nascimento = input("Data de nascimento (dd/mm/aa):  ")
        tipo_sanguineo = input("Tipo sanguíneo: ")

        self.cliente = {"Nome": nome, "\nEmail": email, "\nTelefone": telefone}
        print(f"Nome: {nome}\nEmail: {email}\nTelefone: {telefone}\nRG: {rg} \nCPF: {cpf}\nData de nascimento: {data_nascimento}\nTipo sanguíneo: {tipo_sanguineo}")
        print("Cadastro realizado com sucesso!")
    def mostrar_menu(self):
        print("\n--- Menu ---")
        print("1. Menu Cliente")
        print("2. Menu Empresa")
        print("3. Menu Prestador")
        print("4. Menu Corretor")
        print("5. Menu Suporte")
        print("6. Sair")

    def executar(self):
        print("Bem-vindo à Hapvida NotreDame Intermédica!")
        self.cadastrar_paciente()
        while True:
            self.mostrar_menu()
            print("---------------------------------------------------------------------")
            escolha = input("Escolha uma opção (1-6): ")
            print("---------------------------------------------------------------------")

            if escolha == "1":
                self.menu_cliente()
            elif escolha == "2":
                self.menu_empresa()
            elif escolha == "3":
                self.menu_prestador()
            elif escolha == "4":
                self.menu_corretor()
            elif escolha == "5":
                self.menu_suporte()
            elif escolha == "6":
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida. Escolha uma opção válida.")

    def menu_cliente(self):
        print("\n--- Cliente ---")
        print("\n--- Menu Cliente---")
        print("1. Consulta")
        print("2. Carteira Online")
        print("3. Rede Credenciada Odontológica")
        print("4. Guia Médico")
        print("5. Solicitar Autorização")
        print("6. Atualizar Dados")
        print("7. Setor Financeiro")
        print("8. PIN-SS(Portal de Informações do Beneficiário")
        print("9. Substituição de Prestadores")
        print("10. Centrais de Atendimento Presencial")
        print("11. Histórico de Solicitações")
        print("12. Kit Boas-Vindas")
        print("13. Senha Liberada")
        print("14. Clube Vantagens")
        print("15. Central de Serviços")
        print("16. Extrato de Coparticipação")
        print("17. Consignados")
        print("18. Ajuda")

        print("---------------------------------------------------------------------------")
        escolha_cliente = input("Escolha a área que deseja (1-18): ")
        print("---------------------------------------------------------------------------")

        if escolha_cliente == "1":
            print("\n--- Consulta ---\n")
            print("--- Menu Consulta ---")
            print("1. Marcar Consulta")
            print("2. Desmarcar Consulta")
            print("3. Consulta Odonto")
            print("4. Exames")
            print("5. Consulta Reajuste de Contrato")

            print("---------------------------------------------------------------------------")
            escolha_consulta = input("Escolha sua opção (1-5): ")
            print("---------------------------------------------------------------------------")

            if escolha_consulta == "1":
                print("Link direcionado à página Marcar Consulta: https://www.hapvida.com.br/site/lp-escolha-experiencia/?url=https%3A//www.hapvida.com.br/site/marquesuaconsulta")
            elif escolha_consulta == "2":
                print("Link direcionado à página Desmarcar Consulta: https://www.hapvida.com.br/site/lp-escolha-experiencia/?url=https%3A//webhap.hapvida.com.br/pls/webhap/pk_saude.formulario%3Fpds_app%3DwebNewDesmarcaConsulta.inicio%26pfl_mobile%3DN%26pfl_tipo%3DS%26pfl_situacao%3DA")
            elif escolha_consulta== "3":
                print("Link direcionado à página Consulta Odonto: https://www.hapvida.com.br/site/lp-escolha-experiencia/?url=/pls/podontow/webnewdentalcliente.pr_login_n%3FpOrgAmb%3D2")
            elif escolha_consulta == "4":
                print("Link direcionado à página Exames: https://www.hapvida.com.br/site/exames")
            elif escolha_consulta == "5":
                print("Link direcionado à página Consulta Reajuste de Contrato: https://webhap.hapvida.com.br/pls/webhap/pk_ajuste_contrato.principal")
            else:
                print("Digite uma opção válida.")
        elif escolha_cliente == "2":
            print("\n---Carteira Online---")
            print("Link direcionado à página Carteira Online: https://www.hapvida.com.br/site/lp-escolha-experiencia/?url=https%3A//webhap.hapvida.com.br/pls/webhap/pk_carteira_provisoria.login_usuario_form")
        elif escolha_cliente == "3":
            print("\n---Rede Credenciada Odontológica---")
            print("Link direcionado à página Rede Credenciada Odontológica: https://www.hapvida.com.br/site/lp-escolha-experiencia/?url=https%3A//webhap.hapvida.com.br/pls/podontow/webdentalredecredenciada.selecionaRede")
        elif escolha_cliente == "4":
            print("\n---Guia Médico---")
            print("Link direcionado à página Guia Médico: https://www.hapvida.com.br/site/lp-escolha-experiencia/?url=https%3A//webhap.hapvida.com.br/pls/webhap/webnewredecredenciada.selecionarede ")
        elif escolha_cliente == "5":
            print("\n---Solicitar Autorização---")
            print("Link direcionado à página Solicitar Autorização: https://app.hapvida.com.br/solicitacaoautorizacao/login ")
        elif escolha_cliente == "6":
            print("\n---Atualizar Dados---")
            print("Link direcionado à página Atualizar Dados: https://webhap.hapvida.com.br/pls/webhap/pk_atualiza_dados.principal")
        elif escolha_cliente == "7":
            print("\n---Setor Financeiro---")
            print("\n--- Menu Setor Financeiro Cliente ---")
            print("1. Boleto de Pagamento")
            print("2. Boleto Digital e Notificações")
            print("3. Imposto de Renda")
            print("4. Ficha Financeira")
            print("5. Declaração de Quitação Anual")
            print("6. Negociação de Dívida")
            print("7. Nota Fiscal")

            print("---------------------------------------------------------------------------")
            escolha_financeiro_cliente = input("Escolha sua opção (1-7): ")
            print("---------------------------------------------------------------------------")

            if escolha_financeiro_cliente == "1":
                print("Link direcionado à página Boleto de Pagamento: https://www.hapvida.com.br/site/lp-escolha-experiencia/?url=https%3A//webhap.hapvida.com.br/pls/webhap/webNewBoleto.login ")
            elif escolha_financeiro_cliente == "2":
                print("Link direcionado à página Boleto Digital e Notificações: https://www.hapvida.com.br/site/lp-escolha-experiencia/?url=https%3A//notificacaoeletronica.hapvida.com.br/notificacao-eletronica/autenticacao.xhtml%3FcdEmpresa%3D1")
            elif escolha_financeiro_cliente == "3":
                print("Link direcionado à página Imposto de Renda: https://www.hapvida.com.br/site/lp-escolha-experiencia/?url=https%3A//webhap.hapvida.com.br/pls/webhap/webnewirusuario.login")
            elif escolha_financeiro_cliente == "4":
                print("Link direcionado à página Ficha Financeira: https://www.hapvida.com.br/site/lp-escolha-experiencia/?url=https%3A//webhap.hapvida.com.br/pls/webhap/webfichafinanceira.login")
            elif escolha_financeiro_cliente == "5":
                print("Link direcionado à página Declaração de Quitação Anual: https://webhap.hapvida.com.br/pls/webhap/webNewQuitacaoAnual.login")
            elif escolha_financeiro_cliente == "6":
                print("Link direcionado à página Negociação de Dívida: https://www.hapvida.com.br/pls/webhap/pk_saude.formulario?pds_app=pk_selfcheckout.pr_inicio&pfl_mobile=N&pfl_tipo=S&pfl_situacao=A&p_ambiente=S")
            elif escolha_financeiro_cliente == "7":
                print("Link direcionado à página Nota Fiscal: https://www.hapvida.com.br/pls/webhap/pk_nota_fiscal_ind.login_usuario_form")
            else:
                print("Digite uma opção válida.")
        elif escolha_cliente == "8":
            print("\n---PIN-SS (Portal de Informaçoes do Benefício)---")
            print("Link direcionado à página PIN-SS (Portal de Informaçoes do Benefício): https://webhap.hapvida.com.br/pls/webhap/pk_portal_transparente.login")
        elif escolha_cliente == "9":
            print("\n---Substituição de Prestadores---")
            print("Link direcionado à página Substituição de Prestadores: https://webhap.hapvida.com.br/pls/webhap/webNewSubstituicaoRede.login")
        elif escolha_cliente == "10":
            print("\n---Centrais de Atendimento Presencial---")
            print("Link direcionado à página Centrais de Atendimento Presencial: https://www.hapvida.com.br/site/atendimento-ao-cliente")
        elif escolha_cliente == "11":
            print("\n---Histórico de Solicitações---")
            print("Link direcionado à página Histórico de Solicitações: https://webhap.hapvida.com.br/pls/webhap/pk_saude.formulario?pds_app=webNewHapMovelLinhaDireta.listarSacMsg&pfl_mobile=N&pfl_tipo=S&pfl_situacao=A")
        elif escolha_cliente == "12":
            print("\n---Kit Boas-Vindas---")
            print("Link direcionado à página Kit Boas-Vindas: https://www.hapvida.com.br/site/noticias/confira-onde-voc%C3%AA-pode-pegar-seu-kit-boas-vindas-carteirinha-e-guia-m%C3%A9dico")
        elif escolha_cliente == "13":
            print("\n---Senha Liberada---")
            print("Link direcionado à página Senha Liberada: https://webhap.hapvida.com.br/pls/webhap/pk_saude.formulario?pds_app=webNewHapMovelSenhaLiberada.execLogon&pfl_mobile=N&pfl_tipo=S&pfl_situacao=A")
        elif escolha_cliente == "14":
            print("\n---Clube Vantagens---")
            print("Link direcionado à página Clube Vantagens: https://clube.hapvidandi.com.br/")
        elif escolha_cliente == "15":
            print("\n---Central de Serviços---")
            print("Link direcionado à página Central de Serviços: https://cafex.hapvida.com.br/sigo/linha-frente/#/login/1")
        elif escolha_cliente == "16":
            print("\n---Extrato de Coparticipações---")
            print("Link direcionado à página Extrato de Coparticipações: https://www.hapvida.com.br/site/lp-escolha-experiencia/?url=https%3A//webhap.hapvida.com.br/pls/webhap/webnewextratoutilizacao.login")
        elif escolha_cliente == "17":
            print("\n---Consignados---")
            print("Link direcionado à página Consignados: https://www.hapvida.com.br/site/noticias/confira-os-extratos-de-consigna%C3%A7%C3%B5es")
        elif escolha_cliente == "18":
            print("\n---Ajuda---")
            print("Link direcionado à página Ajuda: https://www.hapvida.com.br/site/central_de_ajuda")
        else:
            print("Opção inválida. Escolha uma opção válida.")

        self.mostrar_resumo_operacao("Cliente")