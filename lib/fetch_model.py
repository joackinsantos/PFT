"""Helper functions to fetch model versions for Agents"""

DEFAULT_MODEL_VERSION = 'gemini-2.5-flash'
DEFAULT_PRO_MODEL_VERSION = 'gemini-2.5-pro'

def get_pro_model() -> str:
    """Return the pro model"""
    return get_base_model(DEFAULT_PRO_MODEL_VERSION)

def get_base_model(
        model_version: str = DEFAULT_MODEL_VERSION,
) -> str:
    """Return the base model"""
    return model_version