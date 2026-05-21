"""src/datafun/app_case.py - Project script (example).

Author: Denise Case, Hannah Sacco
Date: 2026-04

  Practice key Python skills related to:
    - imports
    - logging
    - pathlib for cross-platform file paths
    - type hints
    - global constants with Final
    - functions
    - repetition patterns:
        - for loop over a numeric range
        - for loop over a list
        - list comprehension
        - while loop with a counter
    - main function
    - conditional execution guard

  Terminal command to run this file from the root project folder:

    uv run python -m datafun.app_hasacco_numbers

OBS:
  Don't edit this file - it should remain a working example.
  Copy it, rename it, and modify your copy.

  This is a copy of the instructor's file and has been modified.
"""

# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
from pathlib import Path
import time
from typing import Final

from datafun_toolkit.logger import get_logger, log_header

# === CONFIGURE LOGGER ONCE PER MODULE (PYTHON FILE) ===

LOG: logging.Logger = get_logger("P02", level="INFO")

# === DECLARE GLOBAL CONSTANTS ===

ROOT_DIR: Final[Path] = Path.cwd()
DATA_DIR: Final[Path] = ROOT_DIR / "data"
PROCESSED_DIR: Final[Path] = DATA_DIR / "processed"

FIRST_SIX_WEEKS: Final[int] = 1
LAST_SIX_WEEKS: Final[int] = 6

EXAM_LIST: Final[list[str]] = [
    "Unit 1",
    "Unit 2",
    "Unit 3",
    "1st Semester Exam",
    "Unit 4",
    "Unit 5",
    "Unit 6",
    "2nd Semester Exam",
]

SENTINEL_VALUE: Final[int] = -1

WAIT_SECONDS: Final[int] = 1


# === DECLARE A HELPER FUNCTION TO WRITE A FILE ===


def write_text_file(*, path: Path, content: str) -> None:
    """Write content to a text file, creating parent directories as needed.

    Arguments:
        path: Full path to the file to create or overwrite.
        content: Text content to write.

    Returns:
        None
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    LOG.info(f"Wrote file: {path.name}")


# === DECLARE REPETITION FUNCTION 1: FOR LOOP OVER A NUMERIC RANGE ===


def create_files_from_numeric_range() -> None:
    """Create one text file per six weeks using a for loop over a range.

    WHY: Use range() when repeating logic a known number of times.
    range(start, stop + 1) produces start, start+1, ..., stop (inclusive).

    Arguments: None
    Returns: None
    """
    LOG.info("========================")
    LOG.info("FUNCTION 1: for loop over a numeric range")
    LOG.info("========================")

    LOG.info(f"First six weeks: {FIRST_SIX_WEEKS}")
    LOG.info(f"Last six weeks:  {LAST_SIX_WEEKS}")

    for week_number in range(FIRST_SIX_WEEKS, LAST_SIX_WEEKS + 1):
        filename: str = f"hasacco_sixweeks_{week_number}.txt"
        path: Path = PROCESSED_DIR / filename
        content: str = f"Grade report for Six Weeks number {week_number}:\n"
        write_text_file(path=path, content=content)


# === DECLARE REPETITION FUNCTION 2: FOR LOOP OVER A LIST ===


def create_files_from_list() -> None:
    """Create one text file per exam in a list using a for loop.

    WHY: Use a for loop over a list when repeating logic for each item.
    The loop variable takes on each value in the list, one at a time.

    Arguments: None
    Returns: None
    """
    LOG.info("========================")
    LOG.info("FUNCTION 2: for loop over a list")
    LOG.info("========================")

    LOG.info(f"Exam list: {EXAM_LIST}")

    for exam_name in EXAM_LIST:
        filename: str = f"hasacco_{exam_name}.txt"
        path: Path = PROCESSED_DIR / filename
        content: str = f"Exam scores for '{exam_name}':\n"
        write_text_file(path=path, content=content)


# === DECLARE REPETITION FUNCTION 3: LIST COMPREHENSION ===


def create_files_using_list_comprehension() -> None:
    """Create one intervention text file per exam in a transformed list.

    WHY: Use a list comprehension to transform one list into another.
    Read it as: <expression> FOR each <item> IN <list>.
    List comprehensions are more concise than a for loop building a new list.

    Arguments: None
    Returns: None
    """
    LOG.info("========================")
    LOG.info("FUNCTION 3: list comprehension")
    LOG.info("========================")

    prefix: str = "intervention_"

    LOG.info(f"Original list: {EXAM_LIST}")
    intervention_list: list[str] = [f"{prefix}{name}" for name in EXAM_LIST]
    LOG.info(f"Transformed list: {intervention_list}")

    for intervention in intervention_list:
        filename: str = f"hasacco_{intervention}.txt"
        path: Path = PROCESSED_DIR / filename
        content: str = "Students with performance needing targeted interventions: \n"
        write_text_file(path=path, content=content)


# === DECLARE REPETITION FUNCTION 4: WHILE LOOP ===


def intervention_group_assignment() -> None:
    """Use a while loop to assign students to intervention groups based on a user input test grade while also inputting scores into exam text files.

    Arguments: None
    Returns: None
    """
    LOG.info("========================")
    LOG.info("FUNCTION 4: while loop with sentinel value")
    LOG.info("========================")

    LOG.info(f"Sentinel value to stop the loop: {SENTINEL_VALUE}")
    LOG.info(f"Seconds between inputs: {WAIT_SECONDS}")

    prefix: str = "intervention_"
    intervention_cutoff: int = 70

    current_exam: str = input(
        f"Enter the name of the current exam from exam list(e.g., '{EXAM_LIST[0]}'): "
    )
    i: int = int(
        input(
            f"Enter a test grade determine need for intervention group (or {SENTINEL_VALUE} to stop): "
        )
    )
    student_name: str = input("Enter the student's name: ")

    while i != SENTINEL_VALUE:
        with Path.open(
            PROCESSED_DIR / f"hasacco_{current_exam}.txt", mode="a", encoding="utf-8"
        ) as file:
            file.write(f"Student: {student_name}, Test Grade: {i}\n")
        with Path.open(
            PROCESSED_DIR / f"hasacco_{prefix}{current_exam}.txt",
            mode="a",
            encoding="utf-8",
        ) as file:
            if i < intervention_cutoff:
                file.write(f"Student: {student_name}, Test Grade: {i}\n")
        LOG.info(f"Waiting {WAIT_SECONDS} second(s)...")
        time.sleep(WAIT_SECONDS)
        i = int(
            input(
                f"Enter a test grade determine need for intervention group (or {SENTINEL_VALUE} to stop): "
            )
        )
        if i == SENTINEL_VALUE:
            break
        student_name = input("Enter the student's name: ")


# === DEFINE THE MAIN FUNCTION THAT CALLS OTHER FUNCTIONS ===


def main() -> None:
    """Entry point when running this file as a Python script.

    Arguments: None
    Returns: None
    """
    log_header(LOG, "P02")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    create_files_from_numeric_range()
    create_files_from_list()
    create_files_using_list_comprehension()
    intervention_group_assignment()

    LOG.info("========================")
    LOG.info("Executed successfully!")
    LOG.info("========================")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: Only call main() when running this file directly as a script.
# This is standard Python boilerplate.

if __name__ == "__main__":
    main()
