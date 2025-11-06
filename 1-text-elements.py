import streamlit as st

st.write("Hello")


import streamlit as st

st.write('World!!!')



#import library streamlit
import streamlit as st

# bagian 1 text element
st.header("ini Header") # untuk membuat header
st.subheader("Ini Subheader") # untuk membuat subheader
st.text("ini biasa tanpa format") # untuk membuat teks biasa tanpa format
st.markdown("*ini teks bold* dan ini teks italic") # untuk membuat teks bold dan miring
st.markdown("""
- ini baris 1 
- menggunakan markdown multi baris 
1. ini baris 2
2. menggunakan markdown multi baris
* ini baris 3   
* menggunakan markdown multi baris
""")
st.caption("Ini caption") # untuk membuat teks kecil untuk penjelasan
st.title("Ini title") # untuk membuat title

#coba mandiri
st.header("Praktikum 1 Visualisasi Data")
st.subheader("Bagian 1: Teks Element")
st.markdown("""
Kelompok 21:
1. Iwanda Aulia Rosando (0110222095)
2. Rio Adi Saputro (0110122076) 
3. Shila Mumtaz (0110222039)
""")

#bagian 2 menampilkan rumus (latex)
st.header("Displaying Latex")
st.latex(r''' \cos^2\theta = 1-2\sin^2\theta ''') #rumus trigonometri
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''') #rumus kuadrat binominal

#bagian 3 menampilkan kode program
st.header("Displaying Code")
st.subheader("Python code")
#simpan ke variable
code = '''
def hello():
    print("hello streamlit!")
'''
#st.code untuk menampilkan potongan kode dengan format rapi
st.code(code, language='python')

st.subheader("Java Code")
st.code("""
        public class gpg {
            public static void main(String[] args) {
                    System.out.println("Hello World!");   
                }    
        }
""", language='java')
# Fungsi st.code digunakan untuk bahasa pemrograman lainnya

st.subheader("Javascript")
st.code("""
<p id="demo"></p>        
<script>
try {
    addalert("Welcome");
}
catch(err) {
    document.getElementById("demo").innerHTML = err.message; //
    menampilakn pesan error di elemen html dengan id "demo"
}
</script> 
""", language='javascript')