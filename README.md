# 📦 Lectura de Peso desde Balanza (Python)

## 📖 Descripción

Este script en Python permite leer datos desde una balanza conectada por puerto serial (COM), procesar el peso recibido y almacenarlo automáticamente en una base de datos SQL Server.

Es útil para automatizar procesos de pesaje en sistemas productivos.

---

## ⚙️ Requisitos

### 🐍 Python

* Python 3.8 o superior

### 📦 Dependencias

Instalar desde `requirements.txt`:

```bash
pip install -r requirements.txt
```

Dependencias utilizadas:

* `pyserial`
* `pyodbc`

---

## 🔌 Configuración

### 📡 Puerto serial

Modificar según tu entorno:

```python
puerto = 'COM1'
rate   = 9600
```

### 🗄️ Base de datos

Configurar cadena de conexión:

```python
conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=127.0.0.1;DATABASE=nombreBD;UID=usuario;PWD=tu_password'
)
```

⚠️ **Recomendación:** No dejar credenciales en texto plano en producción.

---

## ▶️ Funcionamiento

1. Se conecta al puerto serial configurado.
2. Lee continuamente datos enviados por la balanza.
3. Intenta decodificar usando múltiples codificaciones:

   * UTF-8
   * ISO-8859-1
   * CP1252
4. Extrae el peso usando expresiones regulares.
5. Si encuentra un valor válido:

   * Lo imprime en consola
   * Lo guarda en la base de datos

---

## 🧠 Formato esperado de datos

El script espera datos similares a:

```
12.34 kg
```

O dentro de strings separados por coma:

```
ST,GS,12.34 kg
```

---

## 🗃️ Consulta SQL utilizada

```sql
UPDATE prod_pack_peso_balanza 
SET peso = ? 
WHERE id = '1'
```

---

## 🔁 Ejecución

```bash
python script.py
```

Salida esperada:

```
Puerto = COM1
Rate   = 9600

Iniciando...
Leyendo...

12.34
12.50
12.48
```

---

## ⚠️ Manejo de errores

* Ignora líneas vacías
* Maneja errores de decodificación
* Captura errores de conexión a la base de datos

---

## 🛠️ Mejoras recomendadas

* ✅ Usar variables de entorno para credenciales
* ✅ Implementar logs en lugar de `print`
* ✅ Reutilizar conexión a base de datos (mejor rendimiento)
* ✅ Agregar validación de peso (rangos)
* ✅ Manejar reconexión automática del puerto serial

---

## 📌 Notas

* Asegúrate de que la balanza esté configurada con el mismo `baudrate`
* Verifica que el puerto COM esté disponible
* Ejecutar como administrador si es necesario (Windows)

---

## 👨‍💻 Autor

Script orientado a automatización de lectura de balanzas industriales.

---
