class PaymentCalculatorContext():
    entry = str()

    time_sheet_list = list()

    payroll_list = list()

    def __init__(self, entry):
        self.entry = entry


class EmployeeTimeSheet():

    def __init__(self, name, time_sheet):
        self.name = name
        self.time_sheet = time_sheet


class EmployeePayroll():

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class WorkDay():

    def __init__(self, dotw, start, end):
        self.dotw = dotw
        self.start = start
        self.end = end
