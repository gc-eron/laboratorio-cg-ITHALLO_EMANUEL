import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

st.header("8. Negativo")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
negativo = 255 - img
st.image(img, caption="Imagem original")
st.image(negativo, caption="Imagem negativa")

st.header("9. Recorte")
altura = img.shape[0]
largura = img.shape[1]
limite = min(altura, largura) - 1
tamanho = st.slider("Tamanho do recorte", 1, limite, limite // 2)
coluna = st.slider("Coluna inicial", 0, largura - tamanho, 0)
linha = st.slider("Linha inicial", 0, altura - tamanho, 0)
recorte = img[linha:linha + tamanho, coluna:coluna + tamanho]
st.image(recorte, caption="Imagem recortada")

st.header("11. Espelhamento")
horizontal = img[:, ::-1]
vertical = img[::-1, :]
st.image(horizontal, caption="Espelhamento horizontal")
st.image(vertical, caption="Espelhamento vertical")

st.header("12. Simetria")
largura = img.shape[1]
meio = largura // 2
simetria = img.copy()
simetria[:, largura - meio:] = img[:, :meio][:, ::-1]
st.image(simetria, caption="Imagem com simetria")

st.header("19. Moldura")
espessura = st.slider("Espessura da moldura", 1, 75, 12)
vermelho = st.slider("Vermelho", 0, 255, 255)
verde = st.slider("Verde", 0, 255, 0)
azul = st.slider("Azul", 0, 255, 0)
cor = [vermelho, verde, azul]
moldura = img.copy()
moldura[:espessura, :] = cor
moldura[-espessura:, :] = cor
moldura[:, :espessura] = cor
moldura[:, -espessura:] = cor
st.image(img, caption=" Imagem original")
st.image(moldura, caption="Imagem com moldura")

