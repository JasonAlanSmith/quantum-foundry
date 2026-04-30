"""

"""


class DataFarmError(Exception):
    """Base exception for Quantum Foundry."""
    pass


class EmptyInputFileError(DataFarmError):
    """Raised when an input file contains no usable data."""
    pass
