"""Helper functions to fetch model versions for Agents"""

DEFAULT_MODEL_VERSION = 'gemini-3.1-flash-lite-preview'
DEFAULT_PRO_MODEL_VERSION = 'gemini-2.5-pro'

# models to use for testing
# gemini-3.1-flash-lite-preview
# gemini-2.5-flash

def get_pro_model() -> str:
    """Return the pro model"""
    return get_base_model(DEFAULT_PRO_MODEL_VERSION)

def get_base_model(
        model_version: str = DEFAULT_MODEL_VERSION,
) -> str:
    """Return the base model"""
    return model_version