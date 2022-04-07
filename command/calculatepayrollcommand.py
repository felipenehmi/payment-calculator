from command.base import BaseCommand
from config import Config
from context.paymentcalculator import EmployeePayroll


class CalculatePayrollCommand(BaseCommand):

    def __init__(self, context):
        self.context = context

    def execute(self):
        for employee_time_sheet in self.context.time_sheet_list:
            amount = self.calculate_amount(employee_time_sheet.time_sheet)
            self.context.payroll_list.append(
                EmployeePayroll(employee_time_sheet.name, amount)
            )

    def calculate_amount(self, time_sheet):
        return sum(self.calculate_day(work_day) for work_day in time_sheet)

    def calculate_day(self, work_day):
        base = Config.WEEKDAY_BASE
        if work_day.dotw in ['SA', 'SU']:
            base = Config.WEEKEND_BASE

        day_hours = evening_hours = overnight_hours = 0
        for hour in range(work_day.start, work_day.end):
            if hour < 9:
                overnight_hours += 1
            elif hour < 18:
                day_hours += 1
            else:
                evening_hours += 1

        return day_hours * base \
            + evening_hours * (base + Config.EVENING_EXTRA) \
            + overnight_hours * (base + Config.OVERNIGHT_EXTRA)
