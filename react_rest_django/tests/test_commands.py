"""Tests for the system level commands"""
from collections import namedtuple
from unittest import mock

from django.test import TestCase
from django.core.management import call_command
from django.core.management.base import CommandError

class LintTest(TestCase):
    """Tests for the lint command"""

    @mock.patch('subprocess.call')
    def test_command_calls(self, mock_call):
        """Make sure errors in lint cause Command Exceptions."""

        # raise exception on pylint errors.
        mock_call.side_effect = lambda args: 'pylint' in args[0]
        self.assertRaises(CommandError, call_command, 'lint')

        # raise exception on tslint errors.
        mock_call.side_effect = lambda args: 'tslint' in args[0]
        self.assertRaises(CommandError, call_command, 'lint')

        # no errors, no exceptions.
        mock_call.side_effect = lambda args: 0
        call_command('lint')

class CoverageTest(TestCase):
    """Tests for the coverage command"""

    @mock.patch('subprocess.run')
    @mock.patch('subprocess.call')
    def test_command_calls(self, mock_call, mock_run):
        """Make sure errors in lint cause Command Exceptions."""

        # make sure failing tests do not show report.
        mock_call.side_effect = lambda args: 'run' in args[1]
        self.assertRaises(CommandError, call_command, 'coverage')
        mock_run.assert_not_called()

        # make sure assert if there is not 100% coverage.
        mock_call.side_effect = lambda args: 0
        mock_run.return_value = namedtuple("mock", ["stdout"])(
            stdout='{"totals": {"missing_lines": 2}}')
        self.assertRaises(CommandError, call_command, 'coverage')

        # make sure no assert if there is 100% coverage.
        mock_call.side_effect = lambda args: 0
        mock_run.return_value = namedtuple("mock", ["stdout"])(
            stdout='{"totals": {"missing_lines": 0}}')
        call_command('coverage')

class QCTest(TestCase):
    """Tests for the qc command"""

    @mock.patch('django.core.management.call_command')
    def test_command_calls(self, mock_call):
        """Make sure the qc command calls both lint and coverage."""
        call_command('qc')
        self.assertEqual(mock_call.call_args_list, [mock.call('lint'), mock.call('coverage')])
