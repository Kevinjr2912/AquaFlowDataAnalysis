# AquaFlowDataAnalysis

## Descripción del Proyecto

**AquaFlowDataAnalysis** es una API desarrollada con **FastAPI** diseñada para brindar a los usuarios información en tiempo real sobre:

- **Índice de Calidad de Agua (ICA)**  
- **Estado del filtro de agua**, calculado según el uso y las mediciones registradas
- **Procesamiento de datos de sensores IoT** (pH, TDS, temperatura y turbidez)
- **Datos externos del clima** (vía API de clima)

Este servicio forma parte del ecosistema AquaFlow, encargado de recibir y analizar datos de los sensores y brindar métricas útiles para la salud del agua y mantenimiento del filtrador.

---

## Tecnologías Utilizadas

- **Python**
- **FastAPI**
- **Pydantic**
- **SQLAlchemy / Conexión a base de datos**
- **Uvicorn** (servidor ASGI)
- Integración con API externa de clima

---

## Ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/Kevinjr2912/AquaFlowDataAnalysis.git
cd AquaFlowDataAnalysis
```

### 2. Crear un entorno virtual

python3 -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
La API requiere las siguientes variables de entorno:

DB_HOST=tu_host
DB_USER=tu_usuario
DB_PASSWORD=tu_password
DB_DATABASE=nombre_base_datos
VITE_WEATHER_API_KEY=api_key_clima

### 5. Ejecutar el servidor
```bash
uvicorn main:app --reload
````

El servidor estará disponible en:
http://127.0.0.1:8000

