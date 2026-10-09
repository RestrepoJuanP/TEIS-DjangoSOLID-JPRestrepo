# 1. Imagen base oficial de Python, versión ligera
FROM python:3.11-slim

# 2. Evitar archivos .pyc y activar logs sin buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Directorio de trabajo dentro del contenedor
WORKDIR /app

# 4. Dependencias primero: aprovecha la caché de capas de Docker
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 5. Código fuente
COPY . /app/

# 6. Escuchar en 0.0.0.0 para aceptar tráfico externo al contenedor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]