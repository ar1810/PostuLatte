class UnsupportedDocumentError(Exception):
    """
    Se lanza cuando se intenta abrir un formato de documento
    que PostuLatte todavía no soporta.
    """