# test_endpoints.py

import requests
import sys

def print_resultado(texto, ok=True):
    if ok:
        print(f"✅ {texto}")
    else:
        print(f"❌ {texto}")

def probar_endpoint(url, method="GET", json_data=None):
    try:
        if method == "GET":
            response = requests.get(url, timeout=3)
        else:
            response = requests.post(url, json=json_data, timeout=3)
        
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, f"Error {response.status_code}: {response.text}"
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    print("\n=== PRUEBAS DE ENDPOINTS FRANKO.AR ===\n")
    
    base_url = "http://localhost:8000"
    
    # Verificar que el servidor esté corriendo
    server_ok, _ = probar_endpoint(base_url)
    if not server_ok:
        print_resultado("Servidor no está ejecutándose", False)
        print("Ejecuta: cd mvp/backend && uvicorn main:app --reload")
        return
    
    print_resultado("Servidor en ejecución")
    
    # Probar endpoints básicos
    endpoints = [
        ("/personajes", "GET", None),
        ("/avatar", "GET", None),
        ("/historia", "GET", None),
        ("/preguntar", "POST", {"pregunta": "¿Quién eres?"}),
        ("/personajes_cercanos", "POST", {"lat": 40.7128, "lng": -74.0060, "radio": 100})
    ]
    
    for endpoint, method, data in endpoints:
        url = base_url + endpoint
        ok, resultado = probar_endpoint(url, method, data)
        
        if ok:
            print_resultado(f"Endpoint {endpoint} funciona correctamente")
        else:
            print_resultado(f"Endpoint {endpoint} falló", False)
            print(f"  {resultado}")
    
    print("\nPruebas completadas.")

if __name__ == "__main__":
    main()