# src/workflow/analyze_job.py
from typing import Any
from src.domain.entities.analysis import JobAnalysis
from src.domain.entities.candidate import CandidateProfile
from src.domain.entities.job import JobDescription


class JobAnalyzerWorkflow:
    """Orquesta la comparación entre el perfil de un candidato y una oferta laboral

    para generar un informe de compatibilidad (JobAnalysis).
    """

    def __init__(self, ai_service: Any) -> None:
        self.ai_service = ai_service

    def run(self, candidate: CandidateProfile, job: JobDescription) -> JobAnalysis:
        """Ejecuta el análisis de brecha y compatibilidad."""
        prompt = self._build_prompt(candidate, job)

        analysis_result: JobAnalysis = self.ai_service.generate_structured(
            prompt=prompt,
            response_schema=JobAnalysis
        )

        return analysis_result

    def _build_prompt(self, candidate: CandidateProfile, job: JobDescription) -> str:
        """Construye las instrucciones para el LLM con la información contextualizada."""
        candidate_name = candidate.personal.full_name if candidate.personal else "Candidato"
        hard_skills = ", ".join(candidate.skills.hard_skills) if candidate.skills else ""
        soft_skills = ", ".join(candidate.skills.soft_skills) if candidate.skills else ""

        required_skills = ", ".join(job.required_skills) if job.required_skills else ""
        desired_skills = ", ".join(job.desired_skills) if job.desired_skills else ""

        return (
            "Analizá la compatibilidad entre el siguiente candidato y la oferta laboral.\n\n"
            f"=== PERFIL DEL CANDIDATO ===\n"
            f"Nombre: {candidate_name}\n"
            f"Resumen: {candidate.summary}\n"
            f"Hard Skills: {hard_skills}\n"
            f"Soft Skills: {soft_skills}\n\n"
            f"=== OFERTA DE TRABAJO ===\n"
            f"Título: {job.title}\n"
            f"Empresa: {job.company}\n"
            f"Habilidades Requeridas: {required_skills}\n"
            f"Habilidades Deseadas: {desired_skills}\n"
            f"Descripción: {job.description if hasattr(job, 'description') else job.raw_text}\n\n"
            "Determina el porcentaje de coincidencia, habilidades presentes y faltantes, "
            "fortalezas principales y sugerencias específicas de mejora."
        )