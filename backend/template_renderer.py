from docxtpl import DocxTemplate
from pathlib import Path
import logging

logger = logging.getLogger("docgen.template_renderer")

def render_docx(template_path: str, context: dict, out_path: str):
    """
    Renders a docx Jinja template with the provided context and saves it.
    `template_path` - path to a docx with docxtpl placeholders (Jinja)
    `context` - dict of placeholders -> values
    `out_path` - file path to write the rendered docx
    """
    tpl = DocxTemplate(template_path)
    tpl.render(context or {})
    tpl.save(out_path)
    logger.info("Saved rendered DOCX to %s", out_path)

import subprocess

def convert_to_pdf(docx_path: str, out_dir: str):
    """
    Converts a DOCX file to PDF using LibreOffice (soffice).
    """
    try:
        # LibreOffice headless conversion
        cmd = [
            'soffice',
            '--headless',
            '--convert-to', 'pdf',
            '--outdir', out_dir,
            docx_path
        ]
        
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        logger.info(f"PDF Conversion successful: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"PDF Conversion failed: {e.stderr}")
        return False
    except Exception as e:
        logger.exception(f"Unexpected error during PDF conversion: {e}")
        return False