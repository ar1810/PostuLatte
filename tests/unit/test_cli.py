import pytest
from unittest.mock import MagicMock, patch
from pathlib import Path

from src.cli.main import main
from src.domain.entities.candidate import CandidateProfile, PersonalInfo
from src.domain.entities.analysis import JobAnalysis


@patch("src.cli.main.OllamaAIService")
@patch("src.cli.main.ProfileExtractionPipeline")
def test_cli_extract_cv_success(mock_pipeline_cls, mock_ai_cls, monkeypatch, tmp_path, capsys):
    # 1. Mockear archivo de entrada
    fake_cv = tmp_path / "resume.pdf"
    fake_cv.write_text("CV Content")

    # 2. Configurar perfil simulado del dominio
    mock_profile = MagicMock(spec=CandidateProfile)
    mock_profile.model_dump_json.return_value = '{"personal": {"full_name": "Juan Perez"}}'
    
    mock_pipeline_inst = mock_pipeline_cls.return_value
    mock_pipeline_inst.execute.return_value = mock_profile

    # 3. Simular argumentos CLI: extract-cv
    test_args = ["main.py", "extract-cv", "--cv-path", str(fake_cv)]
    monkeypatch.setattr("sys.argv", test_args)

    # 4. Ejecutar CLI
    main()

    # 5. Verificaciones
    mock_pipeline_inst.execute.assert_called_once_with(fake_cv)
    captured = capsys.readouterr()
    assert '"full_name": "Juan Perez"' in captured.out


@patch("src.cli.main.JobAnalyzerWorkflow")
@patch("src.cli.main.OllamaAIService")
@patch("src.cli.main.ProfileExtractionPipeline")
def test_cli_analyze_job_success(
    mock_pipeline_cls, mock_ai_cls, mock_workflow_cls, monkeypatch, tmp_path, capsys
):
    # 1. Crear archivos temporales de prueba
    fake_cv = tmp_path / "cv.pdf"
    fake_cv.write_text("dummy cv")

    fake_job = tmp_path / "job.json"
    fake_job.write_text(
        '{"title": "Python Dev", "company": "Tech", "required_skills": ["Python"], "desired_skills": [], "raw_text": "Dev needed"}'
    )

    # 2. Mocks de resultado
    mock_analysis = MagicMock(spec=JobAnalysis)
    mock_analysis.model_dump_json.return_value = '{"match_percentage": 90.0}'
    
    mock_workflow_inst = mock_workflow_cls.return_value
    mock_workflow_inst.run.return_value = mock_analysis

    # 3. Simular argumentos CLI: analyze-job
    test_args = [
        "main.py",
        "analyze-job",
        "--cv-path",
        str(fake_cv),
        "--job-path",
        str(fake_job),
    ]
    monkeypatch.setattr("sys.argv", test_args)

    # 4. Ejecutar CLI
    main()

    # 5. Verificaciones
    captured = capsys.readouterr()
    assert '"match_percentage": 90.0' in captured.out