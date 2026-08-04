from unittest.mock import MagicMock, patch

from src.cli.main import run_cli


@patch("src.cli.main.JobAnalyzerWorkflow")
def test_cli_analyze_job_success(mock_workflow, capsys):
    """Verifica que el comando 'analyze' procese correctamente el CV y la oferta."""
    mock_workflow_instance = MagicMock()
    mock_workflow.return_value = mock_workflow_instance

    mock_analysis = MagicMock()
    mock_analysis.match_percentage = 85
    mock_analysis.matching_skills = ["Python", "Git"]
    mock_analysis.missing_skills = ["Docker"]
    mock_analysis.key_strengths = ["Buena base técnica"]
    mock_analysis.improvement_suggestions = ["Sumar experiencia en contenedores"]

    mock_workflow_instance.run.return_value = mock_analysis

    mock_ai_service = MagicMock()

    exit_code = run_cli(
        args=[
            "analyze",
            "--cv", "tests/fixtures/pdf/simple_resume.pdf",
            "--job", "tests/fixtures/jobs/python_developer_job.json",
        ],
        ai_service=mock_ai_service
    )

    captured = capsys.readouterr()

    assert exit_code == 0
    assert "85%" in captured.out
    assert "Python" in captured.out