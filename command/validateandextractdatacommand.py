import re
from command.base import BaseCommand
from context.paymentcalculator import EmployeeTimeSheet, WorkDay
from exceptions import InvalidInputFormatError, InvalidHourRangeError


class ValidateAndExtractDataCommand(BaseCommand):

    def __init__(self, context):
        self.context = context

    def execute(self):
        dotw_pattern = "(MO|TU|WE|TH|FR|SA|SU)"
        hour_pattern = "((([0-1][0-9])|([2][0-3])):00)"
        dotw_hour_pattern = "{0}{1}-{1}".format(dotw_pattern, hour_pattern)
        entry_regex = re.compile("^[A-Z]+={0}(,{0})*$".format(dotw_hour_pattern))
        for entry in self.context.entry.split('\n'):
            if entry_regex.match(entry) is None:
                raise InvalidInputFormatError("Invalid Input: " + entry)

            self.extract_data(entry)

    def extract_data(self, employee_entry):
        parts = employee_entry.split('=')
        self.context.time_sheet_list.append(
            EmployeeTimeSheet(parts[0], self.extract_time_sheet(parts[1]))
        )

    def extract_time_sheet(self, time_sheet_entry):
        parts = time_sheet_entry.split(',')
        time_sheet = list()
        for part in parts:
            dow = part[0:2]
            start = int(part[2:4])
            end = int(part[8:10])

            self.validate_hour_range(start, end, time_sheet_entry)
            time_sheet.append(WorkDay(dow, start, end))

        return time_sheet

    def validate_hour_range(self, start, end, entry):
        if start == end:
            raise InvalidHourRangeError("Invalid hour range: " + entry)
