import streamlit as st
st.title('Orçamento de Computador')
st.image('banner2.png')
sdt = st.number_input('Digite o saldo total: ')
placa_mae = st.number_input('Digite o valor da placa mãe: ',min_value= 0.0)
Fonte = st.number_input('Digite o valor da Fonte: ',min_value= 0.0)
Fans = st.number_input('Digite o valor dos Fans: ',min_value= 0.0)
Memoria_RAM = st.number_input('Digite o valor da RAM: ',min_value= 0.0)
Placa_de_Video = st.number_input('Digite o valor da Placa de Video: ',min_value= 0.0)
SSD_ou_HD = st.number_input('Digite o valor do HD ou SSD: ',min_value= 0.0)
Cooler = st.number_input('Digite o valor do Cooler: ',min_value= 0.0)
Gabinete = st.number_input('Digite o valor do Gabinete: ',min_value= 0.0)
Monitor = st.number_input('Digite o valor do Monitor: ',min_value= 0.0)
Mouse = st.number_input('Digite o valor do Mouse: ',min_value= 0.0)
Teclado = st.number_input('Digite o valor do Teclado: ',min_value= 0.0)
CPU = st.number_input('Digite o valor da CPU: ',min_value= 0.0)

total = Placa_de_Video + \
CPU + \
Memoria_RAM + \
Fonte + \
Monitor + \
Cooler + \
SSD_ou_HD + \
Mouse + \
Teclado + \
Gabinete + \
Fans 

sdps = sdt-total

if st.button(f'Calcular R$ {sdps:.2f}'.replace('.',','))
    st.success(total)
if sdps <0:
    st.warning(f'faltam R$ {sdps:.2f}'.replace('.',','))
else:
    st.info(f'Sobram R$ {sdps:.2f}'.replace('.',','))
    

