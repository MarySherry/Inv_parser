from pathlib import Path


NEIGHBOURS = 5
HEADS = 4
EMBEDDING_SIZE = 16
VOCAB_SIZE = 1000
BATCH_SIZE = 16
EPOCHS = 20
LR = 0.0001

current_directory = Path.cwd()
XML_DIR = current_directory / "data" / "xmls"
OCR_DIR = current_directory / "data" / "tesseract_results_lstm"
IMAGE_DIR = current_directory / "data" / "images"
CANDIDATE_DIR = current_directory / "data" / "candidates"
SPLIT_DIR = current_directory / "data" / "split"
OUTPUT_DIR = current_directory / "output"

if not OUTPUT_DIR.exists():
    OUTPUT_DIR.mkdir(parents=True)