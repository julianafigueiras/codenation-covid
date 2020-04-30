import streamlit as st
import pandas as pd
import seaborn as sns

def main():
    
    df = pd.read_csv('base_ajustada.csv', sep = ';', decimal = ',') 
    
    por_sexo = pd.DataFrame({'sexo':(df.SEXO.value_counts()),'%_Partic':(df.SEXO.value_counts() / df.shape[0])*100})
    faixa = pd.DataFrame({'faixa_etaria':(df.FAIXA_ETARIA.value_counts()),'%_Partic':(df.FAIXA_ETARIA.value_counts() / df.shape[0])*100})
    apoio_isol = pd.DataFrame({'apoio_isol':(df.APOIO_ISOL_SOCIAL.value_counts()),'%_Partic':(df.APOIO_ISOL_SOCIAL.value_counts() / df.shape[0])*100})
    comp_fam = pd.DataFrame({'comp_fam':(df.COMP_FAM_ISOL_SOCIAL.value_counts()),'%_Partic':(df.COMP_FAM_ISOL_SOCIAL.value_counts() / df.shape[0])*100})
    cruz = pd.DataFrame({'comp_fam':(df.COMP_FAM_ISOL_SOCIAL.value_counts()),'apoio_isol':(df.APOIO_ISOL_SOCIAL.value_counts())})
    part = pd.DataFrame({'id':(df.ID),'sexo':(df.SEXO),'faixa_etaria':(df.FAIXA_ETARIA)})
    #feminino = (pd.pivot_table(part,index=['sexo','faixa_etaria'],values=["id"],aggfunc=[len],margins=True))
    #masculino = (pd.pivot_table(part,index=['sexo','faixa_etaria'],values=["id"],aggfunc=[len],margins=True))
    
    st.sidebar.image('logo.png', width= 200)
    st.sidebar.image('Instituto-Olhar-Azul.png', width= 200)
    st.sidebar.markdown('**Créditos:** Instituto Olhar https://www.institutoolhar.com.br/')
    st.sidebar.markdown('**Veja a pesquisa na íntegra em:** https://blog.institutoolhar.com.br/termometro-da-crise-do-covid-19-3a-onda-rmbh/')   
            
    st.image('3onda.png', width= 500)
    st.title('AceleraDev Data Science')
    st.header('**Termômetro da Crise Covid 19**')
    st.subheader('Região Metropolitana de Belo Horizonte - 16 a 20 de Abril/2020')
    st.markdown('O Instituto Olhar – Pesquisa e Informação Estratégica é uma empresa que se dedica a projetos de pesquisa e inteligência de mercado para auxiliar empresas e organizações governamentais e não-governamentais em seus processos de planejamento e tomada de decisão.')
    st.subheader('Dimensões do Termômetro')
    st.markdown('O Termômetro da Crise Covid-19 é formado por quatro medidas independentes, que variam de 0 a 10, sendo 0 para discorda totalmente e 10 para apoia totalmente:')
    st.markdown('**Isolamento Social**, que mede o quanto as pessoas apoiam e estão comprometidas com o isolamento; **Medo e da Presença do Covid-19** mede o quanto as pessoas estão temerosas e sentem a presença do Covid-19; **Atuação dos Governos** que mede a avaliação da população sobre a atuação dos governos Federal, Estadual e Municipais e **Economia**, referente a percepção sobre o impacto econômico gerado pelo Covid-19, em nível Mundial, Brasil, Estadual, Municipal e na Renda Familiar.')
    st.markdown('Neste exercício trabalharemos com a medida **Isolamento Social**.')
   
    st.subheader('Conhecendo os dados')
    st.markdown('')
    
    st.markdown('**Visualizando as informações**')
    check = st.checkbox ("Clique aqui para exibir dados")
    if check:
        st.write (df)
        st.write('Quantidade de pessoas entrevistadas:',df.shape[0])
        st.markdown('')
        
    st.subheader('**Percentual de participação dos entrevistados:**')
    radio = st.radio('Escolha por:',('Por Sexo', 'Por Faixa Etária'))
    if radio == 'Por Sexo':
        st.write(por_sexo)
        st.bar_chart (por_sexo['%_Partic'])
    if radio == 'Por Faixa Etária':
        st.write(faixa)
        st.bar_chart (faixa['%_Partic'])
        #st.area_chart (faixa['%_Partic'])
        #st.line_chart (faixa['%_Partic'])
        st.markdown('')
    
    st.write(pd.crosstab(part['sexo'],part['faixa_etaria'],margins=True))

    st.subheader('**Comportamento perante ao isolamento social**:')
    st.text('*Em quantidade de entrevistados, variando termômetro de 0 a 10')
    radio = st.radio('Escolha por:',('Apoio ao isolamento social', 'Comprometimento da família'))
    if radio == 'Apoio ao isolamento social':
        st.write(apoio_isol)
        st.area_chart (apoio_isol['%_Partic'])
    if radio == 'Comprometimento da família':
        st.write(comp_fam)
        st.area_chart (comp_fam['%_Partic'])
    st.markdown('')
    
    st.subheader('**Comprometimento Familiar x Apoio ao Isolamento Social**')
    st.text('*Em quantidade de entrevistados, variando termômetro de 0 a 10')
    st.write (cruz)
    st.line_chart(cruz)
    
    st.markdown('**Matriz de Correlação:**')
    sns.heatmap(cruz.corr(), vmin=0, vmax=1, fmt='.2f', square=True, linewidths= 1, annot=True)
    st.pyplot()
    
    st.markdown('**Distribuição dos dados categóricos:**')
    sns.catplot(x="FAIXA_ETARIA", y="ID",hue="SEXO", kind='swarm', data=df, height=10, aspect=0.6)
    st.pyplot()
    
    st.markdown('**Veja a pesquisa na íntegra em:** https://blog.institutoolhar.com.br/termometro-da-crise-do-covid-19-3a-onda-rmbh/')   
    
    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('Desenvolvido por:')
    st.sidebar.markdown('**Juliana Figueiras de Souza**')
    st.sidebar.markdown('AceleraDev Data Science')

if __name__ == '__main__':
    main()



