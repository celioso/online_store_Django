#!/bin/bash

echo "Activando entorno virtual..."

# Verificar que exista el entorno virtual
if [ ! -d "venv" ]; then
    echo "Error: no se encontró la carpeta 'venv'"
    exit 1
fi

# Activar entorno virtual
source venv/bin/activate

echo "Entorno virtual activado"
echo "Para salir usa: deactivate"

# Mantener la sesión activa
exec "$SHELL"