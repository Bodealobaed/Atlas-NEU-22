from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_canvas_uses_supported_api():
    source = (ROOT / 'segmentation_editor.py').read_text()
    assert 'image_to_url' not in source
    assert 'display_toolbar=' not in source
    assert "['freedraw','rect','polygon']" in source
    assert "getattr(canvas, 'json_data', None)" in source

def test_canvas_dependency_pinned_to_v2():
    requirements = (ROOT / 'requirements.txt').read_text()
    assert 'streamlit>=1.53,<2' in requirements
    assert 'streamlit-drawable-canvas==0.13.0' in requirements
