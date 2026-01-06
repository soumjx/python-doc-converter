import csv
import io
from abc import ABC, abstractmethod
from typing import Iterable
from .core import DocumentElement

class BaseFormatter(ABC):
    """
    Abstract Base Class (Interface) for all formatters.
    Enforces that every formatter must have a convert method.
    """
    @abstractmethod
    def convert(self, elements: Iterable[DocumentElement]) -> str:
        pass

class MarkdownFormatter(BaseFormatter):
    def convert(self, elements: Iterable[DocumentElement]) -> str:
        lines = []
        for el in elements:
            lines.append(f"{el.content}\n")
        return "\n".join(lines)

class HtmlFormatter(BaseFormatter):
    def convert(self, elements: Iterable[DocumentElement]) -> str:
        lines = ["<!DOCTYPE html>", "<html>", "<body>"]
        for el in elements:
            # Escape HTML characters could be added here for safety
            lines.append(f"  <p>{el.content}</p>")
        lines.append("</body>")
        lines.append("</html>")
        return "\n".join(lines)

class CsvFormatter(BaseFormatter):
    def convert(self, elements: Iterable[DocumentElement]) -> str:
        """Converts paragraphs to a single-column CSV string."""
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["Content"])  # Header
        
        for el in elements:
            writer.writerow([el.content])
            
        return output.getvalue()

def get_formatter(format_type: str) -> BaseFormatter:
    """Factory function to retrieve the correct strategy."""
    formatters = {
        "md": MarkdownFormatter(),
        "html": HtmlFormatter(),
        "csv": CsvFormatter(),
    }
    formatter = formatters.get(format_type.lower())
    if not formatter:
        raise ValueError(f"Unsupported format: {format_type}")
    return formatter