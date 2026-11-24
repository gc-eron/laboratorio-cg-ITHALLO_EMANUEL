import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

st.header("8. Negativo")
img1, img2 = st.columns(2)
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
negativo = 255 - img
img1.image(img, caption="Normal")
img2.image(negativo, caption="Negativo")

st.header("9. Recorte")
img1, img2 = st.columns(2)
altura = img.shape[0]
largura = img.shape[1]
limite = min(altura, largura) - 1
tamanho = st.slider("Tamanho do recorte", 1, limite, limite // 2)
coluna = st.slider("Coluna inicial", 0, largura - tamanho, 0)
linha = st.slider("Linha inicial", 0, altura - tamanho, 0)
recorte = img[linha:linha + tamanho, coluna:coluna + tamanho]
img1.image(img, caption="Normal")
img2.image(recorte, caption="Imagem recortada")

st.header("11. Espelhamento")
img1, img2 = st.columns(2)
horizontal = img[:, ::-1]
vertical = img[::-1, :]
img1.image(horizontal, caption="Espelhamento horizontal")
img2.image(vertical, caption="Espelhamento vertical")

st.header("12. Simetria")
img1, img2 = st.columns(2)
largura = img.shape[1]
meio = largura // 2
simetria = img.copy()
simetria[:, largura - meio:] = img[:, :meio][:, ::-1]
img1.image(img, caption="Normal")
img2.image(simetria, caption="Imagem com simetria")

st.header("19. Moldura")
img1, img2 = st.columns(2)
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
img1.image(img, caption=" Imagem original")
img2.image(moldura, caption="Imagem com moldura")

