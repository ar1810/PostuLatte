# tests/unit/test_prompt_builder.py
import json
import pytest
from src.ai.prompt_builder import PromptBuilder

def test_prompt_builder_initialization():
    """Valida que el PromptBuilder se instancie correctamente y contenga la plantilla esperada."""
    builder = PromptBuilder()
    assert builder._template is not None
    assert "personal" in builder._template
    assert "skills" in builder._template

def test_build_system_instructions_contains_strict_rules():
    """Valida que el System Prompt contenga las reglas críticas de extracción
    y las directivas estrictas de formato.
    """
    builder = PromptBuilder()
    instructions = builder.build_system_instructions()
    
    assert "REGLAS CRÍTICAS DE EXTRACCIÓN" in instructions
    assert "lista vacía `[]`" in instructions
    assert "asigna null" in instructions
    assert "ÚNICAMENTE el objeto JSON válido" in instructions

def test_build_system_instructions_includes_valid_json_schema():
    """Valida que la plantilla JSON inyectada dentro de las instrucciones sea parseable
    y contenga la estructura del perfil.
    """
    builder = PromptBuilder()
    instructions = builder.build_system_instructions()
    
    # El prompt debe contener la estructura
    assert "personal" in instructions
    assert "skills" in instructions
    
    # Extraer la porción JSON del prompt para verificar que sea parseable
    marker = "Estructura JSON requerida:\n"
    json_start_idx = instructions.find(marker) + len(marker)
    json_str = instructions[json_start_idx:].strip()
    
    parsed_template = json.loads(json_str)
    assert isinstance(parsed_template, dict)
    assert "personal" in parsed_template
    assert "experience" in parsed_template

def test_build_user_message_formatting():
    """Valida que el mensaje del usuario aísle e inserte correctamente el texto bruto."""
    builder = PromptBuilder()
    raw_text = "Diego Silva - QA Tester - Python, SQL"
    user_message = builder.build_user_message(raw_text)
    
    assert raw_text in user_message
    assert "Texto bruto del CV a procesar:" in user_message