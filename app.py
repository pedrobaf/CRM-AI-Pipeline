import streamlit as st
from datetime import datetime, time

def main():

    st.title("Sistema de CRM e Vendas ZapFlow")
    email = st.text_input("E-mail do Vendedor")
    data = st.date_input("Data da compra", datetime.now())
    hora = st.time_input("Hora da compra", value=time(9, 0))  # Valor padrão: 09:00
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de vendas", min_value=1, step=1)
    produto = st.selectbox("Produto", options=["ZapFlow com Gemini", "ZapFlow com ChatGPT", "ZapFlow com Llama 3.0"])

    if st.button("Salvar"):

        data_hora = datetime.combine(data, hora)
        st.write("Dados da venda:**")
        st.write(f"Email do Vendedor: {email}")
        st.write(f"Data de Hora da Venda: {data_hora}")
        st.write(f"Valor da Venda: R$ {valor:.2f}")
        st.write(f"Quantidade de Produtos: {quantidade}")
        st.write(f"Produto: {produto}")




                    

if __name__ =="__main__": 
    main()