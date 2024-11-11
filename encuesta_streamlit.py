import streamlit as st
import psycopg2 # type: ignore
import os

# Función para conectar a la base de datos de Supabase
def conexion_base():
    try:
        return psycopg2.connect(
            host="aws-0-sa-east-1.pooler.supabase.com",   # Cambia con el host de tu base de datos de Supabase
            database="postgres",      # Cambia con el nombre de tu base de datos
            user="postgres.aapedvwloqydrfdagkte",                # Cambia con tu usuario de Supabase
            password="Km23jl9zu2@",             # Cambia con tu contraseña de Supabase
            port=6543                             # Puerto predeterminado para PostgreSQL
        )
    except psycopg2.Error as err:
        st.error(f"Error: {err}")
        return None

# Función principal
def principal():
    server = conexion_base()
    if not server:
        st.error("No se pudo conectar a la base de datos, por favor verifique su conexión.")
        return

    cursor = server.cursor()
    
    # Puedes cargar una imagen desde una URL o una ubicación accesible en Streamlit Cloud
    st.image(r"http://i12.com.ar/moodle/pluginfile.php/1/core_admin/logo/0x200/1590465306/i12Large.png")

    st.title("Encuesta")
    st.write("¡Hola! Tenemos una pequeña encuesta, espero no te moleste realizarla, ¡Muchas gracias!")

    nombre = st.text_input("Decime, ¿Cuál es tu nombre?").strip().lower()
    apellido = st.text_input("¿Y cuál es tu apellido?").strip().lower()
    direccion = st.text_input("Si no te molesta, ¿Podrías indicarnos una dirección?").strip().lower()
    telefono = st.text_input("¿Te molestaria indicarnos un teléfono? (Sin espacios ni signos)").lower().strip()
    email = st.text_input("¿Podrías indicarnos un email de contacto?").strip().lower()
    ocupacion = st.text_input("¿A qué te dedicas en este momento?").strip().lower()
    estado_civil = st.text_input("¿Cuál es tu estado civil?").lower().strip()
    hijos = st.text_input("¿Tenés hijos? ¿Cuántos?").strip().lower()
    nacionalidad = st.text_input("¿Cuál es tu nacionalidad?").strip().lower()
    nivel_de_estudios = st.text_input("¿Cuál es tu máximo nivel de estudios alcanzado?").strip().lower()
    disp_horaria = st.text_input("¿Cuál es tu disponibilidad horaria?").strip().lower()
    carrera_interesada = st.text_input("¿En qué carrera pensás anotarte?").strip().lower()

    if st.button("Enviar encuesta"):
        if nombre and apellido and direccion and telefono and email and ocupacion and estado_civil and hijos and nacionalidad and nivel_de_estudios and disp_horaria and carrera_interesada:
            sql = """INSERT INTO encuesta_streamlit 
                     (nombre, apellido, direccion, telefono, email, ocupacion, estado_civil, hijos, nacionalidad, nivel_de_estudios, disp_horaria, carrera_interesada) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            valores = (nombre, apellido, direccion, telefono, email, ocupacion, estado_civil, hijos, nacionalidad, nivel_de_estudios, disp_horaria, carrera_interesada)

            try:
                cursor.execute(sql, valores)
                server.commit()
                st.success("¡Respuestas guardadas exitosamente! Muchas gracias.")

            except psycopg2.Error as err:
                st.error(f"Hubo un error al guardar las respuestas: {err}")

            finally:
                cursor.close()
                server.close()
        else:
            st.warning("Por favor, completa todos los campos.")


if __name__ == "__main__":
    principal()
