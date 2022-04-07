from command.validateandextractdatacommand import ValidateAndExtractDataCommand
from command.calculatepayrollcommand import CalculatePayrollCommand
from command.printresultscommand import PrintResultsCommand


class PaymentCalculatorFacade():

    def __init__(self, context):
        self.context = context

    def execute(self):
        ValidateAndExtractDataCommand(self.context).execute()
        CalculatePayrollCommand(self.context).execute()
        PrintResultsCommand(self.context).execute()
