# src/cli/main.py
import argparse
import json
from pathlib import Path
from typing import Any, List, Optional

from src.domain.entities.candidate import CandidateProfile, PersonalInfo, SkillsInfo
from src.domain.entities.job import JobDescription
from src.workflow.analyze_job import JobAnalyzerWorkflow


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="PostuLatte - Asistente de optimización de candidaturas laborales"
    )
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")

    analyze_parser = subparsers.add_parser(
        "analyze", help="Analiza la compatibilidad entre un CV y una oferta"
    )
    analyze_parser.add_argument(
        "--cv", "-c", required=True, type=Path, help="Ruta al archivo PDF/DOCX del CV"
    )
    analyze_parser.add_argument(
        "--job", "-j", required=True, type=Path, help="Ruta al JSON de la oferta"
    )

    return parser


def run_cli(args: Optional[List[str]] = None, ai_service: Optional[Any] = None) -> int:
    parser = create_parser()
    parsed_args = parser.parse_args(args)

    if parsed_args.command == "analyze":
        cv_path: Path = parsed_args.cv
        job_path: Path = parsed_args.job

        if not cv_path.exists():
            print(f"Error: El archivo de CV '{cv_path}' no existe.")
            return 1

        if not job_path.exists():
            print(f"Error: El archivo de oferta '{job_path}' no existe.")
            return 1

        print("Cargando datos...")

        with open(job_path, "r", encoding="utf-8") as f:
            job_data = json.load(f)
        job_entity = JobDescription(**job_data)

        candidate_entity = CandidateProfile(
            personal=PersonalInfo(full_name="Candidato Extraído"),
            skills=SkillsInfo(hard_skills=["Python", "SQL", "Git"]),
        )

        # Si no nos pasan un mock desde el test, instanciamos el servicio
        if ai_service is None:
            from src.ai import ollama_client
            # Si el cliente no se pasa, busca la primera clase disponible en el módulo
            ai_service = getattr(ollama_client, "OllamaClient", None) or getattr(ollama_client, "OllamaService", None)()

        workflow = JobAnalyzerWorkflow(ai_service=ai_service)

        print("Analizando compatibilidad con IA...")
        result = workflow.run(candidate=candidate_entity, job=job_entity)

        print("\n=== INFORME DE COMPATIBILIDAD ===")
        print(f"Coincidencia: {result.match_percentage}%")
        print(f"Habilidades Coincidentes: {', '.join(result.matching_skills)}")
        print(f"Habilidades Faltantes: {', '.join(result.missing_skills)}")
        print(f"Fortalezas: {', '.join(result.key_strengths)}")
        print(f"Sugerencias: {', '.join(result.improvement_suggestions)}")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(run_cli())