@echo off
echo ==========================================
echo Iniciando Mi Primer Juego de Pygame...
echo ==========================================
echo Si es la primera vez, se instalará pygame automagicamente.
echo Por favor espera...
echo.

echo Intentando iniciar el juego...
python main.py
if %ERRORLEVEL% NEQ 0 (
    echo El comando 'python' falló. Probando 'python3'...
    python3 main.py
)
if %ERRORLEVEL% NEQ 0 (
    echo El comando 'python3' falló. Probando 'py' (Launcher de Windows)...
    py main.py
)


echo.
echo El juego se ha cerrado.
pause
