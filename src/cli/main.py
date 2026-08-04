# src/cli/main.py
import argparse
import json
import logging
import sys
from pathlib import Path

from src.ai.ollama_client import OllamaAIService
from src.core.application import ProfileExtractionPipeline
from src.domain.entities.job import JobDescription
from src.workflow.analyze_job import JobAnalyzerWorkflow


def setup_logger() -> logging.Logger:
    logger = logging.getLogger("PostuLatteCLI")
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter("[%(levelname)s] %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="PostuLatte - Asistente inteligente para candidaturas laborales impulsado por IA local."
    )
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")

    # Comando 1: extract-cv
    cv_parser = subparsers.add_parser(
        "extract-cv", help="Extrae y genera la entidad CandidateProfile desde un CV."
    )
    cv_parser.add_argument(
        "--cv-path",
        type=Path,
        required=True,
        help="Ruta al archivo CV (PDF o DOCX).",
    )
    cv_parser.add_argument(
        "--output",
        type=Path,
        required=False,
        help="Ruta de destino opcional para guardar el resultado en JSON.",
    )

    # Comando 2: analyze-job
    job_parser = subparsers.add_parser(
        "analyze-job", help="Analiza la compatibilidad entre un perfil y una oferta laboral."
    )
    job_parser.add_argument(
        "--cv-path",
        type=Path,
        required=True,
        help="Ruta al archivo CV del candidato.",
    )
    job_parser.add_argument(
        "--job-path",
        type=Path,
        required=True,
        help="Ruta al archivo JSON con la descripción del trabajo.",
    )

    return parser


def main() -> None:
    logger = setup_logger()
    parser = build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    try:
        # Instanciación de servicios compartidos
        ai_service = OllamaAIService()

        if args.command == "extract-cv":
            if not args.cv_path.exists():
                logger.error(f"El archivo especificado no existe: {args.cv_path}")
                sys.exit(1)

            pipeline = ProfileExtractionPipeline(ai_service=ai_service)
            logger.info(f"Procesando CV en: {args.cv_path}")
            profile = pipeline.execute(args.cv_path)

            profile_json = profile.model_dump_json(indent=2)
            if args.output:
                args.output.write_text(profile_json, encoding="utf-8")
                logger.info(f"Perfil exportado exitosamente en: {args.output}")
            else:
                print(profile_json)

        elif args.command == "analyze-job":
            if not args.cv_path.exists():
                logger.error(f"El archivo de CV no existe: {args.cv_path}")
                sys.exit(1)
            if not args.job_path.exists():
                logger.error(f"El archivo de oferta laboral no existe: {args.job_path}")
                sys.exit(1)

            # 1. Pipeline para perfil
            pipeline = ProfileExtractionPipeline(ai_service=ai_service)
            profile = pipeline.execute(args.cv_path)

            # 2. Cargar datos de la vacante
            with open(args.job_path, "r", encoding="utf-8") as f:
                job_raw = json.load(f)
            job = JobDescription(**job_raw)

            # 3. Orquestar análisis
            workflow = JobAnalyzerWorkflow(ai_service=ai_service)
            logger.info("Iniciando análisis de compatibilidad laboral...")
            analysis_result = workflow.run(candidate=profile, job=job)

            print(analysis_result.model_dump_json(indent=2))

    except Exception as e:
        logger.error(f"Ocurrió un error inesperado durante la ejecución: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()