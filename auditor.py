import requests
import argparse
import datetime

def check_security_headers(url):
    headers_to_check = {
        'Strict-Transport-Security': 'Falta HSTS. Riesgo de ataques Man-in-the-Middle.',
        'Content-Security-Policy': 'Falta CSP. Riesgo de Cross-Site Scripting (XSS).',
        'X-Frame-Options': 'Falta X-Frame-Options. Riesgo de Clickjacking.',
        'X-Content-Type-Options': 'Falta X-Content-Type-Options. Riesgo de MIME-sniffing.'
    }
    
    report_lines = [f"# Security Audit Report for {url}"]
    report_lines.append(f"**Date:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    report_lines.append("## Header Analysis\n")

    try:
        response = requests.get(url, timeout=10)
        headers = response.headers
        
        for header, warning in headers_to_check.items():
            if header in headers:
                report_lines.append(f"- [x] **{header}**: Presente ✅")
            else:
                report_lines.append(f"- [ ] **{header}**: Ausente ❌ -> *{warning}*")
                
        report_lines.append("\n## Recomendaciones")
        report_lines.append("Configurar el servidor web o el API Gateway para incluir los encabezados de seguridad faltantes y mitigar ataques comunes de cliente.")

    except requests.exceptions.RequestException as e:
        report_lines.append(f"**Error de conexión:** No se pudo alcanzar el objetivo. Detalles: {e}")

    with open("SECURITY_REPORT.md", "w", encoding="utf-8") as file:
        file.write("\n".join(report_lines))
    
    print("Auditoría completada. Resultados guardados en SECURITY_REPORT.md")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Offensive Recon & API Security Auditor")
    parser.add_argument("-t", "--target", help="URL objetivo (ej. https://example.com)", required=True)
    args = parser.parse_args()
    
    print(f"Iniciando escaneo contra: {args.target}")
    check_security_headers(args.target)