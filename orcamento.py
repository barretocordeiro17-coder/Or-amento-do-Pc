import streamlit as st

st.title('Orçamento de Computador')

# Banner
st.image('banner2.png')

# Saldo total
sdt = st.number_input('Digite o saldo total:', min_value=0.0)

# Componentes
placa_mae = st.number_input('Digite o valor da placa mãe:', min_value=0.0)
Fonte = st.number_input('Digite o valor da Fonte:', min_value=0.0)
Fans = st.number_input('Digite o valor dos Fans:', min_value=0.0)
Memoria_RAM = st.number_input('Digite o valor da RAM:', min_value=0.0)
Placa_de_Video = st.number_input('Digite o valor da Placa de Vídeo:', min_value=0.0)
SSD_ou_HD = st.number_input('Digite o valor do HD ou SSD:', min_value=0.0)
Cooler = st.number_input('Digite o valor do Cooler:', min_value=0.0)
Gabinete = st.number_input('Digite o valor do Gabinete:', min_value=0.0)
Monitor = st.number_input('Digite o valor do Monitor:', min_value=0.0)
Mouse = st.number_input('Digite o valor do Mouse:', min_value=0.0)
Teclado = st.number_input('Digite o valor do Teclado:', min_value=0.0)
CPU = st.number_input('Digite o valor da CPU:', min_value=0.0)

# Soma total
total = (
    placa_mae +
    Placa_de_Video +
    CPU +
    Memoria_RAM +
    Fonte +
    Monitor +
    Cooler +
    SSD_ou_HD +
    Mouse +
    Teclado +
    Gabinete +
    Fans
)

# Saldo depois da soma
sdps = sdt - total

# Botão
if st.button('Calcular'):
    
    st.success(f'Total gasto: R$ {total:.2f}'.replace('.', ','))

    if sdps < 0:
        st.warning(f'Faltam R$ {abs(sdps):.2f}'.replace('.', ','))
    else:
        st.info(f'Sobram R$ {sdps:.2f}'.replace('.', ','))
