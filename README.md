# Proyecto de Automatización Web con Selenium y Python

Este repositorio contiene un framework de automatización web utilizando Selenium y Python. A continuación, se detallan los pasos para configurar el entorno y ejecutar las pruebas.

**Sitio Web de prueba:** https://www.saucedemo.com/

## Requisitos Previos

- Python 3.x
- pip (gestor de paquetes de Python)
- Navegador web (Chrome, Firefox, etc.)

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone <URL-del-repositorio>
   cd automation-swag-labs
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

## Estructura del Proyecto

- `pages/`: Contiene las clases del modelo de página.
- `screenshots/`: Contiene las capturas de pantallas cuando encuentra un fallo.
- `tests/`: Contiene las pruebas.
- `utils/`: Contiene utilidades y funciones auxiliares.
- `conftest.py`: Configuraciones y fixtures para pytest.
- `.failures.log`: Registra los fallos ocurridos al ejecutar las pruebas.
- `pytest.ini`: Archivo de configuración de pytest.
- `report.html`: Reporte generado por pytest de las pruebas.
- `requirements.txt`: Lista de dependencias del proyecto.

## Ejecución de Pruebas

Para ejecutar todas las pruebas, utiliza el siguiente comando:

```bash
pytest
```
