import pytest

from scaffold_delete.skeleton import fib, main
from scaffold_delete.skeleton import setup_logging
import logging

__author__ = "jagar2"
__copyright__ = "jagar2"
__license__ = "MIT"


def test_fib():
    """API Tests for the Fibonacci function."""
    # Test known Fibonacci values
    assert fib(1) == 1, "Fib(1) should be 1"
    assert fib(2) == 1, "Fib(2) should be 1"
    assert fib(7) == 13, "Fib(7) should be 13"
    # Test an invalid input, expecting an AssertionError
    with pytest.raises(AssertionError):
        fib(-10)


def test_main(capsys):
    """CLI Tests for the main function."""
    # capsys is a pytest fixture that allows asserts against stdout/stderr
    main(["7"])  # Simulate passing "7" as an argument to main
    captured = capsys.readouterr()
    assert (
        "The 7-th Fibonacci number is 13" in captured.out
    ), "Output should state that Fib(7) is 13"


def test_setup_logging(caplog):
    """Tests for setting up logging configuration with different levels."""

    # Test logging at INFO level
    setup_logging(logging.INFO)
    with caplog.at_level(logging.INFO):
        logging.getLogger().info("Info level log")

    # Check if "Info level log" message is in caplog records at the INFO level
    assert any(
        record.levelname == "INFO" and "Info level log" in record.message
        for record in caplog.records
    ), "Info level log should appear in caplog at INFO level"

    # Test logging at DEBUG level
    setup_logging(logging.DEBUG)
    with caplog.at_level(logging.DEBUG):
        logging.getLogger().debug("Debug level log")

    # Check if "Debug level log" message is in caplog records at the DEBUG level
    assert any(
        record.levelname == "DEBUG" and "Debug level log" in record.message
        for record in caplog.records
    ), "Debug level log should appear in caplog at DEBUG level"
