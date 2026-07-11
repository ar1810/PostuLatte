import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

# src/main.py
from datetime import datetime
from src.core.config import config
from src.domain.entities import CandidateProfile, JobOffer
from src.ai import OllamaAIService

def run_test():
    print(f"☕ Iniciando simulación en {config.app_name}...")
    print(f"🤖 Conectando con el proveedor local: {config.default_provider} ({config.active_ai.model})")
    print("-" * 60)

    # 1. Simulamos el Perfil del Candidato (Molde del Dominio)
    candidato = CandidateProfile(
        full_name="Juan Pérez",
        email="juan.perez@email.com",
        location="Córdoba, Argentina",
        target_roles=["Backend Developer", "Python Developer"],
        skills=["Python", "FastAPI", "SQL", "Git", "Docker"],
        experience_years=3.5,
        experience_summary="Desarrollador Backend enfocado en la creación de APIs REST estables y optimización de consultas a bases de datos relacionales."
    )

    # 2. Simulamos una Oferta de Trabajo encontrada por el Agente
    oferta = JobOffer(
        id="job_hash_12345",
        title="Python Backend Engineer (Middle)",
        company="TechNova Solutions",
        location="Remoto (Argentina)",
        source_portal="LinkedIn",
        url="https://linkedin.com/jobs/view/12345",
        description="Estamos buscando un ingeniero Backend Python. Requisitos excluyentes: experiencia comprobable con Python y frameworks web (FastAPI/Django), manejo de SQL y Docker para contenedores. Deseable: experiencia con AWS y metodologías ágiles."
    )

    # 3. Inicializamos nuestro servicio de IA local
    ai_service = OllamaAIService()

    print("🧠 Llama 3 está analizando la compatibilidad (esto puede tomar unos segundos)...")
    print(f"⚠️ El umbral mínimo de aprobación configurado es: {config.search.min_match_score}%")
    print("-" * 60)

    # 4. Ejecutamos el análisis
    resultado = ai_service.analyze_compatibility(profile=candidato, job=oferta)

    # 5. Mostramos los resultados en consola
    print("\n📊 --- RESULTADO DEL MATCH ---")
    print(f"🎯 Puesto: {oferta.title} en {oferta.company}")
    print(f"📈 Score de Compatibilidad: {resultado.score}%")
    
    if resultado.is_approved:
        print("✅ ¡OFERTA APROBADA! Supera el filtro mínimo para postularse.")
    else:
        print("❌ Oferta descartada (No alcanza el score mínimo).")

    print(f"\n🤝 Habilidades Coincidentes: {resultado.matching_skills}")
    print(f"🔍 Habilidades Faltantes: {resultado.missing_skills}")
    print(f"\n📝 Justificación de la IA:\n{resultado.justification}")
    print("-" * 60)

if __name__ == "__main__":
    run_test()