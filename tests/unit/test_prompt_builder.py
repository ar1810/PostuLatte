# tests/unit/test_prompt_builder.py
import json
import pytest
from src.ai.prompt_builder import PromptBuilder
from src.domain.entities import CandidateProfile

def test_prompt_builder_initialization():
    """Valida que el PromptBuilder se instancie correctamente y extraiga el esquema."""
    builder = PromptBuilder()
    assert builder._schema is not None
    assert "properties" in builder._schema

def test_build_system_instructions_contains_strict_rules():
    """Valida que el System Prompt contenga las directivas de la Política de Extracción Pura
    y la directiva estricta de contenedores vacíos sin ambigüedades.
    """
    builder = PromptBuilder()
    instructions = builder.build_system_instructions()
    
    assert "Cero Tolerancia a la Alucinación" in instructions
    assert "[] para colecciones" in instructions
    assert '"" para campos de texto' in instructions
    assert "ÚNICAMENTE el objeto JSON válido" in instructions

def test_build_system_instructions_includes_valid_json_schema():
    """Valida que el esquema inyectado dentro de las instrucciones sea rastreable
    y fiel al modelo del dominio CandidateProfile.
    """
    builder = PromptBuilder()
    instructions = builder.build_system_instructions()
    
    # El prompt debe contener la estructura del esquema
    assert "personal" in instructions
    assert "skills" in instructions
    
    # Extraer la porción JSON del prompt para verificar que sea parseable
    marker = "Esquema JSON requerido:\n"
    json_start_idx = instructions.find(marker) + len(marker)
    json_str = instructions[json_start_idx:].strip()
    
    parsed_schema = json.loads(json_str)
    assert parsed_schema["type"] == "object"
    assert "properties" in parsed_schema

def test_build_user_message_formatting():
    """Valida que el mensaje del usuario aísle e inserte correctamente el texto bruto."""
    builder = PromptBuilder()
    raw_text = "Juan Pérez - Desarrollador Python - Python, SQL"
    user_message = builder.build_user_message(raw_text)
    
    assert raw_text in user_message
    assert "Texto bruto del CV a procesar:" in user_message