$ErrorActionPreference = 'Stop'

# Start the API server in background
Write-Host "Iniciando servidor API..."
$p = Start-Process -FilePath "python" -ArgumentList "api.py" -PassThru

# Esperar a que el servidor esté arriba
Start-Sleep -Seconds 2

Write-Host "Ejecutando script de demostración..."
python test_demo.py

Write-Host "Pruebas completadas. Deteniendo servidor..."
Try {
    Stop-Process -Id $p.Id -Force
} Catch {
    Write-Warning "No se pudo detener el proceso del servidor: $_"
}

Write-Host "Demo finalizada."
