import streamlit as st
import mysql.connector


def conexion_base():
    try:
        return mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password=None,
            database="encuesta"
        )
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return None

# Función principal
def principal():
    server = conexion_base()
    if not server:
        st.error("No se pudo conectar a la base de datos, por favor verifique su conexión.")
        return

    cursor = server.cursor()
    
    st.image(r"C:\Users\maxim\Downloads\cropped-dbi12Large.png")

    st.title("Encuesta")
    st.write("¡Hola! Tenemos una pequeña encuesta, espero no te moleste realizarla, ¡Muchas gracias!")

    
    nombre = st.text_input("Decime, ¿Cual es tu nombre?").strip().lower()
    apellido = st.text_input("¿Y cuál es tu apellido?").strip().lower()
    direccion = st.text_input("Si no te molesta, ¿Podrías indicarnos una dirección?").strip().lower()
    email = st.text_input("¿Podrias indicarnos un email de contacto?").strip().lower()
    ocupacion = st.text_input("¿A qué te dedicas en este momento?").strip().lower()
    estado_civil = st.selectbox("¿Cuál es tu estado civil?", ["soltero", "casado", "otro"])
    hijos = st.text_input("¿Tenés hijos? ¿Cuántos?").strip().lower()
    nacionalidad = st.text_input("¿Cuál es tu nacionalidad?").strip().lower()
    nivel_de_estudios = st.text_input("¿Cuál es tu máximo nivel de estudios alcanzado?").strip().lower()
    disp_horaria = st.text_input("¿Cuál es tu disponibilidad horaria?").strip().lower()
    carrera_interesada = st.text_input("¿En qué carrera pensás anotarte?").strip().lower()

    
    if st.button("Enviar encuesta"):
        if nombre and apellido and direccion and email and ocupacion and estado_civil and hijos and nacionalidad and nivel_de_estudios and disp_horaria and carrera_interesada:
            sql = """INSERT INTO encuesta 
                     (nombre, apellido, direccion, email, ocupacion, estado_civil, hijos, nacionalidad, nivel_de_estudios, disp_horaria, carrera_interesada) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            valores = (nombre, apellido, direccion, email, ocupacion, estado_civil, hijos, nacionalidad, nivel_de_estudios, disp_horaria, carrera_interesada)

            try:
                cursor.execute(sql, valores)
                server.commit()
                st.success("¡Respuestas guardadas exitosamente! Muchas gracias.")

            except mysql.connector.Error as err:
                st.error(f"Hubo un error al guardar las respuestas: {err}")

            finally:
                cursor.close()
                server.close()
        else:
            st.warning("Por favor, completa todos los campos.")


if __name__ == "__main__":
    principal()
