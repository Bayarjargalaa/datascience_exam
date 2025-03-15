import logging

# Лог файлуудын байршил
TRAINING_LOG_FILE = "logs/training.log"
ERROR_LOG_FILE = "logs/errors.log"
PIPELINE_LOG_FILE = "logs/pipeline.log"

# Лог формат
log_format = "%(asctime)s - %(levelname)s - %(message)s"

# Training лог тохиргоо (UTF-8 кодчилол нэмсэн)
logging.basicConfig(
    filename=TRAINING_LOG_FILE,
    level=logging.INFO,
    format=log_format,
    encoding="utf-8"  
)
training_logger = logging.getLogger("training_logger")

# Error лог тохиргоо (UTF-8 кодчилол нэмсэн)
error_logger = logging.getLogger("error_logger")
error_handler = logging.FileHandler(ERROR_LOG_FILE, encoding="utf-8")
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(logging.Formatter(log_format))
error_logger.addHandler(error_handler)

# Pipeline лог тохиргоо (UTF-8 кодчилол нэмсэн)
pipeline_logger = logging.getLogger("pipeline_logger")
pipeline_handler = logging.FileHandler(PIPELINE_LOG_FILE, encoding="utf-8") 
pipeline_handler.setLevel(logging.INFO)
pipeline_handler.setFormatter(logging.Formatter(log_format))
pipeline_logger.addHandler(pipeline_handler)
