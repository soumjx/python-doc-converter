# src/docgo/main.py
import argparse
import sys
import logging
from pathlib import Path

# Relative imports handling to allow running this as a module
try:
    from .core import DocxParser
    from .formatters import get_formatter
except ImportError:
    # Fallback if run directly without -m (debugging purposes)
    from core import DocxParser
    from formatters import get_formatter

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="DocGo: Convert DOCX to other formats (Core Python).")
    parser.add_argument("input_file", help="Path to the input .docx file")
    parser.add_argument("format", choices=["md", "html", "csv"], help="Target format")
    parser.add_argument("--output", "-o", help="Output file path (e.g., output/result.html)")

    args = parser.parse_args()

    try:
        # 1. Parse Input
        logger.info(f"Reading {args.input_file}...")
        parser_obj = DocxParser(args.input_file)
        elements = parser_obj.parse()

        # 2. Select Strategy (Formatter)
        formatter = get_formatter(args.format)
        
        # 3. Convert
        logger.info(f"Converting to {args.format.upper()}...")
        result = formatter.convert(elements)

        # 4. Output
        if args.output:
            out_path = Path(args.output)
            
            # --- Industry Standard Practice ---
            # Ensure the output directory exists. If 'output/' folder is missing,
            # this command creates it automatically.
            out_path.parent.mkdir(parents=True, exist_ok=True)

            out_path.write_text(result, encoding="utf-8")
            logger.info(f"Success! Saved to {out_path}")
        else:
            # If no output file is provided, print to console
            print("\n--- Output Preview ---\n")
            print(result)
            print("\n----------------------\n")

    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()