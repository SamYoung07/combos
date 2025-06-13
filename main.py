import PIL.Image
from PIL import Image
import streamlit as st
import random
st.set_page_config(page_title = "Combo Generator", page_icon="🥊")
st.title("Combo Generator")
st.write("Randomly Generate a Boxing Combo")

options = [3,4,5]
jab = Image.open("jab.jpg")
cross = Image.open("cross.jpg")
l_hook = Image.open("l-hook.jpg")
r_hook = Image.open("d-hook.jpg")#r dont work :(
l_cut = Image.open("l-uppercut.jpg")
r_cut = Image.open("d-uppercut.jpg")#r dont work :(
slip = Image.open("slip.jpg")

moves = [jab, jab, jab, jab, cross, cross, cross, l_hook, r_hook, l_cut, r_cut, slip, slip]

left, middle, right = st.columns(3)
if middle.button("CREATE"):
    num = random.choice(options)
    for i in range(num):
        middle.image(random.choice(moves))
