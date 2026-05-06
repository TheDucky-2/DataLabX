""" Module For Internal Exceptions"""

from .Constants import SUPPORTED_FILE_TYPES

# Error that gets raised when File is Empty.
class _EmptyFileError(Exception):
    """Internal Exception that gets raised if an empty file is received."""
    pass

# Error that gets raised when Invalid File Type is received.
class _InvalidFileTypeError(Exception):
    """Internal Exception that gets raised if an invalid file type is received"""

    def __init__(self, received_type: str):
        self.received_type = received_type
        super().__init__(
            f""" Received Unsupported file type: {self.received_type}. Supported file types are: {", ".join(SUPPORTED_FILE_TYPES)}."""
        )

class _FileTypeMismatchError(Exception):
    """Internal exception that gets raised when user passed optional file type does not match auto detected file type."""

    def __init__(self, expected_type: str, received_type:str, file_path:str):

        if not isinstance(expected_type, str): 
            raise TypeError(f'expected_type must be a string, got {type(expected_type).__name__}')     
            
        if not isinstance(received_type, str):
                raise TypeError(f'received_type must be a string, got {type(received_type).__name__}')
        
        if not isinstance(file_path, str):
            raise TypeError(f'file_path must be a string, got {type(file_path).__name__} ')

        self.expected_type = expected_type
        self.received_type = received_type
        self.file_path = file_path

        super().__init__(
        f"File type mismatch: expected: {self.expected_type}, received: {self.received_type} from file: {self.file_path}"
        )