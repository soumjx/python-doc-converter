import zipfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Generator
import logging

# Configure logging
logger = logging.getLogger(__name__)

# MS Word XML Namespaces
# Word documents are XMLs. We need to target the specific namespace for text.
WORD_NAMESPACE = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
PARA = f"{WORD_NAMESPACE}p"
TEXT = f"{WORD_NAMESPACE}t"

@dataclass
class DocumentElement:
    """
    Data Transfer Object (DTO) representing a single piece of content 
    extracted from the document.
    """
    content: str
    style: str = "Normal"

class DocxParser:
    """
    Parses a raw .docx file using Python's standard zipfile and xml libraries.
    """
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

    def _get_xml_tree(self) -> ET.Element:
        """
        Unzips the docx (which is a zip archive) and reads 'word/document.xml'.
        """
        try:
            with zipfile.ZipFile(self.file_path, 'r') as docx:
                xml_content = docx.read('word/document.xml')
                return ET.fromstring(xml_content)
        except zipfile.BadZipFile:
            raise ValueError("The provided file is not a valid docx file.")
        except KeyError:
            raise ValueError("Could not find word/document.xml inside the file.")

    def parse(self) -> Generator[DocumentElement, None, None]:
        """
        Yields document elements one by one.
        Using a generator is memory efficient for large documents.
        """
        tree = self._get_xml_tree()
        
        # Iterate over all paragraphs (<w:p>)
        for paragraph in tree.iter(PARA):
            # Extract text from all text nodes (<w:t>) inside the paragraph
            texts = [node.text for node in paragraph.iter(TEXT) if node.text]
            
            if texts:
                full_text = ''.join(texts)
                yield DocumentElement(content=full_text, style="Normal")