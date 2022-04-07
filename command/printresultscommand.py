from command.base import BaseCommand


class PrintResultsCommand(BaseCommand):

    def __init__(self, context):
        self.context = context

    def execute(self):
        for payroll in self.context.payroll_list:
            print('The amount to pay to ' + payroll.name + ' is: ' + str(payroll.amount))
