import streamlit as st

def pagina_sinopse():
    st.title("Minha História")
    
    # Criar 3 colunas: a do meio para a imagem, laterais vazias para centralizar
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.image("assets/foto_perfil.jpg", width=500, caption="")

    st.write("""
    **Sinopse Profissional**

    Iniciei na RT Intelligence em 22/09/2023.  
    Tenho 32 anos, sou graduado em Administração (UFPE) e pós-graduado em Engenharia e Análise de Dados (CESAR School).  

    Atuo com dados, automação e soluções que aumentam a eficiência operacional.
    """)

    st.markdown("---")
    st.header("Linha do Tempo da Trajetória Profissional")
    
    st.markdown("""
    🟢 **Setembro 2023** — Iniciei na área de TI.

    🔵 **Maio 2024** — Transição para equipe de Planejamento e Roteiro.

    🟠 **Novembro 2024** — Retorno à equipe de TI.
    """)


def pagina_projetos():
    st.title("Projetos Realizados")
    st.write("Confira os principais projetos que realizei, com detalhes sobre objetivos, desafios e resultados.\n")

    projetos = {
        "🚀 Envio de Informe de Rendimentos": {
            "descricao": """
Disparo individual de informe de rendimentos por e-mail para cerca de 1.000 colaboradores, com custo zero para a empresa.  
Este projeto garantiu agilidade na comunicação fiscal e redução de custos com impressão e envio físico, além de melhorar a experiência dos colaboradores e retirar a carga da demanda para o departamento pessoal.
            """,
            "imagem": "assets/informe_rendimentos.jpg"
        },
        "📧 Projeto Vispera (TI)": {
            "descricao": """
Desenvolvedor do algoritmo-código base para projeto de envio de e-mails personalizados a partir de dados da plataforma Vispera.  
Implementado com sucesso para clientes como Raymundo da Fonte, Hersheys e Sococo, aumentando a eficiência na comunicação e personalização do atendimento.
            """,
            "imagem": "assets/projeto_vispera.jpg"
        },
        "📊 Centralização de Dados (Planejamento/Roteiro)": {
            "descricao": """
- Normalização de nomenclaturas, endereços e geolocalizações de todos os PDVs do compartilhado.  
- Limpeza e estruturação completa da base de contratos, servindo de modelo para replicação no sistema HERO.  

Este projeto resultou em consistência e confiabilidade nas rotas planejadas, eliminou lojas duplicadas e melhorou a integração de dados entre as equipes.  
Duração: aproximadamente 3 meses, com impacto direto na assertividade operacional.
            """,
            "imagem": "assets/centralizacao_dados.jpg"
        },
        "🗺️ Roteiros em Polígonos": {
            "descricao": """
Implementação de roteirização por aproximação espacial (polígonos) para a regional do Ceará, em parceria com o ex-supervisor Walberto.  
Essa solução otimizou a distribuição das visitas no território, contribuindo para a redução dos deslocamentos e aumento da produtividade.

A segunda etapa do roadmap, voltada para VTs, foi interrompida devido à reestruturação do setor.
            """,
            "imagem": "assets/roteiros_poligonos.jpg"
        },
        "⚙️ Programa de Margem": {
            "descricao": """
Desenvolvimento de programa automatizado para cálculo de margem da empresa (RT e CX), eliminando a necessidade de integração manual entre sistemas.  
O programa trouxe maior rapidez e precisão na visualização das informações, suportando decisões estratégicas e facilitando o acompanhamento de resultados.  
Tempo de desenvolvimento: cerca de 60 horas.
            """,
            "imagem": "assets/programa_margem.jpg"
        },
        "📈 Pesquisa x Atendimento": {
            "descricao": """
Desenvolvimento de sistema para equilibrar a carga de trabalho dos promotores das equipes compartilhadas (RT e CX).  
Essa automação permitiu distribuir as visitas de forma mais eficiente, evitando sobrecarga e garantindo melhor cobertura dos PDVs.
            """,
            "imagem": "assets/pesquisa_atendimento.jpg"
        },
        "🤖 Automações Python Office": {
            "descricao": """
Implementação de diversas automações internas, incluindo relatório de offs, layoutização de roteiros, calculadora de contratos e integração com Treasy.  
Essas soluções aumentaram a produtividade das equipes, reduziram erros manuais e facilitaram a gestão operacional.
            """,
            "imagem": "assets/automacoes_python.jpg"
        },
        "💾 Banco de Dados RT – Compartilhado (Em Execução)": {
            "descricao": """
Responsável pelo pipeline estruturado e robusto de dados operacionais, que viabiliza grandes projetos focados em performance e entrega.  
Esta estruturação fortalece a base para análises precisas e tomada de decisão baseada em dados.
            """,
            "imagem": "assets/banco_dados_rt.jpg"
        }
    }

    for titulo, dados in projetos.items():
        with st.expander(titulo):
            if dados.get("imagem"):
                st.image(dados["imagem"], width=1000)
            st.markdown(dados["descricao"].strip())
        st.write("")  # Espaço entre os expanders
    st.markdown("---")


# Página de evolução
def pagina_evolucao():
    st.title("Minha Evolução")
    st.write("Confira minha evolução técnica ao longo do tempo.")

    st.header("Onde Comecei")
    st.write("""
    - **Python**: No início, meu foco era manipulação simples de dados, criando scripts pontuais para resolver problemas específicos.
    - **Dash**: Aprendi a desenvolver web apps para visualização de dados de maneira rápida e prática, sem foco em grandes sistemas.
    - **Foco Inicial**: O objetivo era sempre resolver problemas específicos e criar entregas visuais rápidas, com a mínima integração entre as tecnologias.
    """)

    st.markdown("---")
    st.header("Onde Estou Hoje")
    st.write("""
    Após a evolução, meus conhecimentos se expandiram significativamente:
    
    - **Python Avançado**: Agora, sou capaz de modularizar o código, criando pacotes e funções reutilizáveis. Além disso, adotei boas práticas, como documentação, padronização e observabilidade.
    - **SQL**: Uso SQL no meu dia a dia, aplicando consultas, CRUD e modelagem de dados, garantindo que as informações sejam extraídas e manipuladas de forma eficiente.
    - **Git e GitHub**: Adotei o versionamento de código usando Git e GitHub, o que facilita o trabalho colaborativo e a manutenção do código.
    - **Cloud (GCP)**: Aprendi e apliquei conhecimentos gerais sobre **Google Cloud Platform (GCP)**, com foco em APIs e integrações na nuvem.
    - **Linux**: Adquiri noções de terminal Linux, automatizando processos e trabalhando com servidores, além de gerenciar cronjobs.
    - **Integrações**: Desenvolvi habilidades em protocolos de comunicação HTTP, JSON, REST e estou familiarizado com o consumo de APIs.
    """)



paginas = {
    "Sinopse Geral": pagina_sinopse,
    "Projetos": pagina_projetos,
    "Evolução Técnica": pagina_evolucao,
}

pagina_escolhida = st.sidebar.radio("Navegar para:", list(paginas.keys()))
paginas[pagina_escolhida]()
