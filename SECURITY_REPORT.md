# Security Audit Report for https://example.com
**Date:** 2026-10-14 20:44:22

## Header Analysis

- [ ] **Strict-Transport-Security**: Ausente ❌ -> *Falta HSTS. Riesgo de ataques Man-in-the-Middle.*
- [ ] **Content-Security-Policy**: Ausente ❌ -> *Falta CSP. Riesgo de Cross-Site Scripting (XSS).*
- [ ] **X-Frame-Options**: Ausente ❌ -> *Falta X-Frame-Options. Riesgo de Clickjacking.*
- [ ] **X-Content-Type-Options**: Ausente ❌ -> *Falta X-Content-Type-Options. Riesgo de MIME-sniffing.*

## Recomendaciones
Configurar el servidor web o el API Gateway para incluir los encabezados de seguridad faltantes y mitigar ataques comunes de cliente.