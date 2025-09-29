#!/bin/bash

# ============================================================================
# NOVA-9 Test Runner - Automated Test Execution Protocol
# ============================================================================
# Description: Runs all pytest tests with proper configuration
# Usage: ./test_run.sh [options]
# Options:
#   --verbose, -v    : Verbose output with detailed test information
#   --coverage, -c   : Run with coverage report
#   --specific, -s   : Run specific test file (e.g., -s test_llm_client.py)
# ============================================================================

set -e  # Exit on error

# Color codes for terminal output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default options
VERBOSE=""
COVERAGE=""
SPECIFIC_TEST=""

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -v|--verbose)
            VERBOSE="-v"
            shift
            ;;
        -c|--coverage)
            COVERAGE="--cov=src --cov-report=term-missing --cov-report=html"
            shift
            ;;
        -s|--specific)
            SPECIFIC_TEST="tests/$2"
            shift 2
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            exit 1
            ;;
    esac
done

echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║       NOVA-9 Test Protocol - Initiating Test Suite        ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if pytest is installed
if ! command -v pytest &> /dev/null; then
    echo -e "${RED}❌ pytest not found. Installing dependencies...${NC}"
    pip install -r requirements.txt
fi

# Check if coverage is needed but not installed
if [[ -n "$COVERAGE" ]] && ! python -c "import pytest_cov" &> /dev/null 2>&1; then
    echo -e "${YELLOW}⚠️  pytest-cov not found. Installing...${NC}"
    pip install pytest-cov
fi

echo -e "${GREEN}✓${NC} Starting test execution..."
echo ""

# Set PYTHONPATH to include the project root
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Run pytest with configured options
if [[ -n "$SPECIFIC_TEST" ]]; then
    echo -e "${BLUE}Running specific test: $SPECIFIC_TEST${NC}"
    pytest $SPECIFIC_TEST $VERBOSE $COVERAGE
else
    echo -e "${BLUE}Running all tests in tests/ directory${NC}"
    pytest tests/ $VERBOSE $COVERAGE
fi

# Capture exit code
TEST_EXIT_CODE=$?

echo ""
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}╔════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║           ✓ All Tests Passed Successfully!                ║${NC}"
    echo -e "${GREEN}║        Digital Universe Integrity: MAINTAINED             ║${NC}"
    echo -e "${GREEN}╚════════════════════════════════════════════════════════════╝${NC}"
    
    if [[ -n "$COVERAGE" ]]; then
        echo ""
        echo -e "${BLUE}📊 Coverage report generated in: htmlcov/index.html${NC}"
    fi
else
    echo -e "${RED}╔════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${RED}║              ✗ Tests Failed - Action Required             ║${NC}"
    echo -e "${RED}║        Digital Universe Integrity: COMPROMISED            ║${NC}"
    echo -e "${RED}╚════════════════════════════════════════════════════════════╝${NC}"
fi

exit $TEST_EXIT_CODE
